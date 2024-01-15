import tkinter as tk
from tkinter import filedialog, messagebox

base = tk.Tk()

def new_file():
    print('Create a new file')

def open_file():
    filename = filedialog.askopenfilename()
    print('open file => ' + filename)

def save_as():
    filename = filedialog.asksaveasfilename()
    print('save file as => ' + filename)

def exit_app():
    base.destroy()

def cut_text():
    print('Cut text')

def copy_text():
    print('Copy text')

def paste_text():
    print('Paste text')

def about_app():
    messagebox.showinfo("About", "This is a basic program.")

menubar = tk.Menu(base)

# File menu
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='檔案', menu=filemenu)
filemenu.add_command(label='開啟新檔', command=new_file)
filemenu.add_command(label='開啟舊檔', command=open_file)
filemenu.add_command(label='另存為', command=save_as)
filemenu.add_separator()
filemenu.add_command(label='結束', command=exit_app)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='編輯', menu=editmenu)
editmenu.add_command(label='剪下', command=cut_text)
editmenu.add_command(label='複製', command=copy_text)
editmenu.add_command(label='貼上', command=paste_text)

# About menu
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='說明', menu=helpmenu)
helpmenu.add_command(label='關於本程式', command=about_app)

base.config(menu=menubar)

base.mainloop()
