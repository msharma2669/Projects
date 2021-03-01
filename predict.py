import tesserocr
from PIL import Image
import PDFToImage
import glob

class ocr:
    def __init__(self, filename):
        self.filename = filename

    def getPrediction(self):
        image = Image.open(self.filename)
        lines = tesserocr.image_to_text(image)  # print ocr text from image
        #for line in lines.split("\r"):
         #   print(line)
        return lines

PDFToImage.pdfimgconvert()

for imgfile in glob.glob('PDFImg/*'):
    print(imgfile)
    ocr1 = ocr(imgfile)
    print(ocr1.getPrediction())
