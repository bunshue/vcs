import tkinter as tk

master = tk.Tk()

#w = tk.Message(master, text="this is a relatively long message")    #自動換行
w = tk.Message(master, text="this is a relatively long message", width=50)  #限定寬度
w.pack()

master.mainloop()
