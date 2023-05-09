import tkinter as tk
from PIL import Image, ImageTk

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
title = 'tk顯示一張圖片'
window.title(title)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

pic = Image.open(filename)
pic = ImageTk.PhotoImage(pic)
label1 = tk.Label(image = pic)
label1.image = pic
label1.grid()

window.mainloop()

