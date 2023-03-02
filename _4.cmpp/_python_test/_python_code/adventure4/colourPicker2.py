import Tkinter as tk
window = tk.Tk()


def sliderUpdate(something):
    red = redSlider.get()
    green = greenSlider.get()
    blue = blueSlider.get()

    colour = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=colour)
    hexText.delete(0, tk.END)
    hexText.insert(0, colour)

redSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
greenSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
blueSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)

canvas = tk.Canvas(window, width=200, height=200)

hexText = tk.Entry(window)

redSlider.grid(row=1, column=1)
greenSlider.grid(row=1, column=2)
blueSlider.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
hexText.grid(row=3, column=1, columnspan=3)


window.mainloop()