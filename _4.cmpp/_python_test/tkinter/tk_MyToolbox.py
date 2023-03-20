def execute_command():
    print('execute_command')
    #回傳結果
    show_mesg.set("執行命令 : \n")

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

# 設定 Label
label3 = tk.Label(window, textvariable=show_mesg, foreground="red", font=("標楷體", font_size), padx = w, pady = h)
label3.pack()


window.mainloop()




