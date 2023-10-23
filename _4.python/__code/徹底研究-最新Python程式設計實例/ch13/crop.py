from PIL import Image
with Image.open("images/elephant.jpg") as im:
    print(im.size)
    x = 1000
    y = 0
    x1 = 2100
    y1 = 1600
    new_im = im.crop((x, y, x1, y1))
    print(new_im.size)
    new_im.save( "images/elephant _crop.jpg")
