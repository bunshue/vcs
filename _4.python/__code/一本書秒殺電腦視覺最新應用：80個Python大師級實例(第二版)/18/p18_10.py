from tkinter import Tk, Variable, Entry, Button
from tkinter.messagebox import showinfo
tk = Tk()
a = Variable(tk, value='123')
e = Entry(tk, textvariable=a)
b = Button(tk, command=lambda *args: showinfo(message=a.get()),
          text="获取")
e.pack()
b.pack()
tk.mainloop()

