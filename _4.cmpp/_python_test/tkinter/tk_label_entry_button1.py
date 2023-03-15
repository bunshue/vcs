import tkinter as tk

window = tk.Tk()

entry1 = tk.Entry(window)
entry2 = tk.Entry(window, show="*")

label1 = tk.Label(window, text="Username")
label2 = tk.Label(window, text="Password")
button = tk.Button(window, text="Login")

label1.grid(row=1, column=1)
entry1.grid(row=1, column=2)

label2.grid(row=2, column=1)
entry2.grid(row=2, column=2)

button.grid(row=3, column=2)

window.mainloop()
