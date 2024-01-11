import tkinter as tk
import tkinter.messagebox as tkMessageBox

win = tk.Tk()
def hello():
   tkMessageBox.showinfo('訊息框', "showinfo")
   tkMessageBox.showwarning('訊息框', "showwarning")
   tkMessageBox.showerror('訊息框', "showerror")
   result =tkMessageBox.askquestion('訊息框', "askquestion")
   print(result)
   result=tkMessageBox.askokcancel('訊息框', "askokcancel")
   print(result)
   result=tkMessageBox.askyesno('訊息框', "showeraskyesnoror")
   print(result)
   result=tkMessageBox.askretrycancel('訊息框', "askretrycancel")
   print(result)

B1 = tk.Button(win, text = "Say Hello", command = hello)
B1.pack()

win.mainloop()
