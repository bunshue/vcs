# Python 測試 tkinter

import tkinter as tk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 600
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "測試grid"
window.title(title)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
#column 0 為基礎寬度，column 1 為column0的兩倍寬

'''
window.columnconfigure((0, 2, 3), weight=1)
window.columnconfigure(1, weight=2)
window主視窗的，column 0 , 2, 3為基礎寬度，column 1 為其他column的兩倍寬
'''

'''
rectangle_1 = tk.Button(window, text="Region 1", bg="magenta", fg="black")
rectangle_1.grid(column=0, ipadx=10, ipady=10)
rectangle_2 = tk.Button(window, text="Region 2", bg="cyan", fg="black")
rectangle_2.grid(column=1, ipadx=10, ipady=10)
'''

'''
rectangle_1 = tk.Button(window, text="Region 1", bg="magenta", fg="black")
rectangle_1.grid(column=0,row=0, ipadx=10, ipady=10)
rectangle_2 = tk.Button(window, text="Region 2", bg="cyan", fg="black")
rectangle_2.grid(column=1,row=0, ipadx=10, ipady=10)
'''

'''
參數Sticky填充元件大小
sticky 可以輸入N ,S, E, W或是 混搭例如:EW，NS，NSEW，代表靠N(北方) 、S(南方)、E(東方)、W(西方)，NS(北南延伸)，EW(東西延伸)，NSEW(全方位延伸)
'''

'''
rectangle_1 = tk.Button(window, text="Region 1", bg="magenta", fg="black")
rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10, sticky="EW")
rectangle_2 = tk.Button(window, text="Region 2", bg="cyan", fg="black")
rectangle_2.grid(column=1, row=0, ipadx=10, ipady=10, sticky="EW")
'''

rectangle_1 = tk.Button(window, text="Region 1", bg="magenta", fg="black")
rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10)
rectangle_2 = tk.Button(window, text="Region 2", bg="cyan", fg="black")
rectangle_2.grid(column=1, row=0, ipadx=10, ipady=10)



window.mainloop()


