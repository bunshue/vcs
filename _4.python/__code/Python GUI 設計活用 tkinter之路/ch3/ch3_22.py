# ch3_22.py
from tkinter import *

root = Tk()
root.title("ch3_22")               # 視窗標題
    
Label(root,text='Mississippi',bg='red',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  
Label(root,text='Kentucky',bg='green',fg='white',
      font='Arial 20 bold italic').pack(side=LEFT,fill=BOTH,expand=True)  
Label(root,text='Purdue',bg='blue',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  

root.mainloop() 






