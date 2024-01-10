def bless():
     btnvar.set("心想事成，天天開心")

def changecolor():
     btn2.config(bg = "blue")  

import tkinter as tk
win = tk.Tk()
win.title("按鈕元件(Button)功能示範")
    
btnvar = tk.StringVar() 
btn1 = tk.Button(win, textvariable=btnvar, command=bless)
btnvar.set("按下我會有祝賀語")
btn1.pack(padx=20, pady=10)

btn2 = tk.Button(win, text="按我會改變按鈕背景色", command=changecolor)
btn2.pack(padx=20, pady=10)

win.mainloop()
