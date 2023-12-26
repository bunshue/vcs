# ch17_3.py
from PIL import Image

rushMore = Image.open("rushmore.jpg")       # 建立Pillow物件
print("列出物件型態 : ", type(rushMore))
width, height = rushMore.size               # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)



