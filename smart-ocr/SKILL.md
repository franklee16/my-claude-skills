---
name: smart-ocr
description: Extract text from images, screenshots, scanned PDFs, and photos using PaddleOCR. Supports 100+ languages including Chinese, English, Japanese, Korean, and handwritten text, returning text with bounding-box position and confidence scores. Use when the user asks to OCR an image, extract text from a picture or scan, read text from a photo, or digitize printed or handwritten documents.
---

# Smart OCR Skill

Extract text from images and scanned documents using **PaddleOCR** (PP-OCRv6, paddleocr 3.7.0 installed in miniconda base).

## Verified working setup (this machine)

Two Windows-specific gotchas, both verified 2026-10-02:

1. **`import torch` BEFORE any paddle import.** If paddle loads first, torch's `shm.dll` fails with WinError 127 and the `paddleocr` import chain (paddlex → modelscope → torch) crashes. Import order fixes it.
2. **`enable_mkldnn=False` is mandatory.** With MKLDNN on (the default), paddlepaddle 3.3.1 on Windows raises `NotImplementedError: ConvertPirAttribute2RuntimeAttribute ... onednn_instruction.cc` at inference.

```python
import torch  # MUST precede paddle imports (DLL conflict on Windows)
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en', use_textline_orientation=True, enable_mkldnn=False)
result = ocr.predict('image.png')
r = result[0]                    # one result per input image
texts  = r['rec_texts']          # list of strings
confs  = r['rec_scores']         # list of floats (0–1)
boxes  = r['rec_boxes']          # list of [x1, y1, x2, y2] arrays
```

Use the miniconda Python: `/c/Users/frank/miniconda3/python.exe` (the `python` on PATH is a Store stub).

First run downloads models (~100 MB) to `~/.paddlex/official_models/` — subsequent runs use the cache.

## Language codes

`en` English · `ch` Simplified Chinese · `cht` Traditional Chinese · `japan` Japanese · `korean` Korean · `french` · `german` · `spanish` · `russian` · `arabic` · `hindi` · `vi` Vietnamese · `th` Thai. Use `lang='ch'` for mixed Chinese/English documents.

## Scanned PDFs

Render pages with PyMuPDF at 200–300 dpi, then OCR each page:

```python
import fitz  # pymupdf
import torch
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en', use_textline_orientation=True, enable_mkldnn=False)

def ocr_pdf(pdf_path, first=0, last=None):
    doc = fitz.open(pdf_path)
    last = last if last is not None else len(doc)
    all_text = []
    for i in range(first, last):
        pix = doc[i].get_pixmap(dpi=200)
        img_path = f'page_{i+1}.png'
        pix.save(img_path)
        r = ocr.predict(img_path)[0]
        page_text = '\n'.join(t for t, c in zip(r['rec_texts'], r['rec_scores']) if c > 0.5)
        all_text.append(f'--- Page {i+1} ---\n{page_text}')
        import os; os.remove(img_path)
    return '\n\n'.join(all_text)
```

Practical note: for this folder's image-only criteria PDFs, OCR works well (verified: 57 lines at ~0.99 confidence on `Annual Performance Review 2027/EF-202627-Academic-Approved.pdf` page 1).

## Ordering output by position

`predict()` returns lines in detection order, roughly top-to-bottom, but for multi-column layouts sort by box position:

```python
lines = list(zip(r['rec_texts'], r['rec_scores'], r['rec_boxes']))
lines.sort(key=lambda x: (x[2][1], x[2][0]))  # sort by top, then left
```

## Preprocessing (only when accuracy is poor)

Grayscale + contrast boost + sharpen, via PIL:

```python
from PIL import Image, ImageEnhance, ImageFilter
img = Image.open(p).convert('L')
img = ImageEnhance.Contrast(img).enhance(2.0)
img = img.filter(ImageFilter.SHARPEN)
img.save(p_processed)
```

## API notes (paddleocr 3.x)

- `predict()` replaces 2.x's `ocr()`. Old snippets using `ocr.ocr(img, cls=True)` and `use_angle_cls=True` are obsolete: the parameter is `use_textline_orientation`, and results are dicts keyed `rec_texts` / `rec_scores` / `rec_boxes`, not the 2.x `[box, (text, conf)]` tuples.
- `use_gpu` is not a parameter — device selection is automatic (CPU build installed here).
- Suppress the harmless `RequestsDependencyWarning` (chardet/urllib3 version notice) if it clutters output; it does not affect results.

## Limitations

- Handwritten text accuracy varies
- Very small text may need higher render dpi (300)
- Complex backgrounds reduce accuracy
- CPU-only on this machine (paddlepaddle CPU build)
