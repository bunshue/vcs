import tkinter as tk

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


print('用Frame做一個toolbar')
toolbar = tk.Frame(window, relief = "raised", borderwidth = 1)
toolbar.pack(side = "top",fill = "x", padx = 2, pady = 1)

button1 = tk.Button(toolbar, text = "Function 1")
button1.pack(side = "left", pady = 2)
button2 = tk.Button (toolbar, text = "Function 2")
button2.pack(side = "left", pady = 2)
button3 = tk.Button(toolbar, text = "Function 3")
button3.pack(side = "left", pady = 2)
button4 = tk.Button (toolbar, text = "Function 4")
button4.pack(side = "left", pady = 2)
button5 = tk.Button(toolbar, text = "Function 5")
button5.pack(side = "left", pady = 2)
button6 = tk.Button (toolbar, text = "Function 6")
button6.pack(side = "left", pady = 2)



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()

