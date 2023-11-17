import tkinter as tk
import tkinter.messagebox as tkMessageBox
#import tkinter.messagebox

win = tk.Tk()
def hello():
   tkMessageBox.showinfo('訊息框', "Hello World")

B1 = tk.Button(win, text = "Say Hello", command = hello)
B1.pack()

win.mainloop()
