import tkinter as tk

def callback():
    print("called the callback!")

window = tk.Tk()

menubar = tk.Menu(window)

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=callback)
filemenu.add_command(label="Save", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=callback)
editmenu.add_command(label="Copy", command=callback)
editmenu.add_command(label="Paste", command=callback)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=callback)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
window.config(menu=menubar)



