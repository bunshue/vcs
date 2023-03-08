import tkinter as tk

window = tk.Tk()

def buttonClick():
    print("Beep!")
    print("Ping!")
    print("Flash!")

button = tk.Button(window, text="Click me!", command=buttonClick)
button.pack()

button2 = tk.Button(window, text="Click me!", command=buttonClick)
button2.pack()

button3 = tk.Button(window, text="Click me!", command=buttonClick)
button3.pack()

button4 = tk.Button(window, text="Click me!", command=buttonClick)
button4.pack()

window.mainloop()



