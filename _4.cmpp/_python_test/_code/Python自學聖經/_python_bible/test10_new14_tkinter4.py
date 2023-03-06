# Python 新進測試 14  tkinter



'''
import tkinter as tk
win = tk.Tk()
label1 = tk.Label(win, text="這是標籤元件！", fg="red", bg="yellow", font=("新細明體", 12), padx=20, pady=10)
label1.pack()
win.mainloop()
'''

'''
import tkinter as tk
win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.grid(row=0, column=1, padx=5, pady=5, columnspan=2,sticky="e")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.grid(row=0, column=3, padx=5, pady=5)
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = tk.Button(win, text="這是按鈕五", width=20)
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = tk.Button(win, text="這是按鈕六", width=20)
button6.grid(row=1, column=2, padx=5, pady=5)
win.mainloop()
'''

'''
import tkinter as tk
win = tk.Tk()
text = tk.Text(win)
text.insert(tk.INSERT, "Tkinter 套件是圖形使用者介面，\n")
text.insert(tk.INSERT, "雖然功能略為陽春，\n")
text.insert(tk.INSERT, "但已足夠一般應用程式使用，\n")
text.insert(tk.INSERT, "而且是內含於 Python 系統中，\n")
text.insert(tk.END, "不需另外安裝即可使用。")
text.pack()
text.config(state=tk.DISABLED)
win.mainloop()
'''

'''
def choose():
    msg.set("你最喜歡的球類運動：" + choice.get())

import tkinter as tk

win = tk.Tk()
choice = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="選擇最喜歡的球類運動：")
label.pack()
item1 = tk.Radiobutton(win, text="足球", value="足球", variable=choice, command=choose)
item1.pack()
item2 = tk.Radiobutton(win, text="籃球", value="籃球", variable=choice, command=choose)
item2.pack()
item3 = tk.Radiobutton(win, text="棒球", value="棒球", variable=choice, command=choose)
item3.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
item1.select()
choose()
win.mainloop()
'''

'''

import tkinter as tk
win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = tk.Button(win, text="這是按鈕五", width=20)
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = tk.Button(win, text="這是按鈕六", width=20)
button6.grid(row=1, column=2, padx=5, pady=5)
win.mainloop()
'''


'''
import tkinter as tk
win = tk.Tk()
win.geometry("300x100")
label1=tk.Label(win, text="輸入成績：")
label1.place(x=20, y=20)
score = tk.StringVar()
entryUrl = tk.Entry(win, textvariable=score)
entryUrl.place(x=90, y=20)
btnDown = tk.Button(win, text="計算成績")
btnDown.place(x=80, y=50)
win.mainloop()
'''

'''
import tkinter as tk
win = tk.Tk()
win.geometry("400x150")
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.place(relx=0.5, rely=0.5, anchor="center")
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.place(relx=0.1, rely=0.1, anchor="nw")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.place(relx=0.1, rely=0.8, anchor="w")
win.mainloop()
'''

'''
import tkinter as tk
win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack()
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack()
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack()
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack()
win.mainloop()
'''

'''
import tkinter as tk
win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack(padx=20, pady=5)
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack(padx=20, pady=5)
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack(padx=20, pady=5)
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack(padx=20, pady=5)
win.mainloop()
'''

'''
import tkinter as tk
win = tk.Tk()
button1 = tk.Button(win, text="這是按鈕一", width=20)
button1.pack(padx=20, pady=5, side="right")
button2 = tk.Button(win, text="這是按鈕二", width=20)
button2.pack(padx=20, pady=5, side="left")
button3 = tk.Button(win, text="這是按鈕三", width=20)
button3.pack(padx=20, pady=5, side="bottom")
button4 = tk.Button(win, text="這是按鈕四", width=20)
button4.pack(padx=20, pady=5)
win.mainloop()
'''



def checkPW():
    if(pw.get() == "1234"):
        msg.set("密碼正確，歡迎登入！")
    else:
        msg.set("密碼錯誤，請修正密碼！")

import tkinter as tk

win = tk.Tk()
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
win.mainloop()





