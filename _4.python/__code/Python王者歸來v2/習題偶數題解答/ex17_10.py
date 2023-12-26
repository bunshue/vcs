# ex17_10.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('d:\\Python\\ex\\data17_10.jpg'),
                                               lang='chi_sim')
print(text)
with open('d:\\Python\\ex\\out17_10.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)


