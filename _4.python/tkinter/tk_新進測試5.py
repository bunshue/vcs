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
title = "Toolbox 測試"
window.title(title)

print('Toolbox 測試')
tk.Button(window, text = "OK").pack(side = tk.LEFT)
tk.Button(window, text = "Cancel").pack(side = tk.LEFT)
tk.Label(window, text = "Enter your name:").pack(side = tk.LEFT)
tk.Entry(window, text = "Type Name").pack(side = tk.LEFT)
tk.Checkbutton(window, text = "Bold").pack(side = tk.LEFT)
tk.Checkbutton(window, text = "Italic").pack(side = tk.LEFT)
tk.Radiobutton(window, text = "Red").pack(side = tk.LEFT)
tk.Radiobutton(window, text = "Yellow").pack(side = tk.LEFT)

#label的寫法
label3 = tk.Label(text = 'Created by Harsh Bardhan Mishra', font = ('Times', 22), fg = 'brown')
label3.pack()


window.mainloop()
