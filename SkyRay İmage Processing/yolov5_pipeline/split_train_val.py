import os
import shutil
import random
from pathlib import Path

# Ayarlar
DATASET_DIR = Path(__file__).parent.parent / "yolo_dataset"  # yolo_dataset klasörü
TRAIN_RATIO = 0.8  # %80 train, %20 val

def main():
    random.seed(42)

    images_dir = DATASET_DIR / "images"
    labels_dir = DATASET_DIR / "labels"

    train_images_dir = DATASET_DIR / "train/images"
    train_labels_dir = DATASET_DIR / "train/labels"
    val_images_dir = DATASET_DIR / "val/images"
    val_labels_dir = DATASET_DIR / "val/labels"

    # Klasörleri oluştur
    for d in [train_images_dir, train_labels_dir, val_images_dir, val_labels_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # Hem .jpg hem .png dosyalarını al
    images = sorted(list(images_dir.glob("*.jpg")) + list(images_dir.glob("*.png")))
    n = len(images)
    if n == 0:
        print(f"ERROR: '{images_dir}' klasöründe hiç görsel bulunamadı!")
        return

    train_count = int(TRAIN_RATIO * n)
    idx = list(range(n))
    random.shuffle(idx)
    train_idx = set(idx[:train_count])

    for i, img_path in enumerate(images):
        label_path = labels_dir / f"{img_path.stem}.txt"

        if i in train_idx:
            shutil.copy(img_path, train_images_dir / img_path.name)
            if label_path.exists():
                shutil.copy(label_path, train_labels_dir / label_path.name)
        else:
            shutil.copy(img_path, val_images_dir / img_path.name)
            if label_path.exists():
                shutil.copy(label_path, val_labels_dir / label_path.name)

    print("Train/Validation bölme tamamlandı.")
    print(f"Train images: {len(list(train_images_dir.glob('*.*')))}")
    print(f"Validation images: {len(list(val_images_dir.glob('*.*')))}")

if __name__ == "__main__":
    main()
