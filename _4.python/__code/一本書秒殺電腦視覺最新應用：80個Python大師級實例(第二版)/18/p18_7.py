from tkinter import *
"""自定义函数"""
def init(data):
    # 数据从run函数中预置宽度和高度
    data.circleSize = min(data.width, data.height)/10
    data.circleX = data.width/2
    data.circleY = data.height/2
    data.charText = ""
    data.keysymText = "" 
"""跟踪并响应鼠标点击"""
def mousePressed(event, data):
    data.circleX = event.x
    data.circleY = event.y 
"""跟踪和响应按键"""
def keyPressed(event, data):
    data.charText = event.char
    data.keysymText = event.keysym 
"""通常使用redrawAll绘制图形"""
def redrawAll(canvas, data):
    canvas.create_oval(data.circleX - data.circleSize, 
                       data.circleY - data.circleSize,
                       data.circleX + data.circleSize,
                       data.circleY + data.circleSize)
    if data.charText != "":
        canvas.create_text(data.width/10, data.height/3,
                           text="char: " + data.charText)
    if data.keysymText != "":
        canvas.create_text(data.width/10, data.height*2/3, 
                           text="keysym: " + data.keysymText)
"""按原样使用run函数""" 
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()     
    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data) 
    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data) 
    #设置数据并调用init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data) 
    #创建根和画布
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack() 
    #设置事件
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data) 
    #然后启动应用程序
    root.mainloop()  #块，直到窗口关闭
    print("bye!") 
run(400, 200)
