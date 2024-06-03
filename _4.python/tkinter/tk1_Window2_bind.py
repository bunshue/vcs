"""
綁定鍵盤滑鼠事件 Window
"""

import tkinter as tk
import tkinter.filedialog

print("------------------------------------------------------------")  # 60個



'''
cccc = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
cccc.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = '綁定鍵盤滑鼠事件 Window'
cccc.title(title)

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

def mouse_up2(event):
    print('up2', end = ' ')

def mouse_up3(event):
    print('up3', end = ' ')

def mouse_up4(event):
    print('up4', end = ' ')

def mouse_up5(event):
    print('up5', end = ' ')

def mouse_motion(event):
    #print(f'x: {event.x} y: {event.y}')
    #print('滑鼠位置: (%s, %s)' % (event.x, event.y), end = ' ')
    cccc.title('滑鼠位置: (%s, %s)' % (event.x, event.y))

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

cccc.bind('<KeyPress>', lambda event: print(f'KeyPress ({event.char})'))
cccc.bind('<Alt-KeyPress-a>', lambda event: print('你按了Alt+A ', event))

cccc.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "Mouse location - x:{}, y:{}".format(x,y)
    var.set(textvar)
    
root = Tk()
root.title("ch40_20_2")             # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

x, y = 0, 0                         # x,y座標
var = StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = Label(root,textvariable=var)  # 建立標籤
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

root.bind("<Motion>",mouseMotion)   # 增加事件處理程式

root.mainloop()

'''
print("------------------------------------------------------------")  # 60個

print('按右鍵 另存新圖')
window = tk.Tk()

from PIL import ImageTk, Image
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
img = ImageTk.PhotoImage(Image.open(filename))
label1 =tk.Label(window, image = img)
label1.pack()

def save(event):
    filename = tkinter.filedialog.asksaveasfilename(title="儲存檔案", initialfile="tmp_picture1.jpg")
    if filename and hasattr(label1, "qr_img"):
        label1.qr_img.save(filename)


window.bind("<Button-3>", save)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print('按右鍵 右鍵選單 另存新圖')
window = tk.Tk()

from PIL import ImageTk, Image
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
img = ImageTk.PhotoImage(Image.open(filename))
label1 =tk.Label(window, image = img)
label1.pack()

def save():
    filename = tkinter.filedialog.asksaveasfilename(title="儲存檔案", initialfile="tmp_picture2.jpg")
    if filename and hasattr(label1, "qr_img"):
        label1.qr_img.save(filename)


def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)


context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="儲存圖片", command=save)

window.bind("<Button-3>", show_context_menu)


window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




