import tkinter

def btn_on():
    la["bg"] = "magenta"
    la["text"] = "按下按鈕了"

root = tkinter.Tk()
root.geometry("300x200")
root.title("GUI的主要元件 -1-")
root["bg"]="black"
la = tkinter.Label(text="這是稱為標籤的元件", bg="cyan")
la.place(x=10, y=10)
bu = tkinter.Button(text="按鈕", command=btn_on)
bu.place(x=10, y=60, width=100, height=40)
root.mainloop()
