# Greeting Card Database Automation

> **⚠️ Status: Work in Progress**  
> This project is currently in active development and testing. The code may contain bugs or incomplete features. Use at your own risk and feel free to report issues or contribute improvements!

When I began updating SEO for my website and integrating new Pinterest content, I realized how difficult it was to locate specific greeting card designs. Over the years I created thousands of cards, but they were scattered across different computers and folders with inconsistent file names. Without a clear naming convention or searchable system, finding the right files for republishing or linking was slow and disorganized.

This project organizes those designs into a single searchable database. It uses a Google Sheet for tagging and organization, and a Python script that automatically extracts text from each card image using OCR (Tesseract) and updates a CSV file.

The result is a simple, maintainable system for locating cards by the text printed on them, as well as by color, occasion, or design type.

## Goals

- Locate any card by the exact text printed on it
- Filter by color, occasion, and style (icons, gifs, charcoal, lettering)
- Prepare assets for reuse in projects such as Pinterest posts or Photoshop edits

## System Overview

The system includes two parts:

1. A Google Sheet that serves as the database for tagging and metadata
2. A Python script that automatically extracts text from card images and updates a CSV file

Together, these tools convert a large, unorganized image collection into a structured, searchable archive.

## Google Sheet Structure

| Column | Description |
|--------|-------------|
| `file_name` | Standardized name for each card (e.g. `birthday_lettering_pink_flowers_2011.jpg`) |
| `folder_path` | File location on disk (e.g. `/Originals/Birthdays`) |
| `title_on_card` | The first line of visible text on the card |
| `text_on_card` | The full visible text extracted with OCR |
| `main_color` | The dominant color, added manually later |
| `occasion` | Category such as Birthday, Love, Sympathy, etc. |
| `year` | Year created, if known |
| `notes` | Optional details about design or variations |
| `icons` / `gifs` / `charcoal` / `lettering` | Yes/No flags for the type or medium of the design |

The top two rows are color-coded and frozen to keep the naming pattern visible while scrolling.

## Python OCR Script

The script [`ocr_cards_min.py`](ocr_cards_min.py) scans all images in the `Originals` folder, extracts text with Tesseract, and appends results to a CSV. It skips any images already processed.

## Requirements

```bash
pip install pillow pytesseract pandas
```

Tesseract must also be installed locally. Installation instructions:
- **macOS**: `brew install tesseract`
- **Ubuntu/Debian**: `sudo apt-get install tesseract-ocr`
- **Windows**: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)

## Running the Script

```bash
python ocr_cards_min.py
```

This generates `cards_ocr.csv`, which can be imported into the Google Sheet or linked directly using a formula such as:

```
=IMPORTDATA("https://raw.githubusercontent.com/<user>/<repo>/main/cards_ocr.csv")
```

## Workflow

1. Copy new card files into the `Originals` folder
2. Run the Python script to extract text and update the CSV
3. Import or refresh the CSV data in Google Sheets
4. Add color, occasion, and style tags manually as needed

## Current Work and Next Steps

This project is actively being developed while I continue organizing and tagging the archive. I'm currently working on:

- Adding automatic color detection and color-name mapping
- Connecting the script directly to the Google Sheets API for live updates
- Building a small search interface with image previews and filters
- Improving batch file renaming and tag suggestions





## Contact

[Add your contact information or link to your website]
