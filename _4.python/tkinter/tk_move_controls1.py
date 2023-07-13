import math
import tkinter as tk

# 建立主視窗
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
title = "移動測試"
window.title(title)

#公用變數
width = 300
height = 300
canvas = tk.Canvas(window, bg = 'pink', width = width, height = height)
canvas.pack()

radius = 20
x1 = 0 # Starting x position
y1 = 100
sleepTime = 100 #Sleep 一段時間(msec)
canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius, fill = 'red', tags = 'moving1')

x2 = x1
y2 = 200
canvas.create_oval(x2 - radius, y2 - radius, x2 + radius, y2 + radius, fill = 'red', tags = 'moving2')

dx = 10

count = 0
msg = tk.StringVar()
msg.set('')

label1 = tk.Label(window, textvariable = msg, fg = 'red', font=("新細明體", 20))
label1.pack() 

while True:
    #移動法
    canvas.move('moving1', dx, 0) #移動那個被畫上去的移動物件
    canvas.after(sleepTime) #Sleep 一段時間(msec)
    canvas.update() # Update canvas
    count = count + 1
    msg.set(count)
    
    if x1 < width:
        x1 += dx  # Set new position 
    else:
        x1 = 0
        canvas.delete('moving1') #刪除所有移動物件
        #畫 移動物件
        canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius, fill = 'red', tags = 'moving1')

    #重畫法
    canvas.delete('moving2') #刪除所有移動物件
    y2 = 200 + 50 * math.sin(count / 5)
    x2 = x1
    canvas.create_oval(x2 - radius, y2 - radius, x2 + radius, y2 + radius, fill = 'red', tags = 'moving2')


window.mainloop()

