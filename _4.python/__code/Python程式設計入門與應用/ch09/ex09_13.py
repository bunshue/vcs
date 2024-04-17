# Filename: ex09_13.py
import tkinter as tk
import tkinter.font as tkfont
def but_click():
    selected_options = ''
    if asia.get():
        selected_options += chkbut_asia.cget('text')
    if america.get():
        selected_options += chkbut_america.cget('text')
    if europe.get():
        selected_options += chkbut_europe.cget('text')
    if aferica.get():
        selected_options += chkbut_aferica.cget('text')
    lab_result.config(text=selected_options)   
win = tk.Tk()
win.geometry("400x300")
win.title("試題與測驗分析程式")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
asia = tk.IntVar()
chkbut_asia = tk.Checkbutton(win, text='亞洲',variable=asia,anchor=tk.W)
chkbut_asia.pack(padx=90, pady=5, fill=tk.X)
america = tk.IntVar()
chkbut_america = tk.Checkbutton(win, text='美洲',variable=america,anchor=tk.W)
chkbut_america.pack(padx=90, pady=5, fill=tk.X)
europe = tk.IntVar()
chkbut_europe = tk.Checkbutton(win, text='歐洲',variable=europe,anchor=tk.W)
chkbut_europe.pack(padx=90, pady=5, fill=tk.X)
aferica = tk.IntVar()
chkbut_aferica = tk.Checkbutton(win, text='非洲',variable=aferica,anchor=tk.W)
chkbut_aferica.pack(padx=90, pady=5, fill=tk.X)
but = tk.Button(win, text='確定', command=but_click, font=default_font, padx=15)
but.pack(padx=10, pady=5)
lab_result = tk.Label(win, font=default_font, fg='black', width=20)
lab_result.pack(padx=10, pady=(5,10))
win.mainloop()