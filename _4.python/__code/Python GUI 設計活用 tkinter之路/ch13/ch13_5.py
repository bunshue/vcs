# ch13_5.py
from tkinter import *
from  tkinter.ttk  import *
 
root = Tk()
root.title("ch13_5")                        # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var,        # 建立Combobox
              value=("Python","Java","C#","C"))   
cb.pack(pady=10)

root.mainloop()











