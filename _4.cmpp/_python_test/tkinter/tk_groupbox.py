import tkinter as tk

window = tk.Tk()

group = tk.LabelFrame(window, text="Group", padx=5, pady=5)
group.pack(padx=10, pady=10)

w = tk.Entry(group)
w.pack()

window.mainloop()



