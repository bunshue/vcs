import tkinter as tk

window = tk.Tk()

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(window, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(tk.END, str(i))
    
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=listbox.yview)

window.mainloop()
