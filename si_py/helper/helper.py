from PIL import Image
import pytesseract

def tesseract_ocr(scannedFile):
    text = pytesseract.image_to_string(Image.open(scannedFile))
    return text

def handle_uploaded_file(f):
    text = tesseract_ocr(f)
    return text