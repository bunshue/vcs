# ch17_18.py
from PIL import Image

pict = Image.open("rushmore.jpg")               # 建立Pillow物件
copyPict = pict.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
cropWidth, cropHeight = cropPict.size           # 獲得裁切區間的寬與高

width, height = 600, 320                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
        newImage.paste(cropPict, (x, y))        # 合成

newImage.save("out17_18.jpg")                   # 儲存









