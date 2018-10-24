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
Usage:       extract_images.py PDF OUT
             extract_images.py --pdf PDF --out OUT
```

Example Usage:

```bash
python extract_images.py --pdf sample.pdf --out sample_out extract
```

You can see more help with:
`python extract_images.py -- --help`
