# The Python Imaging Viewer

import tkinter as tk
from PIL import Image, ImageTk

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

window = tk.Tk()

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

im = Image.open(filename)

'''
#case 1 bitmap image
# bitmap image
self_image = ImageTk.BitmapImage(im, foreground="white")
tk.Label(window, image=self_image, bg="blue", bd=0).pack()
'''

#case 2 picture image
# photo image
self_image = ImageTk.PhotoImage(im)

tk.Label(window, text='多人圖片', image=self_image, bd=50, bg='red').pack()
#tk.Label(window, text='多人圖片', image=self_image, bd=0, bg='red',   width=1200).pack()

window.mainloop()




