# Filename: ex09_06.py
def checkpw():
    pmsg.set("輸入的密碼:"+ppw.get())
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
ppw = tk.StringVar()
pmsg = tk.StringVar()
pLabel = tk.Label(win, text="請輸入密碼:")
pLabel.pack(padx=20, pady=5)
pEntry = tk.Entry(win, textvariable=ppw)
pEntry.pack(padx=20, pady=5)
pButton = tk.Button(win, text="登入", command=checkpw)
pButton.pack(padx=20, pady=5)
pLabmsg = tk.Label(win, textvariable=pmsg)
pLabmsg.pack(padx=20, pady=5)
win.mainloop()