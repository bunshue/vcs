import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

canvas1 = tk.Canvas(window, bg = 'yellow', width = 600, height = 300)
canvas1.grid(columnspan = 3, rowspan = 3)

#tk顯示一張圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)
image = ImageTk.PhotoImage(image)
label1 = tk.Label(image = image)
label1.image = image
label1.grid(column = 1, row = 0)

canvas2 = tk.Canvas(window, bg = 'pink', width = 600, height = 250)
canvas2.grid(columnspan = 3)

window.mainloop()
