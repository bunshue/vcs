# ch3_33.py
from tkinter import *

window = Tk()
window.title("ch3_33")              # 視窗標題
lab1 = Label(window,text="明志工專",relief="raised")
lab2 = Label(window,bg="yellow",width=20)
lab3 = Label(window,text="明志科技大學",relief="raised")
lab4 = Label(window,bg="aqua",width=20)
lab1.grid(row=0,column=0,padx=5,pady=5)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,padx=5)
lab4.grid(row=1,column=1,padx=5)

window.mainloop()






