# ch4_10.py
from tkinter import *

root = Tk()
root.title("ch4_10")                                # 視窗標題
lab  = Label(root,text="",bg="yellow",width=20)
btn7 = Button(root,text="7",width=3)
btn8 = Button(root,text="8",width=3)
btn9 = Button(root,text="9",width=3)
btnM = Button(root,text="*",width=3)                # 乘法符號
btn4 = Button(root,text="4",width=3)
btn5 = Button(root,text="5",width=3)
btn6 = Button(root,text="6",width=3)
btnS = Button(root,text="-",width=3)                # 減法符號
btn1 = Button(root,text="1",width=3)
btn2 = Button(root,text="2",width=3)
btn3 = Button(root,text="3",width=3)
btnP = Button(root,text="+",width=3)                # 加法符號
btn0 = Button(root,text="0",width=8)
btnD = Button(root,text=".",width=3)                # 小數點符號
btnE = Button(root,text="=",width=3)                # 等號符號

lab.grid(row=0,column=0,columnspan=4)
btn7.grid(row=1,column=0,padx=5)
btn8.grid(row=1,column=1,padx=5)
btn9.grid(row=1,column=2,padx=5)
btnM.grid(row=1,column=3,padx=5)                    # 乘法符號
btn4.grid(row=2,column=0,padx=5)
btn5.grid(row=2,column=1,padx=5)
btn6.grid(row=2,column=2,padx=5)
btnS.grid(row=2,column=3,padx=5)                    # 減法符號
btn1.grid(row=3,column=0,padx=5)
btn2.grid(row=3,column=1,padx=5)
btn3.grid(row=3,column=2,padx=5)
btnP.grid(row=3,column=3,padx=5)                    # 加法符號
btn0.grid(row=4,column=0,padx=5,columnspan=2)
btnD.grid(row=4,column=2,padx=5)                    # 小數點符號
btnE.grid(row=4,column=3,padx=5)                    # 等號符號

root.mainloop()






