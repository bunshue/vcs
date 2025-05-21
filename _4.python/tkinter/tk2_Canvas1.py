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

n = 0


def click(e):
    global n
    n = n + 1
    if n == 3:
        n = 0
    cvs.delete("all")
    if n == 0:
        cvs.create_oval(200, 100, 400, 300, fill="green")
    if n == 1:
        cvs.create_rectangle(200, 100, 400, 300, fill="gold")
    if n == 2:
        cvs.create_polygon(300, 100, 200, 300, 400, 300, fill="red")


root = tk.Tk()
root.title("取得滑鼠點擊事件")
root.bind("<Button>", click)
cvs = tk.Canvas(width=600, height=400, bg="white")
cvs.create_text(300, 200, text="請點選視窗內部任何一個位置")
cvs.pack()
root.mainloop()

print("------------------------------------------------------------")  # 60個

FNT = ("Times New Roman", 40)


def move(e):
    cvs.delete("all")
    s = "({}, {})".format(e.x, e.y)
    cvs.create_text(300, 200, text=s, font=FNT)


root = tk.Tk()
root.title("滑鼠游標的座標")
root.bind("<Motion>", move)
cvs = tk.Canvas(width=600, height=400)
cvs.create_text(300, 200, text="請在視窗之內移動滑鼠游標")
cvs.pack()
root.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
