# Python 測試 tkinter

def choose():
    str = "你喜歡的球類運動："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + ball[i] + " "
    print(str)
    msg.set(str)

import tkinter as tk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 600
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

choice = []
ball = ["足球", "籃球", "棒球"]
msg = tk.StringVar()
label1 = tk.Label(window, text="選擇喜歡的球類運動：")
label1.pack()

for i in range(0, len(ball)):
    tem = tk.IntVar()
    choice.append(tem)
    item = tk.Checkbutton(window, text=ball[i], variable=choice[i], command=choose)
    item.pack()
label2 = tk.Label(window, fg="red", textvariable=msg)
label2.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線


def checkPW():
    if(pw.get() == "1234"):
        msg.set("密碼正確，歡迎登入！")
    else:
        msg.set("密碼錯誤，請修正密碼！")

pw = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(window, text="請輸入密碼：(1234)")
label.pack()
entry = tk.Entry(window, textvariable=pw)
entry.pack()
button = tk.Button(window, text="登入", command=checkPW)
button.pack()
lblmsg = tk.Label(window, fg="red", textvariable=msg)
lblmsg.pack()


'''
import tkinter as tk
window = tk.Tk()
label1 = tk.Label(window, text="這是標籤元件！", fg="red", bg="yellow", font=("新細明體", 12), padx=20, pady=10)
label1.pack()
window.mainloop()
'''

'''

import tkinter as tk
window = tk.Tk()
text = tk.Text(window)
text.insert(tk.INSERT, "Tkinter 套件是圖形使用者介面，\n")
text.insert(tk.INSERT, "雖然功能略為陽春，\n")
text.insert(tk.INSERT, "但已足夠一般應用程式使用，\n")
text.insert(tk.INSERT, "而且是內含於 Python 系統中，\n")
text.insert(tk.END, "不需另外安裝即可使用。")
text.pack()
text.config(state=tk.DISABLED)
window.mainloop()
'''

'''
def choose():
    msg.set("你最喜歡的球類運動：" + choice.get())

import tkinter as tk

window = tk.Tk()
choice = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(window, text="選擇最喜歡的球類運動：")
label.pack()
item1 = tk.Radiobutton(window, text="足球", value="足球", variable=choice, command=choose)
item1.pack()
item2 = tk.Radiobutton(window, text="籃球", value="籃球", variable=choice, command=choose)
item2.pack()
item3 = tk.Radiobutton(window, text="棒球", value="棒球", variable=choice, command=choose)
item3.pack()
lblmsg = tk.Label(window, fg="red", textvariable=msg)
lblmsg.pack()
item1.select()
choose()
window.mainloop()
'''

'''
import tkinter as tk

window = tk.Tk()
window.geometry("300x100")
label1=tk.Label(window, text="輸入成績：")
label1.place(x=20, y=20)
score = tk.StringVar()
entryUrl = tk.Entry(window, textvariable=score)
entryUrl.place(x=90, y=20)
btnDown = tk.Button(window, text="計算成績")
btnDown.place(x=80, y=50)

window.mainloop()
'''


window.mainloop()

#window.destroy() # optional; see description below


