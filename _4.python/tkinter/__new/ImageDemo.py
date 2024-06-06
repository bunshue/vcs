from tkinter import * # Import tkinter

class ImageDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Image Demo") # Set title
        
        # Create PhotoImage objects
        caImage = PhotoImage(file = "ca.gif")
        chinaImage = PhotoImage(file = "china.gif")
        leftImage = PhotoImage(file = "left.gif")
        rightImage = PhotoImage(file = "right.gif")
        usImage = PhotoImage(file = "usIcon.gif")
        ukImage = PhotoImage(file = "ukIcon.gif")
        crossImage = PhotoImage(file = "x.gif")
        circleImage = PhotoImage(file = "o.gif")
        
        # frame1 to contain label and canvas
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image = caImage).pack(side = LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image = chinaImage)
        canvas["width"] = 200
        canvas["height"] = 100
        canvas.pack(side = LEFT)
        
        # frame2 to contain buttons, check buttons, and radio buttons
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, image = leftImage).pack(side = LEFT)
        Button(frame2, image = rightImage).pack(side = LEFT)
        Checkbutton(frame2, image = usImage).pack(side = LEFT)
        Checkbutton(frame2, image = ukImage).pack(side = LEFT)
        Radiobutton(frame2, image = crossImage).pack(side = LEFT)
        Radiobutton(frame2, image = circleImage).pack(side = LEFT)
        
        window.mainloop() # Create an event loop

print(E)

ImageDemo() # Create GUI 


print("------------------------------------------------------------")  # 60個

import tkinter as tk

window = tk.Tk()
window.geometry("600x400")

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

# Create PhotoImage objects
caImage = tk.PhotoImage(file = "ca.gif")
chinaImage = tk.PhotoImage(file = "china.gif")
leftImage = tk.PhotoImage(file = "left.gif")
rightImage = tk.PhotoImage(file = "right.gif")
usImage = tk.PhotoImage(file = "usIcon.gif")
ukImage = tk.PhotoImage(file = "ukIcon.gif")
crossImage = tk.PhotoImage(file = "x.gif")
circleImage = tk.PhotoImage(file = "o.gif")

# frame1 to contain label and canvas
frame1 = tk.Frame(window)
frame1.pack()
tk.Label(frame1, image = caImage).pack(side = tk.LEFT)
canvas = tk.Canvas(frame1)
canvas.create_image(90, 50, image = chinaImage)
canvas["width"] = 200
canvas["height"] = 100
canvas.pack(side = tk.LEFT)

# frame2 to contain buttons, check buttons, and radio buttons
frame2 = tk.Frame(window)
frame2.pack()
tk.Button(frame2, image = leftImage).pack(side = tk.LEFT)
tk.Button(frame2, image = rightImage).pack(side = tk.LEFT)

tk.Checkbutton(frame2, image = usImage).pack(side = tk.LEFT)
tk.Checkbutton(frame2, image = ukImage).pack(side = tk.LEFT)

tk.Radiobutton(frame2, image = crossImage).pack(side = tk.LEFT)
tk.Radiobutton(frame2, image = circleImage).pack(side = tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
