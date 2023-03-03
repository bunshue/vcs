import Tkinter as tk
window = tk.Tk()


def buttonClick():
    print "Beep!"

button = tk.Button(window, text="Click me!", command=buttonClick)
button.pack()
window.mainloop()