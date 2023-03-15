import tkinter as tk

window = tk.Tk()

redDirection = "up"
greenDirection = "up"
blueDirection = "up"

red = 0
green = 0
blue = 0

def colourUpdate():
    global red
    global green
    global blue

    global redDirection
    global greenDirection
    global blueDirection

    redIncrement = scale1.get()
    greenIncrement = scale2.get()
    blueIncrement = scale3.get()

    red = incrementColour(red, redIncrement, redDirection)
    green = incrementColour(green, greenIncrement, greenDirection)
    blue = incrementColour(blue, blueIncrement, blueDirection)

    redDirection = updateDirection(red, redDirection)
    greenDirection = updateDirection(green, greenDirection)
    blueDirection = updateDirection(blue, blueDirection)

    redHex = format(red, 'x')
    redHex = str(redHex.zfill(2))
    greenHex = format(green, 'x')
    greenHex = str(greenHex.zfill(2))
    blueHex = format(blue, 'x')
    blueHex = format(blueHex.zfill(2))

    colour = "#" + redHex + greenHex + blueHex
    canvas.config(bg=colour)
    #window.after(100, colourUpdate)    #這行是什麼意思
    #print('設定顏色')


def incrementColour(colourValue, increment, direction):
    if direction == "up":
        if colourValue + increment >= 255:
            return 255
        else:
            return colourValue + increment
    elif direction == "down":
        if colourValue - increment <= 0:
            return 0
        else:
            return colourValue - increment


def updateDirection(colourValue, direction):
    if colourValue >= 255:
        return "down"
    elif colourValue <= 0:
        return "up"
    else:
        return direction

scale1 = tk.Scale(window, from_=0, to=20)
scale2 = tk.Scale(window, from_=0, to=20)
scale3 = tk.Scale(window, from_=0, to=20)
canvas = tk.Canvas(window, width=300, height=300)
button = tk.Button(window, text="Go!", command=colourUpdate)

#設定控件的排列位置
scale1.grid(row=1, column=1)
scale2.grid(row=1, column=2)
scale3.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
button.grid(row=3, column=2)

window.mainloop()


