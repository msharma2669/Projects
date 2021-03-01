from wand.image import Image as wi

def pdfimgconvert():
    pdffilepath = "Offer.pdf"
    PDFfile = wi(filename=pdffilepath, resolution=400)

    Images = PDFfile.convert('jpg')
    ImageSequence = 1
    for img in PDFfile.sequence:
        Image = wi(image=img)
        Image.save(filename="PDFImg/Image" + str(ImageSequence) + ".jpg")
        ImageSequence += 1



