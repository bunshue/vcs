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
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Label測試"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

font1 = ("Courier", 40, "bold")

label1 = tk.Label(window, text = 'label之字型', font = font1)
label1.pack()

label2a = tk.Label(window, text = '不使用label1之字型')
label2a.pack()

label2b = tk.Label(window, text = '使用label1之字型')
label2b.pack()

font2 = label1["font"]  #將label1的字型讀出來

#label2a.config(font = font2)  #label2a 不使用
label2b.config(font = font2)   #label2b 使用

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# Label測試
tk.Label(text = '有背景色的Label測試').pack()
tk.Label(window, text = '有背景色的Label 紅', bg = 'red',   width = 20).pack()
tk.Label(        text = '有背景色的Label 綠', bg = 'green', width = 30).pack()
tk.Label(window, text = '有背景色的Label 藍', bg = 'blue',  width = 20).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

tk.Label(window, text = "Blue", bg = "blue").pack()
#tk.Label(window, text = "Red", bg = "red").pack(fill = tk.BOTH, expand = 1)
tk.Label(window, text = "Red", bg = "red").pack(fill = tk.BOTH)
tk.Label(window, text = "Green", bg = "green").pack(fill = tk.BOTH)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


tk.Label(window, text = "Blue", bg = "blue").pack(side = tk.LEFT)
#tk.Label(window, text = "Red", bg = "red").pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
tk.Label(window, text = "Red", bg = "red").pack(side = tk.LEFT, fill = tk.BOTH)
tk.Label(window, text = "Green", bg = "green").pack(side = tk.LEFT, fill = tk.BOTH)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()

