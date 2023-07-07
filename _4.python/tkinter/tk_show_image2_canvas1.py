'''
使用 canvas 顯示圖片 全部 與 部分
'''
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = '使用 canvas 顯示圖片 全部 與 部分'
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

width = 700
height = 700
canvas = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas.pack()

#create_image 繪製影像
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/train.gif'

img1 = Image.open(filename)
img2 = ImageTk.PhotoImage(img1)
#img2 = tk.PhotoImage(file = filename)   #gif專用

x_st = 0
y_st = 0
canvas.create_image(x_st, y_st, anchor = tk.NW, image = img2)




filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)
if image.mode != "RGB":
    print('圖片非RGB模式, 要轉成RGB格式')
    image = image.convert("RGB")	#轉換成RGB圖像

x_st = 50
y_st = 50
w = 100
h = 100
box = x_st, y_st, x_st + w, y_st + h

tile = ImageTk.PhotoImage(image.crop(box))
x = 350
y = 100

canvas.create_image(x, y, image = tile, anchor = tk.NW)


#將圖片的一小塊裁出顯示在某處
box = (101, 133, 201, 233)
tile2 = ImageTk.PhotoImage(image.crop(box))

x_st = 50
y_st = 450
canvas.create_image(x_st, y_st, image = tile2, anchor = tk.NW)

'''
self.bitmap = c.create_bitmap(width//2, height//2,
                bitmap=bitmap,
                foreground='blue')
'''


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)
if image.mode != "RGB":
    print('圖片非RGB模式, 要轉成RGB格式')
    image = image.convert("RGB")	#轉換成RGB圖像

#將全圖顯示在某處
x_st = 250
y_st = 250
image2 = ImageTk.PhotoImage(image)
canvas.create_image(x_st, y_st, anchor = tk.NW, image = image2)



window.mainloop()
