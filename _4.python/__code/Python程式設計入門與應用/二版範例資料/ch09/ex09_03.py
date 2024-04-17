# Filename: ex09_03.py
def cal():
    textvar.set("計算完成")    
import tkinter as tk
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
textvar=tk.StringVar()
pButton1 = tk.Button(win, textvariable=textvar, command=cal, padx=20, pady=10)
textvar.set("開始計算")
pButton1.pack()
win.mainloop()