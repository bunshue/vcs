# -*- coding: utf-8 -*-

import tkinter as tk
win = tk.Tk()
win.geometry("200x100")
win.title("Label元件的參數設定")

label = tk.Label(win, bg="#ff00ff", fg="#ffff00", \
                font ="新細明體 14 bold italic", \
                padx=20, pady=5, text = "生日快樂")
label.pack()

win.mainloop()
