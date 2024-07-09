"""
tk 之 Canvas 畫圖

無 canvas.create_image()

"""
import sys
import math
import random
import tkinter as tk

print("------------------------------------------------------------")  # 60個

W, H = 1200, 900

window = tk.Tk()
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, 0, 0))
window.title("tk畫圖大集合 1")

print("建立畫布")
width = W - 20
height = H - 20
canvas1 = tk.Canvas(window, bg="pink", width=width, height=height-30)
canvas1.pack()

#基準線
canvas1.create_line(0, H // 3 * 1, W, H // 3 * 1)
canvas1.create_line(0, H // 3 * 2, W, H // 3 * 2)
canvas1.create_line(W // 3 * 1, 0, W // 3 * 1, H)
canvas1.create_line(W // 3 * 2, 0, W // 3 * 2, H)

# create_line 繪製直線 (x1, y1)-(x2, y2)
x1, y1, x2, y2 = 20, 20, 120, 20
canvas1.create_line(x1, y1, x2, y2) #零點黑線
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="gray50")
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="red", dash=(4, 4))
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, width=5)#粗線
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, width=10, fill="blue")#顏色線
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, dash=(10, 2, 2, 2)) #點線
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="#FF0000")

""" 直線連線

#多點連線
x1, y1, x2, y2, x3, y3, x1, y1 = 30,30,500,30,265,100,30,30
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=10,joinstyle=tk.ROUND)
#多點連線
x1, y1, x2, y2, x3, y3, x1, y1 = 30,130,500,130,265,200,30,130
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=10,joinstyle=tk.BEVEL)
#多點連線
x1, y1, x2, y2, x3, y3, x1, y1 = 30,230,500,230,265,300,30,230
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=10,joinstyle=tk.MITER)

#直線 線條樣式
x1, y1, x2, y2 = 230,30,500,30
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.BUTT)
x1, y1, x2, y2 = 230,130,500,130
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.ROUND)
x1, y1, x2, y2 = 230,230,500,230
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.PROJECTING)

#直線 線條樣式
x1, y1, x2, y2 = 230,30,500,30
canvas1.create_line(x1, y1, x2, y2,width=20,stipple="gray25")
x1, y1, x2, y2 = 230,130,500,130
canvas1.create_line(x1, y1, x2, y2,width=20,stipple="questhead")
x1, y1, x2, y2 = 30,230,500,230
canvas1.create_line(x1, y1, x2, y2,width=20,stipple="info")
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
canvas1.create_oval(cx - radius, cy - radius, cx + radius, cy + radius)
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

dx = 110
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.ARC, width=5, start=0, extent=180)

x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.ARC, width=5, start=90, extent=180, outline='blue')

x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.ARC, extent=180)

x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.CHORD, extent=180)

x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.PIESLICE, start=30, extent=120)

x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, start = 0, extent = 90, width = 5, fill = "red")

# create_polygon 繪製多邊形
x_st = 400
y_st = 280
canvas1.create_polygon(
    x_st+40,
    y_st+40,
    x_st+60,
    y_st+20,
    x_st+80,
    y_st+40,
    x_st+80,
    y_st+80,
    x_st+40,
    y_st+80,
)  # 無參數, 黑色實心

# 空心 外框線
canvas1.create_polygon(
    x_st+100,
    y_st+40,
    x_st+120,
    y_st+20,
    x_st+140,
    y_st+40,
    x_st+140,
    y_st+80,
    x_st+100,
    y_st+80,
    fill="",
    outline="red",
)

# 實心
canvas1.create_polygon(
    x_st+160, y_st+80, x_st+200, y_st+80, x_st+180, y_st+20, fill="green"
)

# 實心 外框線
canvas1.create_polygon(
    x_st+220,
    y_st+80,
    x_st+260,
    y_st+80,
    x_st+240,
    y_st+20,
    fill="blue",
    outline="yellow",
    width=5,
)

# create_text 繪製文字
x_st, y_st = 200, H // 2+50
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

xWidth = 400
yHeight = 250

x_center, y_center, r = 1080, 500, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas1.create_line(x[i],y[i],x[j],y[j])

print("------------------------------------------------------------")  # 60個

print('製作格線 NXN')

x_st = 1080
y_st = 305
w = 10
h = 10
COLUMN = 10
ROW = 10
W = (COLUMN-1)*w
H = (ROW-1)*h

for i in range(COLUMN):
    #垂直線
    canvas1.create_line(x_st+h*i, y_st, x_st+h*i, y_st+H)

for i in range(ROW):
    #水平線
    canvas1.create_line(x_st, y_st+h*i, x_st+W, y_st+h*i)
        
print("------------------------------------------------------------")  # 60個

xWidth = 350
yHeight = 200
#x_st, y_st, x_sp, y_sp = 400, H//2, 400+280, H//2+200  # 左上-右下
x_st, y_st = 400+20, 600+20

for i in range(8):
    # 無參數, 空心1點, 黑線
    obj = canvas1.create_rectangle(x_st+i*10, y_st+i*10, x_st+xWidth-i*10, y_st+yHeight-i*10)
    obj_coord = canvas1.coords(obj)
    print("此物件座標 :", obj_coord)

print("------------------------------------------------------------")  # 60個

x_st, y_st = 800+20, 600+20

for i in range(30):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = random.randint(1, 320), random.randint(1, 200)
    x2, y2 = random.randint(1, 320), random.randint(1, 200)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas1.create_rectangle(x_st+x1, y_st+y1, x_st+x2, y_st+y2)

print("------------------------------------------------------------")  # 60個

# 使用 tags

def drawCanvas():
    print("在 Canvas 上畫一些東西")
    x_st = 400
    y_st = 450
    radius = 50
    for i in range(0, 8):
        canvas1.create_oval(
            x_st + 50 * i, y_st, x_st + 50 * i + radius, y_st + radius, tags="tags_example"
        )
        canvas1.create_oval(
            x_st + 50 * i, y_st + 75, x_st + 50 * i + radius, y_st + 75 + radius
        )

def deleteCanvas():
    print("刪除 Canvas 上畫的部分東西")
    canvas1.delete("tags_example")

button2 = tk.Button(window, text="在 Canvas 上畫一些東西", command=drawCanvas)
button2.pack(side = tk.LEFT)

button3 = tk.Button(window, text="刪除 Canvas 上畫的部分東西", command=deleteCanvas)
button3.pack(side = tk.LEFT)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""

color = "#FF0000"
canvas = tk.Canvas(window, width=500, height=150, bg=color)
canvas.pack()



canvas1.create_text(60, 40, text = "Hi, I am a string", font = "Times 30 bold underline")

canvas1.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue")



# create_arc 繪製圓弧
# 圓之左上-右下
x_st, y_st, x_sp, y_sp = 500, H//2+20, 750, H//2+20+150  # 左上-右下

canvas1.create_arc(x_st, y_st, x_sp, y_sp, # 使用create_arc繪制圓弧
		start=0, extent=240, # 設定圓弧的起止角度
		fill="pink")	# 設定圓弧填充彩色
canvas1.create_arc(x_st+3, y_st+3, x_sp, y_sp, 
		start=241, extent=118, 
		fill="red")




"""





