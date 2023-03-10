import tkinter as tk

window = tk.Tk()

def checkPassword():
    password = "1234"
    enteredPassword = passwordEntry.get()
    if password == enteredPassword:
        confirmLabel.config(text="Correct")
    else:
        confirmLabel.config(text="Incorrect")

passwordLabel = tk.Label(window, text="Password:(1234)")
passwordEntry = tk.Entry(window, show="*")

button = tk.Button(window, text="Enter", command=checkPassword)
confirmLabel = tk.Label(window)

passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()
