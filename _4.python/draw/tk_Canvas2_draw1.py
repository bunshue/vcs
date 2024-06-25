import sys
import math
import random
import tkinter as tk

print("------------------------------------------------------------")  # 60個

W = 900
H = 800

window = tk.Tk()
window.geometry("900x800")
title = "tk畫圖大集合"
window.title(title)

print("建立畫布")
width = W - 20
height = H - 20
canvas1 = tk.Canvas(window, bg="pink", width=width, height=height)
canvas1.pack()

canvas1.create_line(0, H // 2, W, H // 2)
canvas1.create_line(W // 2, 0, W // 2, H)

# create_line 繪製直線 (x1, y1)-(x2, y2)
x1, y1, x2, y2 = 20, 20, 120, 20
canvas1.create_line(x1, y1, x2, y2)
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="gray50")
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="red", dash=(4, 4))
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, width=5)
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, width=10, fill="blue")
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, dash=(10, 2, 2, 2))
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="#FF0000")

""" 直線連線
x1, y1, x2, y2, x3, y3, x1, y1 = 30,30,500,30,265,100,30,30
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=5,joinstyle=tk.ROUND)
x1, y1, x2, y2, x3, y3, x1, y1 = 30,130,500,130,265,200,30,130
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=5,joinstyle=tk.BEVEL)
x1, y1, x2, y2, x3, y3, x1, y1 = 30,230,500,230,265,300,30,230
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=5,joinstyle=tk.MITER)

x1, y1, x2, y2 = 230,30,500,30
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.BUTT)
x1, y1, x2, y2 = 230,130,500,130
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.ROUND)
x1, y1, x2, y2 = 230,230,500,230
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.PROJECTING)

x1, y1, x2, y2 = 230,30,500,30
canvas1.create_line(x1, y1, x2, y2,width=5,stipple="gray25")
x1, y1, x2, y2 = 230,130,500,130
canvas1.create_line(x1, y1, x2, y2,width=5,stipple="questhead")
x1, y1, x2, y2 = 30,230,500,230
canvas1.create_line(x1, y1, x2, y2,width=5,stipple="info")
"""
# create_rectangle 繪製矩形
x_st, y_st, x_sp, y_sp = 150, 20, 250, 60
dy = 55
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp)  # 無參數, 空心1點, 黑線
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, dash=(4, 4))  # 虛線
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, outline="red")  # 外框線紅色
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill="red")  # 實心
# canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill='#FF0000')#實心
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill="green", outline="red", width=5)
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(
    x_st, y_st, x_sp, y_sp, fill="blue", width=6, dash=(4, 2, 1, 1), outline="red"
)

# create_oval 繪製圓形、橢圓

# 圓形
cx, cy = 300, 40
radius = 30
dy = 60

canvas1.create_oval(cx - radius, cy - radius, cx + radius, cy + radius)  # 無參數, 空心1點, 黑線
cx, cy = cx, cy + dy
canvas1.create_oval(
    cx - radius, cy - radius, cx + radius, cy + radius, tags="oval"
)  # 多了tags參數
cx, cy = cx, cy + dy
canvas1.create_oval(
    cx - radius, cy - radius, cx + radius, cy + radius, fill="green"
)  # 實心圓, 黑色外框1點
cx, cy = cx, cy + dy
canvas1.create_oval(
    cx - radius, cy - radius, cx + radius, cy + radius, outline="red"
)  # 外框線紅色
cx, cy = cx, cy + dy

# 橢圓形
dy = 70
x_st, y_st, x_sp, y_sp = 270, 260, 420, 320  # 左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp)  # 橢圓, 無fill, 黑色外框1點

x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy  # 左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp, fill="aqua", outline="blue", width=5)

# create_arc 繪製圓弧
# 圓之左上-右下
x_st, y_st, x_sp, y_sp = 400, 0, 400 + 100, 0 + 100  # 左上-右下

start, extent = 45, 180  # 起始45度, 掃描180度
canvas1.create_arc(
    (x_st, y_st, x_sp, y_sp),
    fill="red",
    start=start,
    extent=extent,
    style=tk.CHORD,
    outline="green",
    width=5,
)
"""
style = tk.PIESLICE  # 派形
style = tk.ARC  # 僅弧線
style = tk.CHORD  # 弓形
"""

diameter = 100
dx = 80
dy = 80
x_st, y_st, x_sp, y_sp = 350, 120, 350 + diameter, 120 + diameter  # 左上-右下
canvas1.create_arc(x_st, y_st, x_sp, y_sp)  # 無參數 空心1點黑線0~90度
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp

canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.ARC)  # 僅弧線
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.PIESLICE)  # 派形
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.CHORD)  # 弓形

x_st, y_st, x_sp, y_sp = 400, 120 + dy, 400 + diameter, 120 + diameter + dy  # 左上-右下
canvas1.create_arc(x_st, y_st, x_sp, y_sp, extent=180, fill="yellow")
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, extent=180, style=tk.ARC, width=5)

# create_polygon 繪製多邊形
dx = 400
dy = 280
canvas1.create_polygon(
    40 + dx,
    40 + dy,
    60 + dx,
    20 + dy,
    80 + dx,
    40 + dy,
    80 + dx,
    80 + dy,
    40 + dx,
    80 + dy,
)  # 無參數, 黑色實心
# 空心 外框線
canvas1.create_polygon(
    100 + dx,
    40 + dy,
    120 + dx,
    20 + dy,
    140 + dx,
    40 + dy,
    140 + dx,
    80 + dy,
    100 + dx,
    80 + dy,
    fill="",
    outline="red",
)
# 實心
canvas1.create_polygon(
    160 + dx, 80 + dy, 200 + dx, 80 + dy, 180 + dx, 20 + dy, fill="green"
)
# 實心 外框線
canvas1.create_polygon(
    220 + dx,
    80 + dy,
    260 + dx,
    80 + dy,
    240 + dx,
    20 + dy,
    fill="blue",
    outline="yellow",
    width=5,
)


# create_text 繪製文字

x_st, y_st = W // 4, H // 2
dy = 40
canvas1.create_text(x_st, y_st, text="歡迎來到美國1")  # 無參數
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國2", fill="red", width=20)
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國3", anchor="nw")
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="Welcome to the United States", fill="blue")
x_st, y_st = x_st, y_st + dy
canvas1.create_text(
    x_st,
    y_st,
    text="Welcome to the United States",
    fill="blue",
    font=("Old English Text MT", 20),
)
x_st, y_st = x_st, y_st + dy
canvas1.create_text(
    x_st,
    y_st,
    text="Welcome to the United States",
    fill="blue",
    font=("華康新綜藝體 Std W7", 20),
)
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國4", fill="blue", font=("華康新綜藝體 Std W7", 20))
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國5", font=("Arial", 36))

x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st+2, y_st+2,						# 使用create_text方法在座標（302，77）處繪制文字
		text = '陰影效果'					# 所繪制文字的內容
		,fill = 'gray')						# 所繪制文字的彩色為灰色
canvas1.create_text(x_st, y_st,
		text = '陰影效果',
		fill = 'blue')

print("------------------------------------------------------------")  # 60個

print('畫派圖')
print(H)
# create_arc 繪製圓弧
# 圓之左上-右下
x_st, y_st, x_sp, y_sp = 500, H//2+20, 750, H//2+20+150  # 左上-右下

canvas1.create_arc(x_st, y_st, x_sp, y_sp, 					# 使用create_arc繪制圓弧
		start=0, extent=240, 					# 設定圓弧的起止角度
		fill="pink")						# 設定圓弧填充彩色
canvas1.create_arc(x_st+3, y_st+3, x_sp, y_sp, 
		start=241, extent=118, 
		fill="red")

canvas1.create_rectangle(x_st-10, y_st-10, x_sp+10, y_sp+10,					# 使用create_rectangle繪制一個矩形
		width=5)						# 設定矩形線寬為5個像素

xWidth = 350
yHeight = 220
x_st, y_st, x_sp, y_sp = 470, H//2+20+200-50, 750, H//2+20+150+200  # 左上-右下

for i in range(20):
    canvas1.create_oval(x_st+10+i*5, y_st+10+i*5, x_st+xWidth-10-i*5, y_st+yHeight-10-i*5)

print("------------------------------------------------------------")  # 60個

xWidth = 400
yHeight = 250

x_center, y_center, r = 770, 260, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas1.create_line(x[i],y[i],x[j],y[j])

print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個

# Display a rectangle
def displayRect():
    create_rectangle(10, 10, 190, 90, tags = "rect")

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
window.geometry("800x800")
title = "tk畫圖大集合"
window.title(title)

canvas = tk.Canvas(window, width = 400, height = 400, bg = "white")
canvas.pack()

