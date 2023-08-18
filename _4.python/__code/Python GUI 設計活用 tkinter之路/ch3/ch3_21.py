# ch3_21.py
from tkinter import *

root = Tk()
root.title("ch3_21")               # 視窗標題
root.geometry("300x200")
    
Label(root,text='Mississippi',bg='red',fg='white',
      font='Times 24 bold').pack(fill=X)  
Label(root,text='Kentucky',bg='green',fg='white',
      font='Arial 24 bold italic').pack(fill=BOTH,expand=True)  
Label(root,text='Purdue',bg='blue',fg='white',
      font='Times 24 bold').pack(fill=X)  

root.mainloop() 






