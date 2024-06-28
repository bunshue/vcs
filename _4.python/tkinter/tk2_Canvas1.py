import sys

import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Canvas 測試 1")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

tk.Label(text="Canvas 測試").pack()

color = "#FF0000"
canvas = tk.Canvas(window, width=500, height=150, bg=color)
canvas.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


def changeCanvasBgColor():
    red = 255
    green = 128
    blue = 0
    color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg=color)


button1 = tk.Button(window, text="改變Canvas背景色", command=changeCanvasBgColor)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
