from PIL import Image

infile = "earth.png"
savefile = "tmp_savePNG1.png"

img = Image.open(infile)      #載入圖片檔
img.save(savefile, format="PNG")    #PNG轉存檔案




#檔案 : C:\_git\vcs\_4.python\__code\高效率Python自動化工作術\chap9\test9_2.py

from PIL import Image

infile = "earth.png"
savefile = "tmp_resize2.png"

img = Image.open(infile)
img = img.resize((100, 100), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\高效率Python自動化工作術\chap9\test9_3.py

from PIL import Image

infile = "earthH.png"
savefile = "tmp_resize1.png"

max_size = 100
img = Image.open(infile)
ratio = max_size / max(img.size)    #根據長寬較長的一邊決定縮放比率
w = int(img.width * ratio)
h = int(img.height * ratio)
img = img.resize((w, h), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\高效率Python自動化工作術\chap9\test9_4.py

from PIL import Image
from PIL import ImageDraw

infile = "earth.png"
savefile = "tmp_redline.png"

img = Image.open(infile)
draw = ImageDraw.Draw(img)  #在圖片畫線的準備
draw.line((0, 0, img.width, img.height), fill="RED", width=8) #畫線
img.save(savefile, format="PNG")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\高效率Python自動化工作術\chap9\test9_5.py

from PIL import Image

infile = "earth.png"
savefile = "tmp_saveJPG2.jpg"

img = Image.open(infile)
if img.format == "PNG":
    newimg = Image.new("RGB", img.size, "WHITE")
    newimg.paste(img, mask=img)             # 將PNG檔壓在白底圖片上
    newimg.save(savefile, format="JPEG")    # JPG轉存檔案
elif img.format == "JPEG":
    img.save(savefile, format="JPEG")       # JPG轉存檔案

print("------------------------------------------------------------")  # 60個


