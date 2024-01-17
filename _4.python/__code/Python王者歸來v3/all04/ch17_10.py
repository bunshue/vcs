# ch17_10.py
from PIL import Image

pict = Image.open("rushmore.jpg")           # 建立Pillow物件
pict.rotate(90).save("out17_10_1.jpg")      # 旋轉90度
pict.rotate(180).save("out17_10_2.jpg")     # 旋轉180度
pict.rotate(270).save("out17_10_3.jpg")     # 旋轉270度








