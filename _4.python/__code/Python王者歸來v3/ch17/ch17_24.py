# ch17_24.py
from PIL import Image
import pytesseract

text = pytesseract.image_to_string(Image.open('d:\\Python\\ch17\\atq9305.jpg'))
print(type(text), "   ", text)

