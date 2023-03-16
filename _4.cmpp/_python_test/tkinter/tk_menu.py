import tkinter as tk

def callback():
    print("called the callback!")

window = tk.Tk()

menu = tk.Menu(window)
window.config(menu=menu)

#第1排功能選單
#filemenu = tk.Menu(menu)
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=callback)
filemenu.add_command(label="Save", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

#第2排功能選單
editmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=callback)
editmenu.add_command(label="Copy", command=callback)
editmenu.add_command(label="Paste", command=callback)

#第3排功能選單
#helpmenu = tk.Menu(menu)
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

window.mainloop()
