from tkinter import *

root=Tk()
root.geometry("200x200")
text=Text(root)
text.pack()

def func(event):
    print(event)
def func_release(event):
    print("release")
#单击
# text.bind("<Button-1>",func)
# root.bind("<Button-1>",func)
#双击
# text.bind("<Double-Button-1>",func)
# 鼠标释放
# text.bind("<ButtonRelease-1>",func_release)
#鼠标移入
# text.bind("<Enter>",func)
#鼠标按住移动事件
# text.bind("<B1-Motion>",func)
#键盘按下事件
# text.bind("<Key>",func)

#键位绑定事件
# def func3(event):
#     print("你按下了回车!")
# text.bind("<Return>",func3)


#实现的一个拖拽功能
def func4(event):
    # print(event)
    x=str(event.x_root)
    y=str(event.y_root)
    root.geometry("200x200+"+x+"+"+y)

text.bind("<B1-Motion>",func4)




root.mainloop()
