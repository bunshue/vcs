"""
PhotoImage


"""
import sys

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
'''
print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import Image, ImageTk

window = tk.Tk()

# 檔案 => PIL影像
image0 = Image.open(filename)

# PIL影像 => ImageTk影像
image1 = ImageTk.PhotoImage(image0)

canvas1 = tk.Canvas(window, width=image0.size[0]+40, height=image0.size[1]+30)
canvas1.create_image(20,15,anchor=tk.NW,image=image1)
canvas1.pack(fill=tk.BOTH,expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

import tkinter.font

win = tk.Tk()

default_font = tkinter.font.nametofont('TkDefaultFont')
default_font.configure(size=15)
#然後沒用到

photo = tk.PhotoImage(file=filename)

gs = tk.Canvas(win,width=400,height=300)
gs.create_image(60,120,image=photo)
gs.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

window = tk.Tk() #建立主視窗物件

"""
# 設定標籤的顯示文字(text)、背景(bg)和前景(fg)顏色
lbla = tk.Label(window, text = 'Gray', bg = 'gray',
        fg = 'white').pack(side = 'right')#加入版面

lblb = tk.Label(window, text = 'Yellow',
        bg = 'yellow', fg = 'gray').pack(
        side = 'right', padx = 5, pady = 10)

lblc = tk.Label(window, text = 'Orange',
        bg = 'orange', fg = 'black').pack(side = 'right')

tk.mainloop()
"""

# 檔案 => ImageTk影像
photo = ImageTk.PhotoImage(file = '001.png')

#標籤 - bg 設背景色
t1 = tk.Label(window, text = 'Hello\n Python', bg = '#78A', 
    fg = '#FF0', relief = 'groove', bd = 2, 
    width = 15, height = 3, justify = 'right')

t2 = tk.Label(window, text = '世界', width = 6, height = 3,
    relief = tk.RIDGE, bg = 'pink', font = ('標楷體', 16))

#在第3個標籤載入圖片
t3 = tk.Label(window, image = photo, relief = 'sunken',
    bd = 5, width = 180, height = 150)

t1.grid(row = 0, column = 0)
t2.grid(row = 0, column = 1)
t3.grid(columnspan = 2)

tk.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import ImageTk, Image

window = tk.Tk()

# 檔案 => ImageTk影像
pic_image = ImageTk.PhotoImage(file=filename)

lab1 = tk.Label(window,image=pic_image).pack(side="right")

poem_text = """
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""

lab2 = tk.Label(window,text=poem_text,bg="lightyellow",
             padx=10).pack(side="left")

"""
lab2 = tk.Label(window,text=poem_text,bg="lightyellow",
             justify=tk.LEFT,padx=10).pack(side="left")
"""

tk.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import ImageTk, Image

window = tk.Tk()

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容

# 檔案 => ImageTk影像
sun_gif = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=sun_gif,command=msgShow)

label.pack()                      
btn.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

window = tk.Tk()

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容

# 檔案 => ImageTk影像
sun_gif = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=tk.TOP)

label.pack()                      
btn.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

window = tk.Tk()

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
label = tk.Label(window)               # 標籤內容

# 檔案 => ImageTk影像
sun_gif = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=tk.CENTER)

label.pack()                      
btn.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
html_gif = ImageTk.PhotoImage(file=filename)

tk.Label(window,image=html_gif).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個
    
window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
sselogo = ImageTk.PhotoImage(file=filename)

lab1 = tk.Label(window,image=sselogo).pack(side="right")

poem_text = """
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""

lab2 = tk.Label(window,text=poem_text,bg="lightyellow",
             padx=10).pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個
    
window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
sselogo = ImageTk.PhotoImage(file=filename)

lab1 = tk.Label(window,image=sselogo).pack(side="right")

poem_text = """
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""

lab2 = tk.Label(window,text=poem_text,bg="lightyellow",
             justify=tk.LEFT,padx=10).pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = tk.Tk()

label = tk.Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
sun_gif = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=sun_gif,command=msgShow)

label.pack()                      
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = tk.Tk()

label = tk.Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
sun_gif = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=tk.TOP)

label.pack()                      
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = tk.Tk()

label = tk.Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
sun_gif = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=tk.CENTER)

label.pack()                      
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
pic = ImageTk.PhotoImage(file=filename)

label1 = tk.Label(window,image=pic).pack(side="right")

poem_text = """
故人西辭黃鶴樓，
煙花三月下揚州。
孤帆遠影碧空盡，
唯見長江天際流。
"""
label2 = tk.Label(window,text=poem_text,bg="lightyellow",
             justify=tk.LEFT,padx=10).pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

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

from PIL import Image, ImageTk

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

"""
img = Image.open(filename)        # 開啟圖片
tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件

label = tk.Label(window, image=tk_img, width=200, height=200)  # 在 Lable 中放入圖片
label.pack()

html_gif = ImageTk.PhotoImage(file=filename)
tk.Label(window,image=html_gif).pack()

"""

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageTk

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

window = tk.Tk()
img = Image.open(filename)
image = ImageTk.PhotoImage(img)

canvas = tk.Canvas(window, width=img.size[0]+40,
                height=img.size[1]+30)
canvas.create_image(20,15,anchor=tk.NW,image=image)
canvas.pack(fill=tk.BOTH,expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageTk
                                
window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

img = Image.open(filename)
image = ImageTk.PhotoImage(img)

text = tk.Text()
text.image_create(tk.END,image=image)
text.insert(tk.END,"\n")
text.insert(tk.END,"牡丹亭")
text.insert(tk.END,"還魂記")
text.pack(fill=tk.BOTH,expand=True)
    
window.mainloop()
'''
print("------------------------------------------------------------")  # 60個

window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
html_gif = ImageTk.PhotoImage(file=filename)
label=tk.Label(window,image=html_gif)
label.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("680x400")

image = Image.open("yellowstone.jpg")
yellowstone = ImageTk.PhotoImage(image)
label = Label(root,image=yellowstone)
label.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個

root = Tk()

sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif")
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            compound="left")
label.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif")
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            justify="left",compound="right")
label.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif")
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            compound="center")
label.pack()

root.mainloop()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個






"""

print("全圖640X480, 每160X160裁一塊出來")
W = 640
H = 480
w = 160
h = 160

for(y = 0; y < H; y += h)
  for(x = 0; x < W; x += w)

for y in range(0, H, h):
    for x in range(0, W, w):
        box = x, y, min(W, x + w), min(H, y + h)
        print(box)
        # tile = ImageTk.PhotoImage(image.crop(box))
        # canvas.create_image(x, y, image = tile, anchor = NW)
        # print(x, y)
        # print(box)





"""









