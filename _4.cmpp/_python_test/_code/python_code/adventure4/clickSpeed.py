import Tkinter as tk
import time

window = tk.Tk()

clicks = 0
start = 0
goal = 10


def buttonClick():
    global clicks
    global start

    if clicks == 0:
        start = time.time()
        clicks = clicks + 1
    elif clicks + 1 >= goal:
        score = time.time() - start
        label.config(text="Time: " + str(score))
        clicks = 0
    else:
        clicks = clicks + 1
    slider.set(clicks)

button = tk.Button(window, text="Click me", command=buttonClick)
slider = tk.Scale(window, from_=0, to=goal)
label = tk.Label(window)

button.pack()
slider.pack()
label.pack()

window.mainloop()