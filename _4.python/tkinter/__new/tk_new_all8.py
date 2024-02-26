from tkinter import *

window = Tk() #建立主視窗物件

"""
# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
lbla = Label(window, text = 'Gray', bg = 'gray',
        fg = 'white').pack(side = 'right')#加入版面

lblb = Label(window, text = 'Yellow',
        bg = 'yellow', fg = 'gray').pack(
        side = 'right', padx = 5, pady = 10)

lblc = Label(window, text = 'Orange',
        bg = 'orange', fg = 'black').pack(side = 'right')

mainloop()
"""

photo = PhotoImage(file = '001.png')#建立圖片

#標籤 - bg 設背景色
t1 = Label(window, text = 'Hello\n Python', bg = '#78A', 
    fg = '#FF0', relief = 'groove', bd = 2, 
    width = 15, height = 3, justify = 'right')

t2 = Label(window, text = '世界', width = 6, height = 3,
    relief = RIDGE, bg = 'pink', font = ('標楷體', 16))

#在第3個標籤載入圖片
t3 = Label(window, image = photo, relief = 'sunken',
    bd = 5, width = 180, height = 150)

t1.grid(row = 0, column = 0)
t2.grid(row = 0, column = 1)
t3.grid(columnspan = 2)

mainloop()
