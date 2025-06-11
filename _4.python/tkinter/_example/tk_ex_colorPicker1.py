import tkinter as tk


def colorUpdate():
    global red
    global green
    global blue

    global redDirection
    global greenDirection
    global blueDirection

    redIncrement = scale1.get()
    greenIncrement = scale2.get()
    blueIncrement = scale3.get()

    red = incrementColor(red, redIncrement, redDirection)
    green = incrementColor(green, greenIncrement, greenDirection)
    blue = incrementColor(blue, blueIncrement, blueDirection)

    redDirection = updateDirection(red, redDirection)
    greenDirection = updateDirection(green, greenDirection)
    blueDirection = updateDirection(blue, blueDirection)

    redHex = format(red, "x")
    redHex = str(redHex.zfill(2))
    greenHex = format(green, "x")
    greenHex = str(greenHex.zfill(2))
    blueHex = format(blue, "x")
    blueHex = format(blueHex.zfill(2))

    color = "#" + redHex + greenHex + blueHex
    canvas.config(bg=color)
    # window.after(100, colorUpdate)    #這行是什麼意思, delay 100 msec
    print("設定顏色" + color)


def incrementColor(colorValue, increment, direction):
    if direction == "up":
        if colorValue + increment >= 255:
            return 255
        else:
            return colorValue + increment
    elif direction == "down":
        if colorValue - increment <= 0:
            return 0
        else:
            return colorValue - increment


def updateDirection(colorValue, direction):
    if colorValue >= 255:
        return "down"
    elif colorValue <= 0:
        return "up"
    else:
        return direction


window = tk.Tk()

redDirection = "up"
greenDirection = "up"
blueDirection = "up"

red = 0
green = 0
blue = 0

scale1 = tk.Scale(window, from_=0, to=20)
scale2 = tk.Scale(window, from_=0, to=20)
scale3 = tk.Scale(window, from_=0, to=20)
canvas = tk.Canvas(window, width=300, height=300)
button = tk.Button(window, text="Go!", command=colorUpdate)

# 設定控件的排列位置
scale1.grid(row=1, column=1)
scale2.grid(row=1, column=2)
scale3.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
button.grid(row=3, column=2)

window.mainloop()
