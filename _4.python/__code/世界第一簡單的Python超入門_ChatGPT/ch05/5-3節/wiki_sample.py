import tkinter as tk
import tkinter.filedialog as fd
base = tk.Tk()
def open():
    filename = fd.askopenfilename()
    print('open file => ' + filename)

def exit():
    base.destroy()

def find():
    print('find ! ')

menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='open', command=open)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='find', command=find)
base.config(menu=menubar)

base.mainloop()