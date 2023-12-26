# ex18_8.py
from tkinter import *
    
window = Tk()
window.title("ex18_8")         # 視窗標題

sselogo = PhotoImage(file="hung.gif")
lab1 = Label(window,image=sselogo).pack(side="right")

sseText = """Python作者:洪錦魁
喜歡旅遊
曾經留學University of Mississippi和University of Kentucky"""
lab2 = Label(window,text=sseText,bg="lightyellow",
             justify=LEFT,padx=10).pack(side="left")

window.mainloop()






