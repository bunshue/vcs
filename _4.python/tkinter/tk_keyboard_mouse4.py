'''
Text 綁定鍵盤滑鼠事件
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
title = "這是主視窗"
window.title(title)
#window.title('Event Binding')

text=tk.Text(window)
text.pack()

def func(event):
    print(event)
def func_release(event):
    print("release")
#单击
# text.bind("<Button-1>",func)
# window.bind("<Button-1>",func)
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
    window.geometry("200x200+"+x+"+"+y)

text.bind("<B1-Motion>",func4)

window.mainloop()

