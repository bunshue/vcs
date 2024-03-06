#import tkinter as tk

try:
    from tkinter import Tk, Toplevel, Frame, Label, Scale, HORIZONTAL
except ImportError:
    from Tkinter import Tk, Toplevel, Frame, Label, Scale, HORIZONTAL

from PIL import Image, ImageTk, ImageEnhance
import sys

class Enhance(Frame):
    def __init__(self, master, image, name, enhancer, lo, hi):
        Frame.__init__(self, master)

        # set up the image
        self.tkim = ImageTk.PhotoImage(image.mode, image.size)
        self.enhancer = enhancer(image)
        self.update("1.0")  # normalize

        # image window
        Label(self, image=self.tkim).pack()

        # scale
        s = Scale(self, label=name, orient=HORIZONTAL,
                  from_=lo, to=hi, resolution=0.01,
                  command=self.update)
        s.set(self.value)
        s.pack()

    def update(self, value):
        self.value = float(value)
        self.tkim.paste(self.enhancer.enhance(self.value))


filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
window = Tk()
#window = tk.Tk()

im = Image.open(filename)

im.thumbnail((300, 400))

Enhance(window, im, "Color", ImageEnhance.Color, 0.0, 4.0).pack()
Enhance(Toplevel(), im, "Sharpness", ImageEnhance.Sharpness, -2.0, 2.0).pack()
Enhance(Toplevel(), im, "Brightness", ImageEnhance.Brightness, -1.0, 3.0).pack()
Enhance(Toplevel(), im, "Contrast", ImageEnhance.Contrast, -1.0, 3.0).pack()

window.mainloop()
