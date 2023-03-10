import tkinter as tk

window = tk.Tk()

tk.Label(text="one").pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=5)

tk.Label(text="two").pack()

window.mainloop()


