# ch17_15.py
from PIL import Image

pict = Image.open("rushmore.jpg")           # 建立Pillow物件
cropPict = pict.crop((80, 30, 150, 100))   # 裁切區間
cropPict.save("out17_15.jpg")





