# fitz-wrapper
CLI Utilities for PDF to Image Conversion, built with Py3

## Installation

### 1. Download
Git clone this repo:

`git clone https://github.com/NirantK/fitz-wrapper.git`

OR

[Download as zip](https://github.com/NirantK/fitz-wrapper/archive/master.zip) and then unzip

### 2. Setup
In your terminal/shell, `cd` to the `fitz-wrapper` directory and install all dependencies with:

`pip install -r requirements.txt`

## Usage

Extract images from a sample pdf:
```
Usage:    python pdf_image_handling.py --pdf PDF --out OUT {convert, extract}
```

Example Usage for Extracting Images:

```bash
python pdf_image_handling.py --pdf sample.pdf --out sample_out extract
```

This will extract all images in your pdf to a directory called `sample_out` created relative to present directory


Example Usage for Converting to Images:

```bash
python -m pdf_image_handling --pdf sample.pdf --out output convert
```

This will convert all the pdf pages to images (1 image per page) in your pdf to a directory called `output`. This directory is created relative to present directory

You can see more help with:
`python pdf_image_handling.py -- --help`
