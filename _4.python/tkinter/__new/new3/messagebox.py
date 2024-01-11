from tkinter import *
from tkinter import messagebox
wnd = Tk()
wnd.title('訊息方塊元件(messagebox)')
wnd.geometry('180x120+20+50')

def first():
    messagebox.showinfo('顯示類對話方塊',
            '「顯示」類是以「show」開頭，只會顯示一個「確定」鈕。')

def second():
    messagebox.askretrycancel('詢問類對話方塊', 
            '「詢問」類是以「ask」為開頭，伴隨2~3個按鈕來產生互動。')

Button(wnd, text='顯示類對話方塊', command =
       first).pack(side = 'left', padx = 10)
Button(wnd, text='詢問類對話方塊', command =
       second).pack(side = 'left')
mainloop()
