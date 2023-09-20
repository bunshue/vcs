import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=640, height=480)
canvas.pack()
canvas.create_text(200, 50, text='Welcome to the United States')
canvas.create_text(200, 80, text='Welcome to the United States', fill='blue')
canvas.create_text(300, 120, text='Welcome to the United States', fill='blue',
                   font=('Old English Text MT',20))
canvas.create_text(300, 160, text='Welcome to the United States', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
canvas.create_text(300, 200, text='歡迎來到美國', fill='blue',
                   font=('華康新綜藝體 Std W7',20))


