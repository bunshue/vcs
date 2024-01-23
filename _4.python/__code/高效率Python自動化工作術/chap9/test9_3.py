from PIL import Image

infile = "earthH.png"
savefile = "resize.png"

max_size = 100
img = Image.open(infile)
ratio = max_size / max(img.size)    #根據長寬較長的一邊決定縮放比率
w = int(img.width * ratio)
h = int(img.height * ratio)
img = img.resize((w, h), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")
