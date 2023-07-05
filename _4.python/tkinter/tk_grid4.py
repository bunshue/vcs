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
title = "Grid 測試"
window.title(title)

message = tk.Message(window, text = "這個訊息所佔的位置為3R2C")
message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
tk.Label(window, text = "姓 : ").grid(row = 1, column = 3)
tk.Entry(window).grid(row = 1, column = 4, padx = 5, pady = 5)
tk.Label(window, text = "名 : ").grid(row = 2, column = 3)
tk.Entry(window).grid(row = 2, column = 4)
tk.Button(window, text = "取得姓名").grid(row = 3, padx = 5, pady = 5, column = 4, sticky = tk.E)

window.mainloop()

