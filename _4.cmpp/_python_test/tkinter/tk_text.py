mmm = 'abcd'

def set_data():
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + mmm
    print(mesg)
    text1.insert ('end', mesg)

def clear():
    text1.delete(1.0,'end')
    # 執行 clear 函式時，清空內容

import tkinter as tk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "Text測試"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

filename = 'C:/______test_files/_icon/DrAP.ico'
window.iconbitmap(filename) #設定icon

#像是richTextBox
text1 = tk.Text(window, height = 10)  # 放入多行輸入框
text1.pack()

bt_set_data = tk.Button(window,text='set data', command=set_data)  # 放入清空按鈕
bt_set_data.pack()
bt_clear = tk.Button(window,text='clear', command=clear)  # 放入清空按鈕
bt_clear.pack()

window.mainloop()
