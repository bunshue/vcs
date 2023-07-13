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
title = "蒙地卡羅模擬"
window.title(title)

width = 400
height = 400
canvas2 = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas2.pack()

'''
蒙地卡羅模擬 Monte Carlo Simulation 使用亂數與機率來解決問題
'''
import random

NUMBER_OF_TRIALS = 10000
numberOfHits = 0

for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    #print(x, y)
    px = (int)(x * 200)
    py = (int)(y * 200)

    cx = px + 200
    cy = py + 200
    radius = 2
    
    if x * x + y * y <= 1:
        canvas2.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill = 'red')
        numberOfHits += 1
    else:
        canvas2.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill = 'green')

pi = 4 * numberOfHits / NUMBER_OF_TRIALS

print("PI is", pi)

window.mainloop()

