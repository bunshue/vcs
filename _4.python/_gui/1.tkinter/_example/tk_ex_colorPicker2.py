import tkinter as tk

window = tk.Tk()


def sliderUpdate(something):
    red = scale1.get()
    green = scale2.get()
    blue = scale3.get()

    color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=color)
    hexText.delete(0, tk.END)
    hexText.insert(0, color)


scale1 = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
scale2 = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
scale3 = tk.Scale(window, from_=0, to=255, command=sliderUpdate)

canvas = tk.Canvas(window, width=200, height=200)

hexText = tk.Entry(window)
# hexText = tk.Entry(window, validate="focusout")

# 設定控件的排列位置
scale1.grid(row=1, column=1)
scale2.grid(row=1, column=2)
scale3.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
hexText.grid(row=3, column=1, columnspan=3)

window.mainloop()
