import tkinter as tk

def add(): 
    string3.set(eval(string1.get()) + eval(string2.get()))
    
def subtract():
    string3.set(eval(string1.get()) - eval(string2.get()))
    
def multiply():
    string3.set(eval(string1.get()) * eval(string2.get()))
    
def divide():
    string3.set(eval(string1.get()) / eval(string2.get()))

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)


# Create a menu bar
menubar = tk.Menu(window)
window.config(menu = menubar) # Display the menu bar

# create a pulldown menu, and add it to the menu bar
operationMenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Operation", menu = operationMenu)
operationMenu.add_command(label = "Add", command = add)
operationMenu.add_command(label = "Subtract", command = subtract)
operationMenu.add_separator()
operationMenu.add_command(label = "Multiply", command = multiply)
operationMenu.add_command(label = "Divide", command = divide)

# create more pulldown menus
exitmenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Exit", menu = exitmenu)
exitmenu.add_command(label = "Quit", command = window.quit)


# Add labels and entries to frame1
frame1 = tk.Frame(window)
frame1.grid(row = 2, column = 1, pady = 10)
tk.Label(frame1, text = "Number 1:").pack(side = tk.LEFT)
string1 = tk.StringVar()
tk.Entry(frame1, width = 5, textvariable = string1, justify = tk.RIGHT).pack(side = tk.LEFT)
tk.Label(frame1, text = "Number 2:").pack(side = tk.LEFT)
string2 = tk.StringVar()
tk.Entry(frame1, width = 5, textvariable = string2, justify = tk.RIGHT).pack(side = tk.LEFT)
tk.Label(frame1, text = "Result:").pack(side = tk.LEFT)
string3 = tk.StringVar()
tk.Entry(frame1, width = 5, textvariable = string3, justify = tk.RIGHT).pack(side = tk.LEFT)

window.mainloop()
