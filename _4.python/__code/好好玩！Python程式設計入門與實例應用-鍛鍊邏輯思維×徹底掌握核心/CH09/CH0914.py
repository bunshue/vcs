#使用pack()方法，參數side
from tkinter import *

# Tk()建構式產生主視窗物件
root = Tk()
root.title('有參數pack()方法')

# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
lbla = Label(root, text = 'Gray', bg = 'gray',
        fg = 'white').pack(side = 'right')#加入版面

lblb = Label(root, text = 'Yellow',
        bg = 'yellow', fg = 'gray').pack(
        side = 'right', padx = 5, pady = 10)

lblc = Label(root, text = 'Orange',
        bg = 'orange', fg = 'black').pack(side = 'right')

mainloop()
