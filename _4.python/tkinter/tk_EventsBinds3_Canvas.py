'''
綁定鍵盤滑鼠事件 Canvas
'''
import tkinter as tk

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
title = '綁定鍵盤滑鼠事件 Canvas'
window.title(title)

width = 600
height = 400
cccc = tk.Canvas(window, bg = "pink", width = width, height = height)
cccc.pack()

flag_mouse_down = False

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
    global flag_mouse_down
    flag_mouse_down = True
    '''
    print("在控件位置 : ", event.x, event.y, end = ' ')
    print("視窗位置 : ", event.x_root, event.y_root, end = ' ')
    print("按鍵 : ", event.num, end = ' ')
    '''
    global radius
    cccc.delete("oval")
    if radius < 100:
        radius += 2
    cccc.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, tags = "oval")

def mouse_down2(event):
    print('你按了滑鼠中鍵', end = ' ')
    
def mouse_down3(event):
    print('你按了滑鼠右鍵', end = ' ')
    global radius
    cccc.delete("oval")
    if radius > 2:
        radius -= 2
    cccc.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, tags = "oval")

def mouse_down4(event):
    print('上一頁', end = ' ')
    
def mouse_down5(event):
    print('下一頁', end = ' ')

def mouse_move1(event):
    #print('m1', end = ' ')
    global flag_mouse_down
    if flag_mouse_down == True:
        #用鼠標在canvas上畫圖
        x = event.x
        y = event.y
        brush_size = 4
        cccc.create_oval((x - brush_size / 2,y - brush_size / 2, x + brush_size / 2,y + brush_size / 2), fill = 'black')
        return

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
    global flag_mouse_down
    flag_mouse_down = False

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
    #window.title('滑鼠位置: (%s, %s)' % (event.x, event.y))
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
cccc.bind("<Double-1>", mouseDoubleClick1)    #雙擊左鍵
cccc.bind("<Double-2>", mouseDoubleClick2)    #雙擊中鍵
cccc.bind("<Double-3>", mouseDoubleClick3)    #雙擊右鍵
cccc.bind("<Double-4>", mouseDoubleClick4)    #unknown

#Mouse Down
cccc.bind("<Button-1>", mouse_down1)  #滑鼠左鍵 單擊
cccc.bind("<Button-2>", mouse_down2)  #滑鼠中鍵 單擊
cccc.bind("<Button-3>", mouse_down3)  #滑鼠右鍵 單擊
cccc.bind("<Button-4>", mouse_down4)  #滑鼠上一頁 單擊
cccc.bind("<Button-5>", mouse_down5)  #滑鼠下一頁 單擊

#Mouse Move
cccc.bind('<Button1-Motion>', mouse_move1)    #滑鼠左鍵 移動
cccc.bind('<Button2-Motion>', mouse_move2)    #滑鼠中鍵 移動
cccc.bind('<Button3-Motion>', mouse_move3)    #滑鼠右鍵 移動
cccc.bind('<Button4-Motion>', mouse_move4)    #滑鼠上一頁 移動
cccc.bind('<Button5-Motion>', mouse_move5)    #滑鼠下一頁 移動

#Mouse Up
cccc.bind('<ButtonRelease-1>', mouse_up1) #滑鼠左鍵 放開
cccc.bind('<ButtonRelease-2>', mouse_up2) #滑鼠中鍵 放開
cccc.bind('<ButtonRelease-3>', mouse_up3) #滑鼠右鍵 放開
cccc.bind('<ButtonRelease-4>', mouse_up4) #滑鼠上一頁 放開
cccc.bind('<ButtonRelease-5>', mouse_up5) #滑鼠下一頁 放開

cccc.bind('<Motion>', mouse_motion)  #滑鼠鼠標位置
cccc.bind('<MouseWheel>', mouse_wheel_event)  #滾輪事件

#鍵盤事件
cccc.bind("<Key>", processKeyEvent)
cccc.focus_set()

print('左鍵變大 右鍵變小')

radius = 50
cccc.create_oval(100 - radius, 100 - radius, 100 + radius, 100 + radius, tags = "oval")

window.mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *
def callback(event):                        # 事件處理程式
    print("Clicked at", event.x, event.y)   # 列印座標
    
root = Tk()
root.title("ch40_20_1")
canvas = Canvas(root,width=300,height=180)
canvas.bind("<Button-1>",callback)           # 按一下綁定callback
canvas.pack()

root.mainloop()


print("------------------------------------------------------------")  # 60個

"""
使用tkinter创建GUI
- 使用画布绘图
- 处理鼠标事件

"""
import tkinter

def mouse_evt_handler(evt=None):
    row = round((evt.y - 20) / 40)
    col = round((evt.x - 20) / 40)
    pos_x = 40 * col
    pos_y = 40 * row
    canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')

top = tkinter.Tk()
# 设置窗口尺寸
top.geometry('620x620')
# 设置窗口标题
top.title('五子棋')
# 设置窗口大小不可改变
top.resizable(False, False)
# 设置窗口置顶
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.bind('<Button-1>', mouse_evt_handler)
canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
for index in range(15):
    canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
    canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
canvas.pack()
tkinter.mainloop()

# 请思考如何用面向对象的编程思想对上面的代码进行封装

print('------------------------------------------------------------')	#60個



from tkinter import *

def circleIncrease(event):
    global r
    canvas.delete("myCircle")
    if r < 200:
        r += 5
    canvas.create_oval(200-r,200-r,200+r,200+r,fill='yellow',tag="myCircle")
    
def circleDecrease(event):
    global r
    canvas.delete("myCircle")
    if r > 5:
        r -= 5
    canvas.create_oval(200-r,200-r,200+r,200+r,fill='yellow',tag="myCircle")
    
tk = Tk()
canvas= Canvas(tk, width=400, height=400)
canvas.pack()

r = 100
canvas.create_oval(200-r,200-r,200+r,200+r,fill='yellow',tag="myCircle")
canvas.bind('<Button-1>', circleIncrease)
canvas.bind('<Button-3>', circleDecrease)

mainloop()

print("------------------------------------------------------------")  # 60個


print("01-TkUI11Canvas")

import tkinter as tk

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

win = tk.Tk()

c1 = tk.Canvas(win, 
           width=1000, 
           height=410)

coord = 10, 10, 100, 100
arc = c1.create_arc(coord, start=0, extent=350, fill="red")

img =  ImageTk.PhotoImage(file = filename)

#c1.create_image(300,100,image = img)
c1.create_image(120+300//2, 10+400//2,image = img)

c1.create_line(500,100,600,10, fill="red", width=3)

c1.create_text(700,50, text="牡丹亭")

c1.create_rectangle(800,50,900,100,fill="blue")

def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   c1.create_oval( x1, y1, x2, y2, fill = python_green )

c1.bind( "<B1-Motion>", paint )

c1.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



