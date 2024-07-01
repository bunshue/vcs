"""

綁定鍵盤滑鼠事件 Frame

"""

import tkinter as tk

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x800")
title = '綁定鍵盤滑鼠事件 Frame'
window.title(title)

width = 600
height = 400
cccc = tk.Frame(window, bg = 'pink', width = width, height = 400)
cccc.pack()

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
    """
    print("在控件位置 : ", event.x, event.y, end = ' ')
    print("視窗位置 : ", event.x_root, event.y_root, end = ' ')
    print("按鍵 : ", event.num, end = ' ')
    """
def mouse_down2(event):
    print('你按了滑鼠中鍵', end = ' ')
    
def mouse_down3(event):
    print('你按了滑鼠右鍵', end = ' ')

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
    #print("鍵碼 : ", repr(event.char))

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

window.mainloop()

"""
frame.focus_set()
"""
print('------------------------------------------------------------')	#60個

print('讀取滑鼠左鍵位置')

def callback(event):                        # 事件處理程式
    print("滑鼠點擊位置 :", event.x, event.y)   # 列印座標
    
window = tk.Tk()
window.geometry("600x800")

frame = tk.Frame(window,width=300,height=180)
frame.bind("<Button-1>",callback)           # 按一下綁定callback
frame.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def key(event):                     # 列出所按的鍵
    print("按了 " + repr(event.char) + " 鍵")

def coordXY(event):                 # 列出滑鼠座標
    frame.focus_set()               # frame物件取得焦點
    print("滑鼠座標 : ", event.x, event.y)
    
window = tk.Tk()
window.geometry("600x800")

frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key)            # frame物件的<Key>綁定key
frame.bind("<Button-1>", coordXY)   # frame物件按一下綁定coordXY
frame.pack()

window.mainloop()


print('------------------------------------------------------------')	#60個
