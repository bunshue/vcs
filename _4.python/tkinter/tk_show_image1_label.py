'''
使用 label 顯示圖片
'''

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
title = "使用 label 顯示圖片"
window.title(title)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

im = Image.open(filename)

'''
#case 1 bitmap image
# bitmap image
image = ImageTk.BitmapImage(im, foreground = "white")
tk.Label(window, image = image, bg = "blue", bd = 0).pack()
'''

#case 2 picture image
# photo image
image = ImageTk.PhotoImage(im)

label1 = tk.Label(window, text = '多人圖片', image = image, bd = 20, bg = 'red')
label1.pack()
#tk.Label(window, text = '多人圖片', image = image, bd = 0, bg = 'red', width = 1200).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print('用 Label 顯示一張圖片')
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image2 = Image.open(filename)
image2 = ImageTk.PhotoImage(image2)
label2 = tk.Label(image = image2)
label2.image = image
label2.pack()

window.mainloop()




