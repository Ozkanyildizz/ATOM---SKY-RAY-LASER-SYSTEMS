import os
from pathlib import Path
import csv

# Ayarlar
IMAGES_DIR = Path("../images")       # Görseller
LABELS_CSV = Path("labels.csv")   # CSV dosyası
OUTPUT_DIR = Path("../yolo_dataset/labels")  # YOLO .txt çıkışı

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

with open(LABELS_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        filename = row['filename']
        xmin = float(row['x'])
        ymin = float(row['y'])
        width = float(row['w'])
        height = float(row['h'])
        xmax = xmin + width
        ymax = ymin + height

        # Görsel boyutunu al
        img_path = IMAGES_DIR / filename
        if not img_path.exists():
            print(f"WARNING: {filename} bulunamadı!")
            continue
        from PIL import Image
        img_w, img_h = Image.open(img_path).size

        # YOLO formatına dönüştür
        x_center = ((xmin + xmax) / 2.0) / img_w
        y_center = ((ymin + ymax) / 2.0) / img_h
        w_norm = width / img_w
        h_norm = height / img_h

        # .txt dosyasına yaz
        txt_path = OUTPUT_DIR / f"{Path(filename).stem}.txt"
        with open(txt_path, "w") as f:
            f.write(f"0 {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n")

print("YOLO etiket dosyaları oluşturuldu!")
