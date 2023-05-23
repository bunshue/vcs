def checkPW():
    if(pw.get() == "1234"):
        msg.set("密碼正確，歡迎登入！")
    else:
        msg.set("密碼錯誤，請修正密碼！")

import tkinter as tk

win = tk.Tk()

win.geometry("800x600")

label1=tk.Label(win, text="輸入成績：")
label1.place(x=20, y=20)
score = tk.StringVar()
entryUrl = tk.Entry(win, textvariable=score)
entryUrl.place(x=90, y=20)
btnDown = tk.Button(win, text="計算成績")
btnDown.place(x=80, y=50)





pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="請輸入密碼：")
label.pack()
entry = tk.Entry(win, textvariable=pw)
entry.pack()
button = tk.Button(win, text="登入", command=checkPW)
button.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()



button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack(padx=20, pady=5, side="right")
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack(padx=20, pady=5, side="left")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack(padx=20, pady=5, side="bottom")
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack(padx=20, pady=5)


button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack(padx=20, pady=5)
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack(padx=20, pady=5)
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack(padx=20, pady=5)
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack(padx=20, pady=5)



button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack()
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack()
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack()
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack()

win.mainloop()


