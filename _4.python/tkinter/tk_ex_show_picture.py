# The Python Imaging Library

# tk 顯示一張圖

from tkinter import Tk, Canvas, NW

from PIL import Image, ImageTk

class PaintCanvas(Canvas):
    def __init__(self, master, im):

        Canvas.__init__(self, master, width=im.size[0], height=im.size[1])

        # fill the canvas
        self.tile = {}
        self.tilesize = tilesize = 32
        xsize, ysize = im.size
        for x in range(0, xsize, tilesize):
            for y in range(0, ysize, tilesize):
                box = x, y, min(xsize, x+tilesize), min(ysize, y+tilesize)
                tile = ImageTk.PhotoImage(im.crop(box))
                self.create_image(x, y, image=tile, anchor=NW)
                self.tile[(x, y)] = box, tile
        self.image = im

window = Tk()
filename = 'C:/______test_files2/human2.jpg'
im = Image.open(filename)
if im.mode != "RGB":
    print('圖片非RGB模式, 要轉成RGB格式')
    im = im.convert("RGB")	#轉換成RGB圖像

PaintCanvas(window, im).pack()

window.mainloop()

