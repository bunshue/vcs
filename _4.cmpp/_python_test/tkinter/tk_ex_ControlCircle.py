from tkinter import * # Import tkinter

window = Tk() # Create a window
window.title('左鍵變大 右鍵變小')

# 設定主視窗大小
w = 400
h = 400
size = str(w)+'x'+str(h)
window.geometry(size)

def mouseClick1(event):
    canvas.delete("oval")
    global radius
    if radius < 100:
        radius += 2
    canvas.create_oval(100 - radius, 100 - radius, 
                       100 + radius, 100 + radius, tags = "oval")

def mouseClick2(event):
    print('你按了滑鼠中鍵')
    
def mouseClick3(event):
    canvas.delete("oval")
    global radius
    if radius > 2:
        radius -= 2
    canvas.create_oval(100 - radius, 100 - radius, 
                       100 + radius, 100 + radius, tags = "oval")

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
    
canvas = Canvas(window, bg = "white", width = 200, height = 200)
canvas.pack()
radius = 50
canvas.create_oval(100 - radius, 100 - radius, 
                   100 + radius, 100 + radius, tags = "oval")

# Bind canvas with mouse events
canvas.bind("<Button-1>", mouseClick1)
canvas.bind("<Button-2>", mouseClick2)
canvas.bind("<Button-3>", mouseClick3)
canvas.bind("<Button-4>", mouseClick4)
canvas.bind("<Button-5>", mouseClick5)
canvas.bind("<Double-1>", mouseDoubleClick1)
canvas.bind('<Motion>',motion)

window.mainloop() # Create an event loop
