import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

def callback():
    print("called the callback!")

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
