import tkinter as tk
from tkinter import Tk, Canvas, NW

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

width = 600
height = 400
canvas = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas.pack()

def mouseDoubleClick1(event):
    print('雙擊左鍵', end = ' ')

def mouseDoubleClick2(event):
    print('雙擊中鍵', end = ' ')

def mouseDoubleClick3(event):
    print('雙擊右鍵', end = ' ')

def mouseDoubleClick4(event):
    print('?????', end = ' ')

def mouse_down1(event):
    print('你按了滑鼠左鍵', end = ' ')
    print("canvas位置 : ", event.x, event.y, end = ' ')
    print("視窗位置 : ", event.x_root, event.y_root, end = ' ')
    print("按鍵 : ", event.num, end = ' ')
    
    '''
    canvas.delete("oval")
    global radius
    if radius < 100:
        radius += 2
    canvas.create_oval(100 - radius, 100 - radius, 
                       100 + radius, 100 + radius, tags = "oval")
    '''

def mouse_down2(event):
    print('你按了滑鼠中鍵', end = ' ')
    
def mouse_down3(event):
    print('你按了滑鼠右鍵', end = ' ')
    '''
    canvas.delete("oval")
    global radius
    if radius > 2:
        radius -= 2
    canvas.create_oval(100 - radius, 100 - radius, 
                       100 + radius, 100 + radius, tags = "oval")
    '''

def mouse_down4(event):
    print('上一頁', end = ' ')
    
def mouse_down5(event):
    print('下一頁', end = ' ')

def mouse_move1(event):
    print('m1', end = ' ')

def mouse_move2(event):
    print('m2', end = ' ')

def mouse_move3(event):
    print('m3', end = ' ')

def mouse_move4(event):
    print('m4', end = ' ')

def mouse_move5(event):
    print('m5', end = ' ')

def mouse_up1(event):
    print('up1', end = ' ')

def mouse_up2(event):
    print('up2', end = ' ')

def mouse_up3(event):
    print('up3', end = ' ')

def mouse_up4(event):
    print('up4', end = ' ')

def mouse_up5(event):
    print('up5', end = ' ')

def mouse_motion(event):
    #print('滑鼠位置: (%s, %s)' % (event.x, event.y), end = ' ')
    window.title('滑鼠位置: (%s, %s)' % (event.x, event.y))
    return

def mouse_wheel_event(event):
    if event.delta > 0:
        print('上', end = ' ')
    else:
        print('下', end = ' ')

def processKeyEvent(event):
    print("keysym? ", event.keysym, end = ' ')
    print("char? ", event.char, end = ' ')
    print("keycode? ", event.keycode)

#Mouse Double Click
canvas.bind("<Double-1>", mouseDoubleClick1)    #雙擊左鍵
canvas.bind("<Double-2>", mouseDoubleClick2)    #雙擊中鍵
canvas.bind("<Double-3>", mouseDoubleClick3)    #雙擊右鍵
canvas.bind("<Double-4>", mouseDoubleClick4)    #unknown

#Mouse Down    
canvas.bind("<Button-1>", mouse_down1)  #滑鼠左鍵 單擊
canvas.bind("<Button-2>", mouse_down2)  #滑鼠中鍵 單擊
canvas.bind("<Button-3>", mouse_down3)  #滑鼠右鍵 單擊
canvas.bind("<Button-4>", mouse_down4)  #滑鼠上一頁 單擊
canvas.bind("<Button-5>", mouse_down5)  #滑鼠下一頁 單擊

#Mouse Move
canvas.bind('<Button1-Motion>', mouse_move1)    #滑鼠左鍵 移動
canvas.bind('<Button2-Motion>', mouse_move2)    #滑鼠中鍵 移動
canvas.bind('<Button3-Motion>', mouse_move3)    #滑鼠右鍵 移動
canvas.bind('<Button4-Motion>', mouse_move4)    #滑鼠上一頁 移動
canvas.bind('<Button5-Motion>', mouse_move5)    #滑鼠下一頁 移動

#Mouse Up
canvas.bind('<ButtonRelease-1>', mouse_up1) #滑鼠左鍵 放開
canvas.bind('<ButtonRelease-2>', mouse_up2) #滑鼠中鍵 放開
canvas.bind('<ButtonRelease-3>', mouse_up3) #滑鼠右鍵 放開
canvas.bind('<ButtonRelease-4>', mouse_up4) #滑鼠上一頁 放開
canvas.bind('<ButtonRelease-5>', mouse_up5) #滑鼠下一頁 放開

canvas.bind('<Motion>', mouse_motion)  #滑鼠鼠標位置
canvas.bind('<MouseWheel>', mouse_wheel_event)  #滾輪事件

#鍵盤事件
canvas.bind("<Key>", processKeyEvent)
canvas.focus_set()


'''
canvas.tag_bind('<Button-1>', mouse_down)
canvas.tag_bind('<Button1-Motion>', mouse_move)
canvas.tag_bind('<ButtonRelease-1>', mouse_up)
'''

def moveCanvas():
    print('move')
    #canvas.move(0, -1) TBD
    red = 255
    green = 128
    blue = 0
    color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg = color)


button1 = tk.Button(window, text = '移動', command = moveCanvas)
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

