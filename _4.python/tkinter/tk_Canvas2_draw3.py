import tkinter as tk
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 900
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

#create_image 繪製影像
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/train.gif'

img1 = Image.open(filename)
img2 = ImageTk.PhotoImage(img1)
#img2 = tk.PhotoImage(file = filename)   #gif專用

canvas = tk.Canvas(window, width = img1.size[0], height = img1.size[1])
canvas.pack()

x_st = 0
y_st = 0
canvas.create_image(x_st, y_st, anchor = tk.NW, image = img2)



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()




