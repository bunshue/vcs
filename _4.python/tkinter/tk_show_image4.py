# The Python Imaging Library

# tk 顯示一張圖

import tkinter as tk

from PIL import Image, ImageTk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)
if image.mode != "RGB":
    print('圖片非RGB模式, 要轉成RGB格式')
    image = image.convert("RGB")	#轉換成RGB圖像

width = 600
height = 600

canvas = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas.pack()

#將全圖顯示在某處
x_st = 250
y_st = 150
image2 = ImageTk.PhotoImage(image)
canvas.create_image(x_st, y_st, anchor = tk.NW, image = image2)

#將圖片的一小塊裁出顯示在某處
box = (101, 133, 201, 233)
tile = ImageTk.PhotoImage(image.crop(box))

x_st = 50
y_st = 50
canvas.create_image(x_st, y_st, image = tile, anchor = tk.NW)

window.mainloop()

