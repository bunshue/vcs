import tkinter as tk
win = tk.Tk()
win.title("Button按鈕")
win.geometry('300x200')
button = tk.Button(win, text = "Press", underline=0)
button.pack()
win.mainloop()
