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
title = "Scrollbar 測試"
window.title(title)

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

frame1 = tk.Frame(window)
frame1.pack()
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
text = tk.Text(frame1, width = 40, height = 10, wrap = tk.WORD, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()
