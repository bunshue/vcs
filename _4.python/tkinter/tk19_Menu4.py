# 以Menu元件建置功能表
from tkinter import *
from tkinter import messagebox

# 定義回應函式
def New():
    messagebox.showinfo('新檔案',
        '檔案功能表下的開啟新檔指令')
    
def Open():
    messagebox.showinfo('開啟舊檔',
        '檔案功能表下的開啟舊檔指令')

def Save():
    messagebox.showinfo('儲存檔案',
        '檔案功能表下的儲存檔案指令')
    
def Copyright():
    messagebox.showinfo('版權宣告',
        '我的第一支含視窗功能表程式-使用Python語言撰寫')

wnd = Tk()#主視窗物件
wnd.title('GUI介面-Menu')

# 1.產生功能表物件menuBar
menuBar = Menu(wnd)

# 2.將功能表物件menuBar佈置到主視窗的頂部
wnd.config(menu = menuBar)

# 3.加入主功能表項目
menu_file = Menu(menuBar, tearoff = 0)
menu_font = Menu(menuBar, tearoff = 0)
menu_help = Menu(menuBar, tearoff = 0)

# 4. 產生主功能項目實體
menuBar.add_cascade(label = '檔案', menu = menu_file)
menuBar.add_cascade(label = '字體大小', menu = menu_font)
menuBar.add_cascade(label = '版權宣告', menu = menu_help)

# 5-1. 加入'檔案'功能表下拉選單
menu_file.add_command(label = '新檔案',
        underline = 1, accelerator = 'Ctrl+N',
        command = New)
menu_file.add_command(label = '開啟',
        underline = 1, accelerator = 'Ctrl+O',
        command = Open)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '儲存',
        underline = 1, accelerator = 'Ctrl+S',
        command = Save)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '離開',
        underline = 1, accelerator = 'Ctrl+Q',
        command = lambda : wnd.destroy())

# 5-2. 加入'字體大小'功能表下拉選單
labels = ('大', '中', '小')
for item in labels:
    menu_font.add_radiobutton(label = item)

# 5-3. 加入'版權宣告'功能表下拉選單
menu_help.add_command(label = '原創者聲明', command = Copyright)

mainloop()
