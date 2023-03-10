import tkinter as tk

window = tk.Tk()

listbox = tk.Listbox(window)
listbox.pack()

listbox.insert(tk.END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)

window.mainloop()

