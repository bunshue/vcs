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
tk.Label(text = '有背景色的Label測試', font = "Raleway").pack()
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

#前後移動控件
label1 = tk.Label(window, text = 'Label 1', background = 'red')
label2 = tk.Label(window, text = 'Label 2', background = 'green')
label3 = tk.Label(window, text = 'Label 3', background = 'blue')

#有寬高的Label
x_st = 40
y_st = 180
dd = 20
label1.place(x = x_st + dd * 0, y = y_st + dd * 0, width = 100, height = 100)
label2.place(x = x_st + dd * 1, y = y_st + dd * 1, width = 100, height = 100)
label3.place(x = x_st + dd * 2, y = y_st + dd * 2, width = 100, height = 100)

button1 = tk.Button(window, text = 'Label 1 (R) 向上移動', command = lambda: label1.lift(aboveThis = label2))
button2 = tk.Button(window, text = 'Label 2 (G) 向上移動', command = lambda: label2.tkraise())
button3 = tk.Button(window, text = 'Label 1 (B) 向上移動', command = lambda: label3.tkraise())

# label1.lift()
# label2.lower()

'''
button1.place(rely = 1, relx = 0.8, anchor = 'se')
button2.place(rely = 1, relx = 1, anchor = 'se')
button3.place(rely = 1, relx = 0.6, anchor = 'se')
'''
button1.pack()
button2.pack()
button3.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


tk.Label(window, text = "Blue", bg = "blue").pack(side = tk.LEFT)
#tk.Label(window, text = "Red", bg = "red").pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
tk.Label(window, text = "Red", bg = "red").pack(side = tk.LEFT, fill = tk.BOTH)
tk.Label(window, text = "Green", bg = "green").pack(side = tk.LEFT, fill = tk.BOTH)


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()

