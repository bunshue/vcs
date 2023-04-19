import os
import sys
import shlex

WINREG = True

import tkinter as tk
import tkinter.messagebox as mb

try:
    import winreg as W
except:
    WINREG = False

if WINREG == False:
    mb.showerror(title='Edit with IdleX',
                 message='Unable to import winreg')

    sys.exit(1)

def quitprog():
    root.destroy()

def build_gui():
    f1 = tk.Frame(root)
    f1.config(borderwidth=2, relief=tk.GROOVE)
    f1.pack(side=tk.TOP, fill=tk.BOTH, expand=1, padx=5, pady=5)

    msg = ["This will configure the right-click context menu",
           "item 'Edit with IdleX'. This will sit alongside the",
           "'Edit with IDLE' menu item.",
           "",
           "",
           "If you change the location of IdleX, re-run this script.",
           "Otherwise, no action will occur if you click 'Edit with IdleX'.",
           "",
           "This program creates a registry key here:",
           r"HKEY_CURRENT_USER\Software\Classes\Python.File\shell\Edit with IdleX\command",
           ]
    L = tk.Label(f1, text='\n'.join(msg), wraplength=300, justify=tk.LEFT)
    
    b1 = tk.Button(f1, text="Add 'Edit with IdleX' to context menu")

    b2 = tk.Button(f1, text="Remove 'Edit with IdleX' from context menu")

    b3 = tk.Button(f1, text='Exit this program', command=quitprog)

    TOP = tk.TOP
    L.pack(side=TOP, fill=tk.X, expand=True)
    b1.pack(side=TOP, fill=tk.X, expand=True)
    b2.pack(side=TOP, fill=tk.X, expand=True)
    b3.pack(side=TOP, fill=tk.X, expand=True)

root = tk.Tk()
root.title('Edit with IdleX')
build_gui()
root.mainloop()


