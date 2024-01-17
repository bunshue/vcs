# ch17_27.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('d:\\Python\\ch17\\data17_27.jpg'),
                                               lang='chi_sim')
print(text)
with open('d:\\Python\\ch17\\out17_27.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)


