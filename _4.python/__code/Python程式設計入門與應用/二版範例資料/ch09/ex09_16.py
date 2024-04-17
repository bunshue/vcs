# Filename: ex09_16.py
import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("幾何圖形")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file='python.PNG')
gs = tk.Canvas(win,width=400,height=300)
gs.pack()
gs.create_rectangle(50,20,150,80)
gs.create_rectangle(80,60,200,100,fill='#FF0000')
gs.create_line(200,200,220,200)
gs.create_line(200,160,320,160,fill='#FF0000')                     
win.mainloop()