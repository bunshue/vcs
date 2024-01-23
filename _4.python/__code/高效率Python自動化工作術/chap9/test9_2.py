from PIL import Image

infile = "earth.png"
savefile = "resize.png"

img = Image.open(infile)
img = img.resize((100, 100), Image.LANCZOS)     #調整大小
img.save(savefile, format="PNG")
