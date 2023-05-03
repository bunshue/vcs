import sys
import tkinter as tk
import tkinter.messagebox as messagebox

def show_error():

    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title='IdleX Error',
                         message=('Unable to located "idlexlib".\n' +
                                  'Make sure it is located in the same directory ' +
                                  'as "idlexlib" or run setup.py to install IdleX.\n' +
                                  '  python setup.py install --user'))

show_error()

