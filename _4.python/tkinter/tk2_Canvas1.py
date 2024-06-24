import sys

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
# size = str(w)+'x'+str(h)
# size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
# print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

tk.Label(text="Canvas 測試").pack()

color = "#FF0000"
canvas = tk.Canvas(window, width=500, height=150, bg=color)
canvas.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


def changeCanvasBgColor():
    red = 255
    green = 128
    blue = 0
    color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=color)


def drawCanvas():
    print("draw")
    x_st = 0
    y_st = 0
    radius = 50
    for i in range(0, 10):
        canvas.create_oval(
            x_st + 50 * i, y_st, x_st + 50 * i + radius, y_st + radius, tags="oval"
        )
        canvas.create_oval(
            x_st + 50 * i, y_st + 75, x_st + 50 * i + radius, y_st + 75 + radius
        )


def deleteCanvas():
    print("delete")
    canvas.delete("oval")
    canvas.delete("rect", "oval", "line")


button1 = tk.Button(window, text="改變Canvas背景色", command=changeCanvasBgColor)
button1.pack()

button2 = tk.Button(window, text="在 Canvas 上畫一些東西", command=drawCanvas)
button2.pack()

button3 = tk.Button(window, text="刪除 Canvas 上畫的部分東西", command=deleteCanvas)
button3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

window.mainloop()


print("------------------------------------------------------------")  # 60個

"""
使用 canvas 顯示圖片 gif
"""
import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
# size = str(W) + 'x' + str(H)
# size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = "Display Image"
window.title(title)

filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival.gif"

photo = tk.PhotoImage(file=filename)
tk.Label(window, text="Blue", image=photo, bg="gray").pack(fill=tk.BOTH, expand=1)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival.gif"
caImage = tk.PhotoImage(file=filename)

x = 90
y = 50
width = 400
height = 200

canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()
canvas.create_image(x, y, image=caImage)

window.mainloop()


print("------------------------------------------------------------")  # 60個


"""
使用 canvas 顯示圖片 全部 與 部分 jpg
"""
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
# size = str(W) + 'x' + str(H)
# size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = "使用 canvas 顯示圖片 全部 與 部分"
window.title(title)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

width = 700
height = 700
canvas = tk.Canvas(window, bg="pink", width=width, height=height)
canvas.pack()

# create_image 繪製影像
filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/train.gif'

image1 = Image.open(filename)
image2 = ImageTk.PhotoImage(image1)
# image2 = tk.PhotoImage(file = filename)   #gif專用

# 將全圖顯示在某處1
x_st = 0
y_st = 0
canvas.create_image(x_st, y_st, anchor=tk.NW, image=image2)


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

image3 = Image.open(filename)
if image3.mode != "RGB":
    print("圖片非RGB模式, 要轉成RGB格式")
    image3 = image3.convert("RGB")  # 轉換成RGB圖像
image4 = ImageTk.PhotoImage(image3)

# 將全圖顯示在某處2
x_st = 250
y_st = 250
canvas.create_image(x_st, y_st, anchor=tk.NW, image=image4)

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

image = Image.open(filename)
if image.mode != "RGB":
    print("圖片非RGB模式, 要轉成RGB格式")
    image = image.convert("RGB")  # 轉換成RGB圖像

x_st = 50
y_st = 50
w = 100
h = 100
box = x_st, y_st, x_st + w, y_st + h

tile = ImageTk.PhotoImage(image.crop(box))
x = 350
y = 100

canvas.create_image(x, y, image=tile, anchor=tk.NW)


# 將圖片的一小塊裁出顯示在某處
box = (101, 133, 201, 233)
tile2 = ImageTk.PhotoImage(image.crop(box))

x_st = 50
y_st = 450
canvas.create_image(x_st, y_st, image=tile2, anchor=tk.NW)

"""
self.bitmap = c.create_bitmap(width//2, height//2,
                bitmap=bitmap,
                foreground='blue')
"""

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
