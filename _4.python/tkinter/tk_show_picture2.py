# The Python Imaging Library

# tk 顯示一張圖

from tkinter import Tk, Canvas, NW

from PIL import Image, ImageTk

class PaintCanvas(Canvas):
    def __init__(self, master, image):

        Canvas.__init__(self, master, width=image.size[0], height=image.size[1])

        # fill the canvas
        self.tile = {}
        self.tilesize = tilesize = 32
        xsize, ysize = image.size
        for x in range(0, xsize, tilesize):
            for y in range(0, ysize, tilesize):
                box = x, y, min(xsize, x + tilesize), min(ysize, y + tilesize)
                tile = ImageTk.PhotoImage(image.crop(box))
                self.create_image(x, y, image = tile, anchor = NW)
                self.tile[(x, y)] = box, tile
        self.image = image

window = Tk()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)
if image.mode != "RGB":
    print('圖片非RGB模式, 要轉成RGB格式')
    image = image.convert("RGB")	#轉換成RGB圖像

PaintCanvas(window, image).pack()

window.mainloop()

