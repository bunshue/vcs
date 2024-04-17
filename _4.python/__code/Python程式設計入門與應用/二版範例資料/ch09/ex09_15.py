# Filename: ex09_15.py
import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("圖形顯示")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file='python.PNG')
gs = tk.Canvas(win)
gs.create_image(60,120,image=photo)
gs.pack()
win.mainloop()