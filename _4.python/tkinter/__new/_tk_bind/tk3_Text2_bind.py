'''
綁定鍵盤滑鼠事件 Text
'''
import tkinter as tk

window = tk.Tk()
window.geometry("600x800")
title = '綁定鍵盤滑鼠事件 Text'
window.title(title)

cccc = tk.Text(window)
cccc.pack()

def processKeyEvent(event):
    print("keysym? ", event.keysym, end = ' ')
    print("char? ", event.char, end = ' ')
    print("keycode? ", event.keycode)
    
def mouse_enter(event):
    print('滑鼠移入', end = ' ')

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
    #print("控件位置 : ", event.x, event.y, end = ' ')
    #print("視窗位置 : ", event.x_root, event.y_root, end = ' ')

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

def mouse_up2(event):
    print('up2', end = ' ')

def mouse_up3(event):
    print('up3', end = ' ')

def mouse_up4(event):
    print('up4', end = ' ')

def mouse_up5(event):
    print('up5', end = ' ')

def processKeyEvent(event):
    print(event)

def processKeyEventEnter(event):
    print("你按下了 Enter")

#滑鼠移入
cccc.bind("<Enter>", mouse_enter)

#Mouse Double Click
cccc.bind("<Double-Button-1>", mouseDoubleClick1)    #雙擊左鍵
cccc.bind("<Double-Button-2>", mouseDoubleClick2)    #雙擊中鍵
cccc.bind("<Double-Button-3>", mouseDoubleClick3)    #雙擊右鍵
cccc.bind("<Double-Button-4>", mouseDoubleClick4)    #unknown

#Mouse Down
cccc.bind("<Button-1>", mouse_down1)  #滑鼠左鍵 單擊
cccc.bind("<Button-2>", mouse_down2)  #滑鼠中鍵 單擊
cccc.bind("<Button-3>", mouse_down3)  #滑鼠右鍵 單擊
cccc.bind("<Button-4>", mouse_down4)  #滑鼠上一頁 單擊
cccc.bind("<Button-5>", mouse_down5)  #滑鼠下一頁 單擊

#Mouse Move
cccc.bind('<B1-Motion>', mouse_move1)    #滑鼠左鍵 移動
cccc.bind('<B2-Motion>', mouse_move2)    #滑鼠中鍵 移動
cccc.bind('<B3-Motion>', mouse_move3)    #滑鼠右鍵 移動
cccc.bind('<B4-Motion>', mouse_move4)    #滑鼠上一頁 移動
cccc.bind('<B5-Motion>', mouse_move5)    #滑鼠下一頁 移動

#Mouse Up
cccc.bind('<ButtonRelease-1>', mouse_up1) #滑鼠左鍵 放開
cccc.bind('<ButtonRelease-2>', mouse_up2) #滑鼠中鍵 放開
cccc.bind('<ButtonRelease-3>', mouse_up3) #滑鼠右鍵 放開
cccc.bind('<ButtonRelease-4>', mouse_up4) #滑鼠上一頁 放開
cccc.bind('<ButtonRelease-5>', mouse_up5) #滑鼠下一頁 放開

#Shift + 滾輪
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
cccc.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

#鍵盤事件
cccc.bind("<Key>", processKeyEvent)
cccc.focus_set()

#鍵位事件 Enter
cccc.bind("<Return>", processKeyEventEnter)

window.mainloop()
