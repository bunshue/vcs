# ch18_32.py
from tkinter import *
    
window = Tk()
window.title("ch18_32")         # 視窗標題

sselogo = PhotoImage(file="sse.gif")
lab1 = Label(window,image=sselogo).pack(side="right")

sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
lab2 = Label(window,text=sseText,bg="lightyellow",
             justify=LEFT,padx=10).pack(side="left")

window.mainloop()






