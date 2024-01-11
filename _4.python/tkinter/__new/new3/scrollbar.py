from tkinter import *
win = Tk()
win.title("ScrollBar捲軸")
win.geometry('300x200')
text = Text(win, width = "30", height = "5")
text.grid(row = 0, column = 0)
scrollbar = Scrollbar(command = text.yview, orient = VERTICAL)
scrollbar.grid(row = 0, column = 1, sticky = "ns")
text.configure(yscrollcommand = scrollbar.set)
win.mainloop()

