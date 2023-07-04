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
title = "Label測試"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

font_size = 24
w = 40
h = 30

# 設定 Label 
label1 = tk.Label(window, text = '這是標籤元件', fg = 'red', bg = 'yellow', font = ("標楷體", font_size), padx = w, pady = h)
label1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Label測試
tk.Label(text = '有背景色的Label測試').pack()
tk.Label(window, text = '有背景色的Label 紅', bg = 'red',   width = 20).pack()
tk.Label(        text = '有背景色的Label 綠', bg = 'green', width = 30).pack()
tk.Label(window, text = '有背景色的Label 藍', bg = 'blue',  width = 20).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

print('用 Label 顯示一張圖片')
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)
image = ImageTk.PhotoImage(image)
label1 = tk.Label(image = image)
label1.image = image
#label1.grid()
label1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

