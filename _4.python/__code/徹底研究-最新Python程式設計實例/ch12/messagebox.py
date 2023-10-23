from tkinter import *
from tkinter import messagebox
wnd = Tk()
wnd.title('訊息方塊元件(messagebox)')
wnd.geometry('180x120+20+50')

def answer():
    messagebox.showerror('顯示類訊息框',
            '這是messagebox.showerror的訊息框')

def callback():
    messagebox.askyesno('詢問類訊息框', 
            '這是messagebox.askyesno的訊息框')

Button(wnd, text='顯示詢問訊息框的外觀', command =
       callback).pack(side = 'left', padx = 10)
Button(wnd, text='顯示錯誤訊息框的外觀', command =
       answer).pack(side = 'left')
mainloop()
