import json
from pathlib import Path
from typing import List

import fire
import fitz


class Convertor(object):
    """

    """

    def __init__(self, pdf: str, out: str):
        self.document_path = pdf
        assert Path(self.document_path).exists()
        self.output_dir = Path(out)
        if not self.output_dir.exists():
            self.output_dir.mkdir(exist_ok=True)

    def extract(self) -> List[str]:
        """
        This function convert pdf pages into PNG images. To convert pdf pages to png images, fitz package is used.

        Args:
            document_path (str): Path of the pdf document.

        Returns:
            List of images, path to temporary file and path to temporary directory.

        Raises:
            If any error occurs or fitz package call fails.
        """
        doc = fitz.open(self.document_path)
        image_filenames = []
        for i in range(len(doc)):
            print(f"Page {i+1} | Number of Images: {len(doc.getPageImageList(i))}")
            for img in doc.getPageImageList(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                filename = str(self.output_dir / f"page{i}-image{xref}.png")
                if pix.n < 5:  # this is GRAY or RGB
                    pix.writePNG(filename)
                    image_filenames.append(filename)
                else:  # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG(filename)
                    image_filenames.append(filename)
                    pix1 = None
                pix = None
        print(json.dumps(image_filenames, indent=2))


if __name__ == "__main__":
    fire.Fire(Convertor)
