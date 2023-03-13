import tkinter as tk

window = tk.Tk()

#w = tk.Message(window, text="this is a relatively long message")    #自動換行
w = tk.Message(window, text="this is a relatively long message", width=50)  #限定寬度
w.pack()

window.mainloop()
