#!/usr/bin/python 
# import Tkinter
try:
  import Tkinter as tk
  import tkMessageBox
except ImportError:
  import tkinter as tk
  import tkinter.messagebox as tkMessageBox

win = tk.Tk()
def hello():
   tkMessageBox.showinfo("PowenKo.com", "showinfo")
   tkMessageBox.showwarning("PowenKo.com", "showwarning")
   tkMessageBox.showerror("PowenKo.com", "showerror")
   result =tkMessageBox.askquestion("PowenKo.com", "askquestion")
   print(result)
   result=tkMessageBox.askokcancel("PowenKo.com", "askokcancel")
   print(result)
   result=tkMessageBox.askyesno("PowenKo.com", "showeraskyesnoror")
   print(result)
   result=tkMessageBox.askretrycancel("PowenKo.com", "askretrycancel")
   print(result)


B1 = tk.Button(win, text = "Say Hello", command = hello)
B1.pack()

win.mainloop()