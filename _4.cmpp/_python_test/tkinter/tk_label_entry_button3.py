import tkinter as tk

window = tk.Tk()

def checkPassword():
    password = '1234'
    enteredPassword = entry1.get()
    if password == enteredPassword:
        label2.config(text="Correct")
    else:
        label2.config(text="Incorrect")

label1 = tk.Label(window, text="Password:(1234)")
entry1 = tk.Entry(window, show="*")

button = tk.Button(window, text="Enter", command=checkPassword)
label2 = tk.Label(window)

label1.pack()
entry1.pack()
button.pack()
label2.pack()

window.mainloop()
