import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import numpy as np
import os
from typing import List, Dict

from .class_labels import CLASS_LABELS, NUM_CLASSES


class PlantDiseaseModel(nn.Module):
    """
    MobileNetV2-based plant disease classifier.
    Fine-tuned on the PlantVillage dataset (38 classes).
    """

    def __init__(self, num_classes: int = 38, pretrained: bool = True):
        super(PlantDiseaseModel, self).__init__()
        self.model = models.mobilenet_v2(pretrained=pretrained)
        # Replace the classifier head
        in_features = self.model.classifier[1].in_features
        self.model.classifier = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(in_features, 512),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(512, num_classes)
        )

    def forward(self, x):
        return self.model(x)


class PlantDiseasePredictor:
    """
    Handles model loading and inference for plant disease detection.
    Falls back to a demo mode if no trained weights are found.
    """

    MODEL_PATH = os.path.join(os.path.dirname(__file__), "weights", "plant_disease_model.pth")

    # ImageNet normalization (same used during training on PlantVillage)
    MEAN = [0.485, 0.456, 0.406]
    STD  = [0.229, 0.224, 0.225]

    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=self.MEAN, std=self.STD),
        ])

        self.model = self._load_model()
        self.model.eval()

    def _load_model(self) -> nn.Module:
        model = PlantDiseaseModel(num_classes=NUM_CLASSES, pretrained=False)

        if os.path.exists(self.MODEL_PATH):
            print(f"Loading trained weights from {self.MODEL_PATH}")
            checkpoint = torch.load(self.MODEL_PATH, map_location=self.device)
            # Support both raw state_dict and checkpoint dicts
            state_dict = checkpoint.get("model_state_dict", checkpoint)
            model.load_state_dict(state_dict)
            print("Custom weights loaded successfully.")
        else:
            print("WARNING: No trained weights found. Using ImageNet pretrained weights for demo.")
            print(f"Train the model and place weights at: {self.MODEL_PATH}")
            # Load ImageNet pretrained for demonstration
            model = PlantDiseaseModel(num_classes=NUM_CLASSES, pretrained=True)

        return model.to(self.device)

    @torch.no_grad()
    def predict(self, image: Image.Image, top_k: int = 5) -> List[Dict]:
        """
        Run inference on a PIL Image.

        Args:
            image: PIL.Image in RGB format
            top_k: number of top predictions to return

        Returns:
            List of dicts: [{"class": str, "confidence": float}, ...]
        """
        tensor = self.transform(image).unsqueeze(0).to(self.device)  # (1, 3, 224, 224)
        logits = self.model(tensor)  # (1, 38)
        probs  = torch.softmax(logits, dim=1)[0]  # (38,)

        top_probs, top_indices = torch.topk(probs, k=min(top_k, NUM_CLASSES))

        results = []
        for prob, idx in zip(top_probs.cpu().numpy(), top_indices.cpu().numpy()):
            results.append({
                "class":      CLASS_LABELS[idx],
                "confidence": round(float(prob) * 100, 2),
                "class_idx":  int(idx)
            })

        return results
