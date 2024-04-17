# Filename: ex09_12.py
import tkinter as tk
import tkinter.font as tkfont
def spinbox_select():
    selected_month = month.get()
    lab_result.config(text=selected_month)    
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
month = tk.IntVar()
month.set(1)
spinbox = tk.Spinbox(win, from_=1, to=12, textvariable=month, command=spinbox_select, font=default_font)
spinbox.pack(padx=10, pady=10)
lab_result = tk.Label(win, font=default_font, fg='black')
lab_result.pack(padx=10, pady=(5,10))    
win.mainloop()