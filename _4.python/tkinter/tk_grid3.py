'''
Grid 測試 Button
'''
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
title = "Grid 測試 Button"
window.title(title)

button00 = tk.Button(window, text = "第0排第0個", width = 20)
button00.grid(row = 0, column = 0, padx = 5, pady = 5)
button01 = tk.Button(window, text = "第0排第1個", width = 20)
button01.grid(row = 0, column = 1, padx = 5, pady = 5)
button02 = tk.Button(window, text = "第0排第2個", width = 20)
button02.grid(row = 0, column = 2, padx = 5, pady = 5)
button10 = tk.Button(window, text = "第1排第0個", width = 20)
button10.grid(row = 1, column = 0, padx = 5, pady = 5)
button11 = tk.Button(window, text = "第1排第1個", width = 20)
button11.grid(row = 1, column = 1, padx = 5, pady = 5)
button12 = tk.Button(window, text = "第1排第2個", width = 20)
button12.grid(row = 1, column = 2, padx = 5, pady = 5)

'''
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 2)
#column 0 為基礎寬度，column 1 為column0的兩倍寬
'''
'''
window.columnconfigure((0, 2, 3), weight = 1)
window.columnconfigure(1, weight = 2)
window主視窗的，column 0 , 2, 3為基礎寬度，column 1 為其他column的兩倍寬
'''

button20 = tk.Button(window, text = "第2排第0個")
button20.grid(row = 2, column = 0, ipadx = 10, ipady = 10)
button21 = tk.Button(window, text = "第2排第1個")
button21.grid(row = 2, column = 1, ipadx = 10, ipady = 10)
button22 = tk.Button(window, text = "第2排第2個")
button22.grid(row = 2, column = 2, ipadx = 10, ipady = 10)

'''
參數Sticky填充元件大小
sticky 可以輸入N ,S, E, W或是 混搭例如:EW，NS，NSEW，代表靠N(北方) 、S(南方)、E(東方)、W(西方)，NS(北南延伸)，EW(東西延伸)，NSEW(全方位延伸)
'''

button30 = tk.Button(window, text = "第3排第0個")
button30.grid(row = 3, column = 0, ipadx = 10, ipady = 10, sticky = "EW")
button31 = tk.Button(window, text = "第3排第1個")
button31.grid(row = 3, column = 1, ipadx = 10, ipady = 10, sticky = "EW")
button32 = tk.Button(window, text = "第3排第2個")
button32.grid(row = 3, column = 2, ipadx = 10, ipady = 10, sticky = "EW")

window.mainloop()
