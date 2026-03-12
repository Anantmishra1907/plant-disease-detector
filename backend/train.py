"""
Train the PlantVillage plant disease detection model.

Dataset:
https://www.kaggle.com/datasets/emmarex/plantdisease
https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset

Usage:
python train.py --data_dir /path/to/PlantVillage --epochs 25 --batch_size 32
"""

import argparse
import os
import copy
import time

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader
from tqdm import tqdm

import torchvision.transforms as transforms
import torchvision.datasets as datasets

from model.predictor import PlantDiseaseModel
from model.class_labels import NUM_CLASSES
# ─────────────────────────────────────────────
# Image transforms
# ─────────────────────────────────────────────
MEAN = [0.485, 0.456, 0.406]
STD  = [0.229, 0.224, 0.225]
train_transforms = transforms.Compose([
    transforms.RandomResizedCrop(224, scale=(0.7, 1.0)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.RandomRotation(30),
    transforms.ColorJitter(brightness=0.3, contrast=0.3,
                           saturation=0.3, hue=0.1),
    transforms.RandomGrayscale(p=0.05),
    transforms.ToTensor(),
    transforms.Normalize(mean=MEAN, std=STD),
])

val_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=MEAN, std=STD),
])


# ─────────────────────────────────────────────
# Training loop
# ─────────────────────────────────────────────

def train_one_epoch(model, loader, criterion, optimizer, device):

    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    progress = tqdm(loader, desc="Training", leave=False)

    for inputs, labels in progress:

        inputs = inputs.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        running_loss += loss.item() * inputs.size(0)

        _, preds = torch.max(outputs, 1)

        correct += (preds == labels).sum().item()
        total += labels.size(0)

    return running_loss / total, correct / total


# ─────────────────────────────────────────────
# Validation loop
# ─────────────────────────────────────────────

@torch.no_grad()
def evaluate(model, loader, criterion, device):

    model.eval()

    running_loss = 0.0
    correct = 0
    total = 0

    progress = tqdm(loader, desc="Validation", leave=False)

    for inputs, labels in progress:

        inputs = inputs.to(device)
        labels = labels.to(device)

        outputs = model(inputs)
        loss = criterion(outputs, labels)

        running_loss += loss.item() * inputs.size(0)

        _, preds = torch.max(outputs, 1)

        correct += (preds == labels).sum().item()
        total += labels.size(0)

    return running_loss / total, correct / total


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main(args):

    # Device detection (MPS / CUDA / CPU)
    device = torch.device(
        "mps" if torch.backends.mps.is_available()
        else "cuda" if torch.cuda.is_available()
        else "cpu"
    )

    print(f"Training on: {device}")

    # Dataset paths
    train_dir = os.path.join(args.data_dir, "train")

    val_dir = os.path.join(args.data_dir, "valid")
    if not os.path.isdir(val_dir):
        val_dir = os.path.join(args.data_dir, "val")

    # Datasets
    train_dataset = datasets.ImageFolder(train_dir,
                                         transform=train_transforms)

    val_dataset = datasets.ImageFolder(val_dir,
                                       transform=val_transforms)

    # DataLoaders (stable for macOS)
    train_loader = DataLoader(
        train_dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=0,
        pin_memory=False
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=0,
        pin_memory=False
    )

    print(f"Train samples: {len(train_dataset)} | Val samples: {len(val_dataset)}")
    print(f"Classes: {len(train_dataset.classes)}")

    # Model
    model = PlantDiseaseModel(
        num_classes=NUM_CLASSES,
        pretrained=True
    ).to(device)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

    optimizer = optim.AdamW(
        model.parameters(),
        lr=args.lr,
        weight_decay=1e-4
    )

    scheduler = CosineAnnealingLR(
        optimizer,
        T_max=args.epochs
    )

    # ───────────────── Phase 1 ─────────────────

    for param in model.model.features.parameters():
        param.requires_grad = False

    print("\n=== Phase 1: Training classifier head ===")

    for epoch in range(min(5, args.epochs)):

        start = time.time()

        train_loss, train_acc = train_one_epoch(
            model, train_loader, criterion, optimizer, device
        )

        val_loss, val_acc = evaluate(
            model, val_loader, criterion, device
        )

        scheduler.step()

        print(
            f"Epoch {epoch+1:02d} | "
            f"Train Loss {train_loss:.4f} Acc {train_acc*100:.2f}% | "
            f"Val Loss {val_loss:.4f} Acc {val_acc*100:.2f}% | "
            f"{time.time()-start:.1f}s"
        )

    # ───────────────── Phase 2 ─────────────────

    print("\n=== Phase 2: Full fine-tuning ===")

    for param in model.parameters():
        param.requires_grad = True

    for pg in optimizer.param_groups:
        pg["lr"] = args.lr * 0.1

    best_acc = 0.0
    best_weights = copy.deepcopy(model.state_dict())

    for epoch in range(5, args.epochs):

        start = time.time()

        train_loss, train_acc = train_one_epoch(
            model, train_loader, criterion, optimizer, device
        )

        val_loss, val_acc = evaluate(
            model, val_loader, criterion, device
        )

        scheduler.step()

        if val_acc > best_acc:
            best_acc = val_acc
            best_weights = copy.deepcopy(model.state_dict())
            print(f"✓ New best validation accuracy: {best_acc*100:.2f}%")

        print(
            f"Epoch {epoch+1:02d} | "
            f"Train Loss {train_loss:.4f} Acc {train_acc*100:.2f}% | "
            f"Val Loss {val_loss:.4f} Acc {val_acc*100:.2f}% | "
            f"{time.time()-start:.1f}s"
        )

    # ───────────────── Save Model ─────────────────

    os.makedirs("model/weights", exist_ok=True)

    save_path = "model/weights/plant_disease_model.pth"

    torch.save({
        "model_state_dict": best_weights,
        "val_accuracy": best_acc,
        "num_classes": NUM_CLASSES,
        "epochs_trained": args.epochs,
    }, save_path)

    print("\nModel saved →", save_path)
    print(f"Best Validation Accuracy: {best_acc*100:.2f}%")


# ───────────────── CLI ─────────────────

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Train Plant Disease Classifier"
    )

    parser.add_argument(
        "--data_dir",
        type=str,
        required=True,
        help="Path to dataset root"
    )

    parser.add_argument(
        "--epochs",
        type=int,
        default=25
    )

    parser.add_argument(
        "--batch_size",
        type=int,
        default=32
    )

    parser.add_argument(
        "--lr",
        type=float,
        default=1e-3
    )

    args = parser.parse_args()

    main(args)