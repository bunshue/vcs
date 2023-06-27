import tkinter as tk
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk

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
title = "這是主視窗"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

tk.Label(text = 'Canvas 測試').pack()

color = "#FF0000"
canvas1 = tk.Canvas(window, width = 300, height = 50, bg=color)
canvas1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def drawABar(x, percent, color, title):
    canvas2.create_line(0, height - 10, width, height - 10)
    canvas2.create_rectangle(x, (1 - percent) * (height - 30), x + width / 4.3 - 5, height - 10, fill = color)
    canvas2.create_text((x + x + width / 4.3 - 5) / 2, (1 - percent) * (height - 30) - 10, text = title)

width = 400
height = 200
canvas2 = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas2.pack()

x = 10
drawABar(x, 0.4, "red", "Project -- 20%")
  
x += width / 4.3 - 5 + 10  
drawABar(x, 0.1, "blue", "Quizzes -- 10%")

x += width / 4.3 - 5 + 10  
drawABar(x, 0.3, "green", "Midterm -- 30%")

x += width / 4.3 - 5 + 10  
drawABar(x, 0.4, "orange", "Final -- 40%")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

'''
def mouse_down(self, event):
    lastx = event.x
    lasty = event.y
    origx = event.x
    origy = event.y
    canvas.tag_raise(item_id)

def mouse_move(self, event):
    canvas.move(item_id,event.x - lastx, event.y - lasty)
    lastx = event.x
    lasty = event.y

def mouse_up(self, event):
    i = nearestindex(event.x)
    if i >= array.getsize():
        i = array.getsize() - 1
    if i < 0:
        i = 0
    other = array.items[i]
    here = index
    array.items[here], array.items[i] = other, self
    index = i
    x1, y1, x2, y2 = position()
    canvas.coords(item_id, (x1, y1, x2, y2))
    other.setindex(here)
'''

width = 400
height = 200
canvas3 = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas3.pack()

#直線
canvas3.create_line(0, 0, 100, 100)
canvas3.create_line(100, 100, 0, 0)
canvas3.create_line(0, 100, 100, 0)
canvas3.create_line(0, 0, 400, 200, fill = "red", dash = (4, 4))

#矩形
x1 = 150
y1 = 100
x2 = x1 + 100
y2 = y1 + 100
canvas3.create_rectangle(x1, y1, x2, y2, fill = 'red', outline = 'black', width = 1)
x1 = 25
y1 = 125
x2 = x1 + 100
y2 = y1 + 50
canvas3.create_rectangle(x1, y1, x2, y2, fill = "blue")

#圓形
cx = 50
cy = 50
radius = 50
canvas3.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, tags = "oval")

def mouseClick1(event):
    print('mouseClick1')
    '''
    canvas.delete("oval")
    global radius
    if radius < 100:
        radius += 2
    canvas.create_oval(100 - radius, 100 - radius, 
                       100 + radius, 100 + radius, tags = "oval")
    '''

def mouseClick2(event):
    print('你按了滑鼠中鍵')
    
def mouseClick3(event):
    print('mouseClick3')
    '''
    canvas.delete("oval")
    global radius
    if radius > 2:
        radius -= 2
    canvas.create_oval(100 - radius, 100 - radius, 
                       100 + radius, 100 + radius, tags = "oval")
    '''

def mouseClick4(event):
    print('上一頁')
    
def mouseClick5(event):
    print('下一頁')

def mouseDoubleClick1(event):
    print('雙擊左鍵')

def motion(event):
    #print("Mouse position: (%s %s)" % (event.x, event.y))
    window.title('Mouse position: (%s, %s)' % (event.x, event.y))
    return
    

canvas3.bind("<Button-1>", mouseClick1)
canvas3.bind("<Button-2>", mouseClick2)
canvas3.bind("<Button-3>", mouseClick3)
canvas3.bind("<Button-4>", mouseClick4)
canvas3.bind("<Button-5>", mouseClick5)
canvas3.bind("<Double-1>", mouseDoubleClick1)
canvas3.bind('<Motion>',motion)


'''
canvas.tag_bind('<Button-1>', mouse_down)
canvas.tag_bind('<Button1-Motion>', mouse_move)
canvas.tag_bind('<ButtonRelease-1>', mouse_up)
'''

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)
if image.mode != "RGB":
    print('圖片非RGB模式, 要轉成RGB格式')
    image = image.convert("RGB")	#轉換成RGB圖像


box = 50, 50, 50 + 100, 50 + 100
tile = ImageTk.PhotoImage(image.crop(box))
x = 270
y = 50
canvas3.create_image(x, y, image = tile, anchor = NW)


'''
self.bitmap = c.create_bitmap(width//2, height//2,
                bitmap=bitmap,
                foreground='blue')
'''

def moveCanvas():
    print('move')
    #canvas3.move(0, -1) TBD
    red = 255
    green = 128
    blue = 0
    color = "#%02x%02x%02x" % (red, green, blue)
    canvas3.config(bg = color)


button1 = tk.Button(window, text = '移動', command = moveCanvas)
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

