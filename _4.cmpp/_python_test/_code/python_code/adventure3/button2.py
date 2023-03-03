import Tkinter as tk
window = tk.Tk()


def buttonClick():
    print "Beep!"
    print "Ping!"
    print "Flash!"

button = tk.Button(window, text="Click me!", command=buttonClick)
button.pack()
window.mainloop()