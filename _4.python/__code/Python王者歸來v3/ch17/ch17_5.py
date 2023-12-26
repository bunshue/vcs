# ch17_5.py
from PIL import Image

rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
print("列出物件副檔名 : ", rushMore.format)
print("列出物件描述   : ", rushMore.format_description)



