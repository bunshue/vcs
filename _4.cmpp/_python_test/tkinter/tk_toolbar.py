import tkinter as tk

window = tk.Tk()

def callback():
    print("called the callback!")

# create a toolbar
toolbar = tk.Frame(window)

b = tk.Button(toolbar, text="new", width=6, command=callback)
b.pack(side=tk.LEFT, padx=2, pady=2)

b = tk.Button(toolbar, text="open", width=6, command=callback)
b.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)

window.mainloop()
