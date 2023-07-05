'''
使用 canvas 顯示圖片
'''
import tkinter as tk

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
title = 'Display Image'
window.title(title)

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival.gif'

photo = tk.PhotoImage(file = filename)
tk.Label(window, text = "Blue", image = photo, bg = "gray").pack(fill = tk.BOTH, expand = 1)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/dragon-boat-festival.gif'
caImage = tk.PhotoImage(file = filename)

x = 90
y = 50
width = 400
height = 200

canvas = tk.Canvas(window, width = width, height = height)
canvas.pack()
canvas.create_image(x, y, image = caImage)

window.mainloop()
