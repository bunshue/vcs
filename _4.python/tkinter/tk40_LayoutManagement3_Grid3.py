'''
Grid 測試 Button + Canvas
'''
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
title = "Grid 測試 Button"
window.title(title)

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame1 = tk.Frame(window)
frame1.pack()

message = tk.Message(frame1, text = "這個訊息所佔的位置為3R2C")
message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
tk.Label(frame1, text = "姓 : ").grid(row = 1, column = 3)
tk.Entry(frame1).grid(row = 1, column = 4, padx = 5, pady = 5)
tk.Label(frame1, text = "名 : ").grid(row = 2, column = 3)
tk.Entry(frame1).grid(row = 2, column = 4)
tk.Button(frame1, text = "取得姓名").grid(row = 3, padx = 5, pady = 5, column = 4, sticky = tk.E)

canvas = tk.Canvas(window, width = 400, height = 400, bg = "white")
canvas.pack()

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame2 = tk.Frame(window)
frame2.pack()

btRectangle = tk.Button(frame2, text = "Rectangle", command = displayRect)
btOval = tk.Button(frame2, text = "Oval", command = displayOval)
btArc = tk.Button(frame2, text = "Arc", command = displayArc)
btPolygon = tk.Button(frame2, text = "Polygon", command = displayPolygon)
btLine = tk.Button(frame2, text = "Line", command = displayLine)
btString = tk.Button(frame2, text = "String", command = displayString)
btClear = tk.Button(frame2, text = "Clear", command = clearCanvas)
btRectangle.grid(row = 1, column = 1)
btOval.grid(row = 1, column = 2)
btArc.grid(row = 1, column = 3)
btPolygon.grid(row = 1, column = 4)
btLine.grid(row = 1, column = 5)
btString.grid(row = 1, column = 6)
btClear.grid(row = 1, column = 7)



#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame3 = tk.Frame(window)
frame3.pack()

button00 = tk.Button(frame3, text = "第0排第0個", width = 20)
button00.grid(row = 0, column = 0, padx = 5, pady = 5)
button01 = tk.Button(frame3, text = "第0排第1個", width = 20)
button01.grid(row = 0, column = 1, padx = 5, pady = 5)
button02 = tk.Button(frame3, text = "第0排第2個", width = 20)
button02.grid(row = 0, column = 2, padx = 5, pady = 5)
button10 = tk.Button(frame3, text = "第1排第0個", width = 20)
button10.grid(row = 1, column = 0, padx = 5, pady = 5)
button11 = tk.Button(frame3, text = "第1排第1個", width = 20)
button11.grid(row = 1, column = 1, padx = 5, pady = 5)
button12 = tk.Button(frame3, text = "第1排第2個", width = 20)
button12.grid(row = 1, column = 2, padx = 5, pady = 5)

'''
frame3.columnconfigure(0, weight = 1)
frame3.columnconfigure(1, weight = 2)
#column 0 為基礎寬度，column 1 為column0的兩倍寬
'''
'''
frame3.columnconfigure((0, 2, 3), weight = 1)
frame3.columnconfigure(1, weight = 2)
frame3主視窗的，column 0 , 2, 3為基礎寬度，column 1 為其他column的兩倍寬
'''

button20 = tk.Button(frame3, text = "第2排第0個")
button20.grid(row = 2, column = 0, ipadx = 10, ipady = 10)
button21 = tk.Button(frame3, text = "第2排第1個")
button21.grid(row = 2, column = 1, ipadx = 10, ipady = 10)
button22 = tk.Button(frame3, text = "第2排第2個")
button22.grid(row = 2, column = 2, ipadx = 10, ipady = 10)

'''
參數Sticky填充元件大小
sticky 可以輸入N ,S, E, W或是 混搭例如:EW，NS，NSEW，代表靠N(北方) 、S(南方)、E(東方)、W(西方)，NS(北南延伸)，EW(東西延伸)，NSEW(全方位延伸)
'''

button30 = tk.Button(frame3, text = "第3排第0個")
button30.grid(row = 3, column = 0, ipadx = 10, ipady = 10, sticky = "EW")
button31 = tk.Button(frame3, text = "第3排第1個")
button31.grid(row = 3, column = 1, ipadx = 10, ipady = 10, sticky = "EW")
button32 = tk.Button(frame3, text = "第3排第2個")
button32.grid(row = 3, column = 2, ipadx = 10, ipady = 10, sticky = "EW")



#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame4 = tk.Frame(window)
frame4.pack()

width = 100
height = 100

canvas1 = tk.Canvas(frame4, width = width, height = height)
canvas1.create_line(10, 10, width - 10, height - 10)
canvas1.create_line(width - 10, 10, 10, height - 10)
canvas1.grid(row = 3, column = 1)

canvas2 = tk.Canvas(frame4, width = width, height = height)
canvas2.create_rectangle(10, 10, width - 10, height - 10)
canvas2.grid(row = 3, column = 2)

canvas3 = tk.Canvas(frame4, width = width, height = height)
canvas3.create_oval(10, 10, width - 10, height - 10)
canvas3.grid(row = 3, column = 3)

canvas4 = tk.Canvas(frame4, width = width, height = height)
canvas4.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145)
canvas4.grid(row = 3, column = 4)

canvas5 = tk.Canvas(frame4, width = width, height = height)
canvas5.create_rectangle(10, 10, width - 10, height - 10, fill = "red")
canvas5.grid(row = 3, column = 5)

canvas6 = tk.Canvas(frame4, width = width, height = height)
canvas6.create_oval(10, 10, width - 10, height - 10, fill = "red")
canvas6.grid(row = 3, column = 6)

canvas7 = tk.Canvas(frame4, width = width, height = height)
canvas7.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145, fill = "red")
canvas7.grid(row = 3, column = 7)

window.mainloop()
