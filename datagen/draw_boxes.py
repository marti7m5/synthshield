from pathlib import Path
from PIL import Image, ImageDraw

base_dir = Path(__file__).resolve().parent
image_dir = base_dir / "output"
label_dir = base_dir / "annotations"
preview_dir = base_dir / "preview"
preview_dir.mkdir(exist_ok=True)

for image_path in sorted(image_dir.glob("*.png")):
    label_path = label_dir / f"{image_path.stem}.txt"
    if not label_path.exists():
        continue

    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size

    with open(label_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 5:
                continue

            cls, x_center, y_center, bw, bh = parts
            x_center = float(x_center) * w
            y_center = float(y_center) * h
            bw = float(bw) * w
            bh = float(bh) * h

            x1 = x_center - bw / 2
            y1 = y_center - bh / 2
            x2 = x_center + bw / 2
            y2 = y_center + bh / 2

            draw.rectangle([x1, y1, x2, y2], outline="red", width=3)

    out_path = preview_dir / image_path.name

    # Save labeled image only
    img.save(out_path)

print("Preview images with boxes created in:", preview_dir)
