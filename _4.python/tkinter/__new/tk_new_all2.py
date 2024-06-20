import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

import random

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個






# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2)
#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)
b.pack()


window.mainloop()



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk10_frame.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
tk.Label(window, text='on the window').pack()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm, )
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()
window.mainloop()










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk11_msgbox.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='hahahaha')
    #tk.messagebox.showwarning(title='Hi', message='nononono')
    #tk.messagebox.showerror(title='Hi', message='No!! never')
    #print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))   # return 'yes' , 'no'
    #print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.asktrycancel(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))     # return, True, False, None

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk12_position.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.geometry('200x200')

#canvas = tk.Canvas(window, height=150, width=500)
#canvas.grid(row=1, column=1)
#image_file = tk.PhotoImage(file='welcome.gif')
#image = canvas.create_image(0, 0, anchor='nw', image=image_file)

#tk.Label(window, text='1').pack(side='top')
#tk.Label(window, text='1').pack(side='bottom')
#tk.Label(window, text='1').pack(side='left')
#tk.Label(window, text='1').pack(side='right')

#for i in range(4):
    #for j in range(3):
        #tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk3_entry_text.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
# e = tk.Entry(window, show="*")
e = tk.Entry(window, show="1")
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert(2.2, var)

b1 = tk.Button(window, text='insert point', width=15,
              height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end',
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk4_listbox.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15,
              height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk5_radiobutton.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    l.config(text='you have selected ' + var.get())

r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk6_scale.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk7_checkbutton.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()


window.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk8_canvas.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
x0, y0, x1, y1= 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(rect, 0, 2)

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\tkinterTUT\tk9_menubar.py

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, text='', bg='yellow')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)

window.mainloop()



print("------------------------------------------------------------")  # 60個

