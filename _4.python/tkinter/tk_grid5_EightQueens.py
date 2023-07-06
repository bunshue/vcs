'''
Grid 測試 Label
'''
import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
#window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Grid 測試"
window.title(title)

SIZE = 8

image = tk.PhotoImage(file = "image/queen.gif")
for i in range(SIZE):
    for j in range(SIZE):
        if i == j:
            tk.Label(window, image = image).grid(row = i, column = j)
        else:
            tk.Label(window, width = 5, height = 2, bg = "red").grid(row = i, column = j)
        
window.mainloop()

