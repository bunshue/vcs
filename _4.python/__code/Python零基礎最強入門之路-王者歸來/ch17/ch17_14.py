# ch17_14.py
from PIL import Image
from PIL import ImageColor

newImage = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):                                # x軸區間在50-250
    for y in range(50, 151):                            # y軸區間在50-150
        newImage.putpixel((x, y), (0, 255, 255, 255))   # 填青色
newImage.save("out17_14_1.png")                         # 第一階段存檔
for x in range(50, 251):                                # x軸區間在50-250            
    for y in range(151, 251):                           # y軸區間在151-250
        newImage.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))
newImage.save("out17_14_2.png")                         # 第一階段存檔

















