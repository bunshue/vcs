import tkinter as tk
    
# Display a rectangle
def displayRect():
    canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

# Display an oval
def displayOval():
    canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "oval")

# Display an arc
def displayArc():
    canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", tags = "arc")

# Display a polygon
def displayPolygon():
    canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")

# Display a line
def displayLine():
    canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line")
    canvas.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue", tags = "line")

# Display a string
def displayString():
    canvas.create_text(60, 40, text = "Hi, I am a string", font = "Times 10 bold underline", tags = "string")

# Clear drawings
def clearCanvas():
    canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

window = tk.Tk()

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

window.title("Canvas Demo") # Set title

canvas = tk.Canvas(window, width = 400, height = 400, bg = "white")
canvas.pack()

# Place buttons in frame
frame = tk.Frame(window)
frame.pack()
btRectangle = tk.Button(frame, text = "Rectangle", command = displayRect)
btOval = tk.Button(frame, text = "Oval", command = displayOval)
btArc = tk.Button(frame, text = "Arc", command = displayArc)
btPolygon = tk.Button(frame, text = "Polygon", command = displayPolygon)
btLine = tk.Button(frame, text = "Line", command = displayLine)
btString = tk.Button(frame, text = "String", command = displayString)
btClear = tk.Button(frame, text = "Clear", command = clearCanvas)
btRectangle.grid(row = 1, column = 1)
btOval.grid(row = 1, column = 2)
btArc.grid(row = 1, column = 3)
btPolygon.grid(row = 1, column = 4)
btLine.grid(row = 1, column = 5)
btString.grid(row = 1, column = 6)
btClear.grid(row = 1, column = 7)

window.mainloop()


