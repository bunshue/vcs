from PIL import Image, ImageDraw
im = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(im)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
im.show()
