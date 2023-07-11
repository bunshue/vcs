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
x = 0 # Starting x position
y = 100
sleepTime = 100 # Set a sleep time
canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = 'red', tags = "moving")

dx = 10

count = 0
msg = tk.StringVar()
msg.set('')

label1 = tk.Label(window, textvariable = msg, fg = 'red', font=("新細明體", 20))
label1.pack() 

while True:
    canvas.move('moving', dx, 0) #移動那個被畫上去的移動物件
    canvas.after(sleepTime) # Sleep for 100 milliseconds
    canvas.update() # Update canvas
    count = count + 1
    msg.set(count)
    
    if x < width:
        x += dx  # Set new position 
    else:
        x = 0
        canvas.delete('moving') #刪除所有移動物件
        #畫 移動物件
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = 'red', tags = "moving")

window.mainloop()

