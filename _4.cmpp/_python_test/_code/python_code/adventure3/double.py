import Tkinter as tk
window = tk.Tk()

def changeString():
    stringToCopy = entry.get()
    entry.insert(0, stringToCopy)

entry = tk.Entry(window)
button = tk.Button(window, text="Change", command=changeString)

entry.pack()
button.pack()
window.mainloop()