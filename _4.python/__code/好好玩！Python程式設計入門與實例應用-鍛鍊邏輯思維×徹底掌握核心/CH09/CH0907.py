from tkinter import *

# step2.建立主視窗物件, 標題列顯示文字
wnd = Tk()
wnd.title('Main Window')
# 設定視窗大小
wnd.geometry('220x150+5+40')
# 設定兩個標籤
little = Label(wnd, text = 'Label: First',
        bg = 'skyblue').pack()
bigger = Label(wnd, text ='Label: Second',
        bg = 'pink').pack()
wnd.mainloop()
