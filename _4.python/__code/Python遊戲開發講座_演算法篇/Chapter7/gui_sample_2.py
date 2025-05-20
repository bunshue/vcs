import tkinter

def btn1_on():
    en.insert(tkinter.END, "按下按鈕了")

def btn2_on():
    en.delete(0, tkinter.END)

def btn3_on():
    b3["text"] = en.get()

root = tkinter.Tk()
root.geometry("400x200")
root.title("GUI的主要元件 -2-")
en = tkinter.Entry(width=40)
en.place(x=20, y=10)
b1 = tkinter.Button(text="插入字串", command=btn1_on)
b1.place(x=20, y=60, width=160, height=40)
b2 = tkinter.Button(text="刪除字串", command=btn2_on)
b2.place(x=220, y=60, width=160, height=40)
b3 = tkinter.Button(text="取得字串", command=btn3_on)
b3.place(x=20, y=120, width=360, height=40)
root.mainloop()
