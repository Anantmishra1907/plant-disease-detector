"""
Download a pre-trained PlantVillage model from Hugging Face Hub.

Several community-trained PlantVillage models are available:
  - linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification
  - beingamit99/plant-disease-detection

Run this script once before starting the server if you don't
want to train from scratch.

Usage:
    pip install huggingface_hub
    python download_weights.py
"""

import os
import sys
import torch
import torch.nn as nn
import torchvision.models as models


def download_from_huggingface():
    """
    Downloads weights via huggingface_hub if available.
    """
    try:
        from huggingface_hub import hf_hub_download
    except ImportError:
        print("Install huggingface_hub first:  pip install huggingface_hub")
        sys.exit(1)

    os.makedirs(os.path.join("model", "weights"), exist_ok=True)

    print("Downloading model from Hugging Face Hub ...")
    # Community PlantVillage model (MobileNetV2 compatible architecture)
    path = hf_hub_download(
        repo_id="linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification",
        filename="pytorch_model.bin",
        local_dir=os.path.join("model", "weights"),
    )
    print(f"Downloaded to: {path}")
    print("\nNOTE: Community HF weights may need an adapter layer — see README.")


def create_demo_weights():
    """
    Creates an ImageNet-pretrained MobileNetV2 weight file as a
    working demo when no PlantVillage-trained weights are available.
    The model will load but predictions won't be meaningful until
    fine-tuned on the PlantVillage dataset.
    """
    from model.predictor import PlantDiseaseModel
    from model.class_labels import NUM_CLASSES

    os.makedirs(os.path.join("model", "weights"), exist_ok=True)
    save_path = os.path.join("model", "weights", "plant_disease_model.pth")

    print("Creating ImageNet-pretrained demo weights ...")
    model = PlantDiseaseModel(num_classes=NUM_CLASSES, pretrained=True)
    torch.save({
        "model_state_dict": model.state_dict(),
        "note": "ImageNet pretrained only — fine-tune on PlantVillage for real predictions.",
    }, save_path)
    print(f"Saved → {save_path}")
    print("⚠ These are demo weights only. Run train.py for real performance.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", choices=["huggingface", "demo"], default="demo",
                        help="'huggingface' to download from HF Hub, 'demo' for ImageNet-only weights")
    args = parser.parse_args()

    if args.source == "huggingface":
        download_from_huggingface()
    else:
        create_demo_weights()
