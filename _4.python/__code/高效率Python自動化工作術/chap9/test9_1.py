from PIL import Image

infile = "earth.png"
savefile = "savePNG.png"

img = Image.open(infile)      #載入圖片檔
img.save(savefile, format="PNG")    #PNG轉存檔案
