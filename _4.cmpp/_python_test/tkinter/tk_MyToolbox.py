mmm = 'abcd'

def execute_command():
    print('execute_command')
    #回傳結果
    show_mesg.set("執行命令 : \n")

def set_data():
    print('set_data')
    #回傳結果
    mesg = text1.get("1.0","end")
    mesg= mesg + mmm
    #show_mesg.set(mesg)
    print(mesg)
    text1.insert ('end', mesg)

def clear():
    show_mesg.set('')
    text1.delete(1.0,'end')
    # 執行 clear 函式時，清空內容


import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "MyToolbox"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

#root.iconbitmap('heart_green.ico')

show_mesg = tk.StringVar()

font_size = 24
w = 40
h = 30

# 設定 Label 
label1 = tk.Label(window, text="開啟程式", foreground="red", font=("標楷體", font_size), padx = w, pady = h)
label1.pack()

# 設定 Button
button1 = tk.Button(window, text="imsLink", foreground="blue", font=("標楷體", font_size), padx = w, pady = h, command = execute_command)
button1.pack()
button2 = tk.Button(window, text="imsCap", foreground="blue", font=("標楷體", font_size), padx = w, pady = h, command = execute_command)
button2.pack()
button3 = tk.Button(window, text="imsFlash", foreground="blue", font=("標楷體", font_size), padx = w, pady = h, command = execute_command)
button3.pack()

#像是richTextBox
text1 = tk.Text(window, height=10)  # 放入多行輸入框
text1.pack()

bt_set_data = tk.Button(window,text='set data', command=set_data)  # 放入清空按鈕
bt_set_data.pack()
bt_clear = tk.Button(window,text='clear', command=clear)  # 放入清空按鈕
bt_clear.pack()


# 設定 Label
label3 = tk.Label(window, textvariable=show_mesg, foreground="red", font=("標楷體", font_size), padx = w, pady = h)
label3.pack()


window.mainloop()

