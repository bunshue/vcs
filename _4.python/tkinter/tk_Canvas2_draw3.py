import tkinter as tk

window = tk.Tk()
window.title("Display Figures")

width = 100
height = 100

canvas1 = tk.Canvas(window, width = width, height = height)
canvas1.create_line(10, 10, width - 10, height - 10)
canvas1.create_line(width - 10, 10, 10, height - 10)
canvas1.grid(row = 3, column = 1)

canvas2 = tk.Canvas(window, width = width, height = height)
canvas2.create_rectangle(10, 10, width - 10, height - 10)
canvas2.grid(row = 3, column = 2)

canvas3 = tk.Canvas(window, width = width, height = height)
canvas3.create_oval(10, 10, width - 10, height - 10)
canvas3.grid(row = 3, column = 3)

canvas4 = tk.Canvas(window, width = width, height = height)
canvas4.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145)
canvas4.grid(row = 3, column = 4)

canvas5 = tk.Canvas(window, width = width, height = height)
canvas5.create_rectangle(10, 10, width - 10, height - 10, fill = "red")
canvas5.grid(row = 3, column = 5)

canvas6 = tk.Canvas(window, width = width, height = height)
canvas6.create_oval(10, 10, width - 10, height - 10, fill = "red")
canvas6.grid(row = 3, column = 6)

canvas7 = tk.Canvas(window, width = width, height = height)
canvas7.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145, fill = "red")
canvas7.grid(row = 3, column = 7)

window.mainloop()
