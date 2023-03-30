#!/usr/bin/env python
#
# The Python Imaging Library
# $Id$
#

from __future__ import print_function

try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from PIL import Image, ImageTk
import sys


# --------------------------------------------------------------------
# an image animation player

class UI(Label):

    def __init__(self, master, im):
        if isinstance(im, list):
            # list of images
            self.im = im[1:]
            im = self.im[0]
        else:
            # sequence
            self.im = im

        if im.mode == "1":
            self.image = ImageTk.BitmapImage(im, foreground="white")
        else:
            self.image = ImageTk.PhotoImage(im)

        Label.__init__(self, master, image=self.image, bg="black", bd=0)

        self.update()

        try:
            duration = im.info["duration"]
        except KeyError:
            duration = 100
        self.after(duration, self.next)

    def next(self):

        if isinstance(self.im, list):

            try:
                im = self.im[0]
                del self.im[0]
                self.image.paste(im)
            except IndexError:
                return  # end of list

        else:

            try:
                im = self.im
                im.seek(im.tell() + 1)
                self.image.paste(im)
            except EOFError:
                return  # end of file

        try:
            duration = im.info["duration"]
        except KeyError:
            duration = 100
        self.after(duration, self.next)

        self.update_idletasks()


# --------------------------------------------------------------------
# script interface

filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/data/human.jpg'
filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/data/human2.jpg'

if __name__ == "__main__":

    filename = filename1

    root = Tk()
    root.title(filename)

    # list of images
    print("loading...")
    im = []
    im.append(Image.open(filename1))
    im.append(Image.open(filename2))
    
    #im = Image.open(filename)

    UI(root, im).pack()

    root.mainloop()
