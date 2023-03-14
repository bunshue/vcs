import tkinter as tk

window = tk.Tk()

def callback(event):
    print("clicked at", event.x, event.y)

frame = tk.Frame(window, width=300, height=300)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()
