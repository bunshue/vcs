import tkinter as tk

window = tk.Tk()

v = tk.IntVar()

tk.Radiobutton(window, text="One", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(window, text="Two", variable=v, value=2).pack(anchor=tk.W)


MODES = [
    ("Monochrome", "1"),
    ("Grayscale", "L"),
    ("True color", "RGB"),
    ("Color separation", "CMYK"),
]

v = tk.StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = tk.Radiobutton(window, text=text, variable=v, value=mode)
    b.pack(anchor=tk.W)

window.mainloop()

