import tkinter as tk

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

win = tk.Tk()
img = ImageTk.PhotoImage(Image.open(filename))
label1 =tk.Label(win, image = img)
label1.pack()

win.mainloop()
