# ch17_26.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('d:\\Python\\ch17\\data17_26.jpg'),
                                    lang='chi_tra')
print(text)
with open('d:\\Python\\ch17\\out17_26.txt', 'w') as fn:
    fn.write(text)


