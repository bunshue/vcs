# ch8_6.py
from tkinter import Tk
from tkinter.ttk import Frame, Style

root = Tk()
root.title("ch8_6")
style = Style()                 # 改用Style
style.theme_use("alt")          # 改用alt支援Style

fm1 = Frame(root,width=150,height=80,relief="flat")
fm1.grid(row=0,column=0,padx=5,pady=5)

fm2 = Frame(root,width=150,height=80,relief="groove")
fm2.grid(row=0,column=1,padx=5,pady=5)

fm3 = Frame(root,width=150,height=80,relief="raised")
fm3.grid(row=0,column=2,padx=5,pady=5)

fm4 = Frame(root,width=150,height=80,relief="ridge")
fm4.grid(row=1,column=0,padx=5,pady=5)

fm5 = Frame(root,width=150,height=80,relief="solid")
fm5.grid(row=1,column=1,padx=5,pady=5)

fm6 = Frame(root,width=150,height=80,relief="sunken")
fm6.grid(row=1,column=2,padx=5,pady=5)

root.mainloop()








