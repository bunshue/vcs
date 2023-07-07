'''
綁定鍵盤滑鼠事件 Canvas
'''
import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = '綁定鍵盤滑鼠事件 Canvas'
window.title(title)

print('左鍵變大 右鍵變小')

def mouseClick1(event):
    global radius
    canvas.delete("oval")
    if radius < 100:
        radius += 2
    canvas.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, tags = "oval")

   
def mouseClick3(event):
    global radius
    canvas.delete("oval")
    if radius > 2:
        radius -= 2
    canvas.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, tags = "oval")

canvas = tk.Canvas(window, bg = "white", width = 200, height = 200)
canvas.pack()

radius = 50
canvas.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, tags = "oval")

# Bind canvas with mouse events
canvas.bind("<Button-1>", mouseClick1)
canvas.bind("<Button-3>", mouseClick3)

window.mainloop()
