'''
綁定鍵盤滑鼠事件 Text
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
#單擊
# text.bind("<Button-1>",func)
# window.bind("<Button-1>",func)
#雙擊
# text.bind("<Double-Button-1>",func)
# 鼠標釋放
# text.bind("<ButtonRelease-1>",func_release)
#鼠標移入
# text.bind("<Enter>",func)
#鼠標按住移動事件
# text.bind("<B1-Motion>",func)
#鍵盤按下事件
# text.bind("<Key>",func)

#鍵位綁定事件
# def func3(event):
#     print("你按下了回車!")
# text.bind("<Return>",func3)


#實現的一個拖拽功能
def func4(event):
    # print(event)
    x=str(event.x_root)
    y=str(event.y_root)
    window.geometry("200x200+"+x+"+"+y)

text.bind("<B1-Motion>",func4)

window.mainloop()
