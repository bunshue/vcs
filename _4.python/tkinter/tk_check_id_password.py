import tkinter as tk

def checkPassword():
    password = '1234'
    enteredPassword = entry2.get()
    if password == enteredPassword:
        label_result.config(text="Correct")
    else:
        label_result.config(text="Incorrect")

window = tk.Tk()

label1 = tk.Label(window, text="Username")
entry1 = tk.Entry(window)

label2 = tk.Label(window, text="Password:(1234)")
entry2 = tk.Entry(window, show="*")

button = tk.Button(window, text="Enter", command=checkPassword)
label_result = tk.Label(window)

label1.grid(row=1, column=1)
entry1.grid(row=1, column=2)
label2.grid(row=2, column=1)
entry2.grid(row=2, column=2)
button.grid(row=3, column=2)
label_result.grid(row=4, column=2)

window.mainloop()