btRectangle = tk.Button(window, text = "Rectangle", command = displayRect)
btOval = tk.Button(window, text = "Oval", command = displayOval)
btArc = tk.Button(window, text = "Arc", command = displayArc)
btPolygon = tk.Button(window, text = "Polygon", command = displayPolygon)
btLine = tk.Button(window, text = "Line", command = displayLine)
btString = tk.Button(window, text = "String", command = displayString)
btClear = tk.Button(window, text = "Clear", command = clearCanvas)

btRectangle.pack()
btOval.pack()
btArc.pack()
btPolygon.pack()
btLine.pack()
btString.pack()
btClear.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""

id = canvas1.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas1.coords(id)
print(ballPos)


"""


"""


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


"""



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

canvas1.create_line(100,100,500,100)
canvas1.create_line(100,125,500,125,width=5)
canvas1.create_line(100,150,500,150,width=10,fill='blue')
canvas1.create_line(100,175,500,175,dash=(10,2,2,2))

print("------------------------------------------------------------")  # 60個

canvas1.create_line(30,30,500,30,265,100,30,30,
                   width=20,joinstyle=ROUND)
canvas1.create_line(30,130,500,130,265,200,30,130,
                   width=20,joinstyle=BEVEL)
canvas1.create_line(30,230,500,230,265,300,30,230,
                   width=20,joinstyle=MITER)

print("------------------------------------------------------------")  # 60個

canvas1.create_line(30,30,500,30,width=10,capstyle=BUTT)
canvas1.create_line(30,130,500,130,width=10,capstyle=ROUND)
canvas1.create_line(30,230,500,230,width=10,capstyle=PROJECTING)

canvas1.create_line(30,30,500,30,width=10,stipple="gray25")
canvas1.create_line(30,130,500,130,width=40,stipple="questhead")
canvas1.create_line(30,230,500,230,width=10,stipple="info")

print("------------------------------------------------------------")  # 60個

print('製作格線')
for i in range(19):
    canvas1.create_line(10, 10+10*i, xWidth - 10, 10+10*i)
    canvas1.create_line(10+10*i, 10, 10+10*i, yHeight - 10)
        
print("------------------------------------------------------------")  # 60個

for i in range(50):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = random.randint(1, 640), random.randint(1, 480)
    x2, y2 = random.randint(1, 640), random.randint(1, 480)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas1.create_rectangle(x1, y1, x2, y2)

print("------------------------------------------------------------")  # 60個

canvas1.create_rectangle(10, 10, 120, 60, fill='red')
canvas1.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
canvas1.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')

print("------------------------------------------------------------")  # 60個

for i in range(20):
    canvas1.create_rectangle(10 + i * 5, 10 + i * 5, xWidth - 10 - i * 5, yHeight - 10 - i * 5)
        
print("------------------------------------------------------------")  # 60個

# 以下以圓形為基礎
canvas1.create_arc(10, 10, 110, 110, extent=45, style=ARC)
canvas1.create_arc(210, 10, 310, 110, extent=90, style=ARC)
canvas1.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
canvas1.create_arc(10, 110, 110, 210, extent=270, style=ARC)
canvas1.create_arc(210, 110, 310, 210, extent=359, style=ARC, width=5)
# 以下以橢圓形為基礎
canvas1.create_arc(10, 250, 310, 350, extent=90, style=ARC, start=90)
canvas1.create_arc(320, 250, 620, 350, extent=180, style=ARC)
canvas1.create_arc(10, 360, 310, 460, extent=270, style=ARC, outline='blue')
canvas1.create_arc(320, 360, 620, 460, extent=359, style=ARC)

print("------------------------------------------------------------")  # 60個

# 以下以圓形為基礎
canvas1.create_arc(10, 10, 110, 110, extent=180, style=ARC)
canvas1.create_arc(210, 10, 310, 110, extent=180, style=CHORD)
canvas1.create_arc(410, 10, 510, 110, start=30, extent=120, style=PIESLICE)

print("------------------------------------------------------------")  # 60個

for i in range(20):
    canvas1.create_oval(10+i*5, 10+i*5, xWidth-10-i*5, yHeight-10-i*5)
        
print("------------------------------------------------------------")  # 60個

# 以下是圓形
canvas1.create_oval(10, 10, 110, 110)
canvas1.create_oval(150, 10, 300, 160, fill='yellow')
# 以下是橢圓形
canvas1.create_oval(10, 200, 310, 350)
canvas1.create_oval(350, 200, 550, 300, fill='aqua', outline='blue', width=5)

print("------------------------------------------------------------")  # 60個

canvas1.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
canvas1.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
canvas1.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
canvas1.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')

print("------------------------------------------------------------")  # 60個

canvas1.create_text(200, 50, text='Welcome to the United States')
canvas1.create_text(200, 80, text='Welcome to the United States', fill='blue')
canvas1.create_text(300, 120, text='Welcome to the United States', fill='blue',
                   font=('Old English Text MT',20))
canvas1.create_text(300, 160, text='Welcome to the United States', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
canvas1.create_text(300, 200, text='歡迎來到美國', fill='blue',
                   font=('華康新綜藝體 Std W7',20))

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("800x800")
title = "tk畫圖大集合"
window.title(title)

print("------------------------------------------------------------")  # 60個

color = "#FF0000"
canvas = tk.Canvas(window, width=500, height=150, bg=color)
canvas.pack()

def drawCanvas():
    print("draw")
    x_st = 0
    y_st = 0
    radius = 50
    for i in range(0, 10):
        canvas.create_oval(
            x_st + 50 * i, y_st, x_st + 50 * i + radius, y_st + radius, tags="oval"
        )
        canvas.create_oval(
            x_st + 50 * i, y_st + 75, x_st + 50 * i + radius, y_st + 75 + radius
        )


def deleteCanvas():
    print("delete")
    canvas.delete("oval")
    canvas.delete("rect", "oval", "line")


button2 = tk.Button(window, text="在 Canvas 上畫一些東西", command=drawCanvas)
button2.pack()

button3 = tk.Button(window, text="刪除 Canvas 上畫的部分東西", command=deleteCanvas)
button3.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

   
class FigureCanvas(tk.Canvas):
    def __init__(self, container, figureType, filled = False, 
                 width = 100, height = 100):
        super().__init__(container, 
                         width = width, height = height)
        self.__figureType = figureType
        self.__filled = filled
        self.drawFigure()
      
    def getFigureType(self):
        return self.__figureType 
        
    def getFilled(self):
        return self.__filled 
          
    def setFigureType(self, figureType):
        self.__figureType = figureType
        self.drawFigure()
        
    def setFilled(self, filled):
        self.__filled = filled
        self.drawFigure()
                
    def drawFigure(self):
        if self.__figureType == "line":
            self.line()
        elif self.__figureType == "rectangle":    
            self.rectangle()
        elif self.__figureType == "oval":
            self.oval()
        elif self.__figureType == "arc":    
            self.arc()
        
    def line(self):
        width = int(self["width"])
        height = int(self["height"])
        self.create_line(10, 10, width - 10, height - 10)
        self.create_line(width - 10, 10, 10, height - 10)

    def rectangle(self):
        width = int(self["width"])
        height = int(self["height"])
        if self.__filled:
            self.create_rectangle(10, 10, width - 10, height - 10, 
                              fill = "red")
        else:
            self.create_rectangle(10, 10, width - 10, height - 10)
            
    def oval(self):
        width = int(self["width"])
        height = int(self["height"])
        if self.__filled:
            self.create_oval(10, 10, width - 10, height - 10, 
                             fill = "red")
        else:
            self.create_oval(10, 10, width - 10, height - 10)

    def arc(self):
        width = int(self["width"])
        height = int(self["height"])
        if self.__filled:
            self.create_arc(10, 10, width - 10, height - 10, 
                        start = 0, extent = 145, fill = "red")
        else:
            self.create_arc(10, 10, width - 10, height - 10, 
                        start = 0, extent = 145)


window = tk.Tk() # Create a window
window.title("Display Figures") # Set title

figure1 = FigureCanvas(window, "line", width = 100, height = 100) 
figure1.grid(row = 1, column = 1)
figure2 = FigureCanvas(window, "rectangle", False, 100, 100) 
figure2.grid(row = 1, column = 2)
figure3 = FigureCanvas(window, "oval", False, 100, 100) 
figure3.grid(row = 1, column = 3)
figure4 = FigureCanvas(window, "arc", False, 100, 100) 
figure4.grid(row = 1, column = 4)
figure5 = FigureCanvas(window, "rectangle", True, 100, 100) 
figure5.grid(row = 1, column = 5)
figure6 = FigureCanvas(window, "oval", True, 100, 100) 
figure6.grid(row = 1, column = 6)
figure7 = FigureCanvas(window, "arc", True, 100, 100) 
figure7.grid(row = 1, column = 7)

window.mainloop()

