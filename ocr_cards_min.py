"""
Greeting Card OCR Script
Extracts text from greeting card images using Tesseract OCR and saves the output to a CSV file.
Work in progress — currently being tested and refined.
"""


from pathlib import Path
import pytesseract
from PIL import Image
import pandas as pd

IMG_DIR = Path("/path/to/Greeting_Card_Archive/Originals")  # change this
OUT_CSV = Path("cards_ocr.csv")
EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}

def ocr_text(p):
    try:
        img = Image.open(p).convert("RGB")
        return pytesseract.image_to_string(img)
    except Exception:
        return ""

if OUT_CSV.exists():
    existing = pd.read_csv(OUT_CSV)
    processed = set(existing["file_name"].tolist())
else:
    existing, processed = pd.DataFrame(), set()

new_rows = []
for p in IMG_DIR.rglob("*"):
    if p.suffix.lower() in EXTS and p.name not in processed:
        text = (ocr_text(p) or "").strip()
        title = text.splitlines()[0].strip() if text else ""
        new_rows.append({
            "file_name": p.name,
            "folder_path": str(p.parent),
            "title_on_card": title,
            "text_on_card": text
        })

if new_rows:
    df = pd.concat([existing, pd.DataFrame(new_rows)], ignore_index=True)
    df.to_csv(OUT_CSV, index=False)
    print(f"Added {len(new_rows)} new cards. Total: {len(df)}")
else:
    print("No new images found — everything already processed.")
