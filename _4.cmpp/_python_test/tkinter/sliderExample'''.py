import Tkinter as tk
window = tk.Tk()
slider = tk.Scale(window, from_=0, to=100)
slider.pack()
tk.mainloop()