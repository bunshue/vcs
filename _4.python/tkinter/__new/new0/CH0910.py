from tkinter import *

# 呼叫Tk()建構式產生主視窗
wnd = Tk()

# 顯示主視窗標題列的文字
wnd.title('Button state...')

#Button屬性state的常數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    btn = Button(wnd, text = item, state = item)
    btn.pack()    #以元件加入主視窗
wnd.mainloop()
