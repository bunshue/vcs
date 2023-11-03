from PIL import Image
with Image.open("images/view.jpg") as im:
    print(im.size)
    w=200
    r = w/im.size[0]
    h = int(im.size[1]*r) #依縮放比例計算高度
    new_im = im.resize((w, h))
    print(new_im.size)
    new_im.save( "images/view_resize.jpg" )
