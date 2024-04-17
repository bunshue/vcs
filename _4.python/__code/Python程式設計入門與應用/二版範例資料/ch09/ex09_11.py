# Filename: ex09_11.py
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
def combox_select(event):
    selected_area = event.widget.get()
    lab_result.config(text=selected_area)
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS=('屏東縣','高雄市','台南市','台東縣')
area = tk.StringVar()
combox = ttk.Combobox(win, value=AREA_OPTIONS, textvariable=area, font=default_font)
combox.bind('<<ComboboxSelected>>', combox_select)
combox.current(0)
combox.pack(padx=10, pady=10)
lab_result = tk.Label(win, font=default_font, fg='black', width=18)
lab_result.pack(padx=10, pady=(5,10))       
win.mainloop()