"""
PhotoImage


"""
import sys

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def msgShow():
    print('你按了xxxxxx')
    
print("------------------------------------------------------------")  # 60個
'''
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import Image, ImageTk

window = tk.Tk()

# 檔案 => PIL影像
image0 = Image.open(filename)
# PIL影像 => ImageTk影像
tk_image = ImageTk.PhotoImage(image0)

canvas1 = tk.Canvas(window, width=image0.size[0]+40, height=image0.size[1]+30)
canvas1.create_image(20,15,anchor=tk.NW,image=tk_image)
canvas1.pack(fill=tk.BOTH,expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

import tkinter.font

win = tk.Tk()

default_font = tkinter.font.nametofont('TkDefaultFont')
default_font.configure(size=15)
#然後沒用到

tk_image = tk.PhotoImage(file=filename)

print('W = ', tk_image.width())
print('H = ', tk_image.height())

"""
print('影像放大 zoom, 寬高, 整數倍')
tk_image = tk_image.zoom(2, 1)

print('影像縮小 subsample, 寬高, 整數倍')
tk_image = tk_image.subsample(2, 1)
"""

#tk_image.blank()#移除圖片元件tk_image的影像

gs = tk.Canvas(win,width=512,height=512) # 整個畫布
gs.create_image(256,256,image=tk_image)
gs.pack()

win.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import ImageTk, Image

window = tk.Tk() #建立主視窗物件

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file = filename)

#標籤載入圖片 + 邊框處理
label1 = tk.Label(window, image = tk_image, relief = 'sunken',
    bd = 5, width = 350, height = 450)
label1.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import ImageTk, Image

window = tk.Tk()

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

lab1 = tk.Label(window,image=tk_image).pack(side="right")

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

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=tk_image,command=msgShow)
btn.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

window = tk.Tk()

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.TOP)
btn.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

window = tk.Tk()

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.CENTER)
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

window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=tk_image,command=msgShow)
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.TOP)
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

btn = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.CENTER)
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

# 檔案 => PIL影像
img = Image.open(filename)        # 開啟圖片

# Image影像 => ImageTk影像
tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件

label = tk.Label(window, image=tk_img, width=200, height=200)  # 在 Lable 中放入圖片
label.pack()

# 檔案 => ImageTk影像
html_gif = ImageTk.PhotoImage(file=filename)
tk.Label(window,image=html_gif).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageTk

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

window = tk.Tk()

# 檔案 => PIL影像
img = Image.open(filename)
# PIL影像 => ImageTk影像
image = ImageTk.PhotoImage(img)

canvas = tk.Canvas(window, width=img.size[0]+40, height=img.size[1]+30)
canvas.create_image(20,15,anchor=tk.NW,image=image)
canvas.pack(fill=tk.BOTH,expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageTk
                                
window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
img = Image.open(filename)
# PIL影像 => ImageTk影像
image = ImageTk.PhotoImage(img)

text = tk.Text()
text.image_create(tk.END,image=image)
text.insert(tk.END,"\n")
text.insert(tk.END,"牡丹亭")
text.insert(tk.END,"還魂記")
text.pack(fill=tk.BOTH,expand=True)
    
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
html_gif = ImageTk.PhotoImage(file=filename)

label=tk.Label(window,image=html_gif)
label.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("680x400")

# 檔案 => PIL影像
image = Image.open(filename)
# PIL影像 => ImageTk影像
tk_image = ImageTk.PhotoImage(image)

label = Label(root,image=tk_image)
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


from tkinter import *

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

root = Tk()  # 注意Tk的大小写
photo = PhotoImage(file=filename)
the_label = Label(root,
                  text='LENA',
                  justify=LEFT,  #字符串进行左对齐
                  image=photo,
                  compound=CENTER,  # 混合模式,文字在图片的正上方显示
                  font=("方正粗黑宋简体", 24),  #字体和大小
                  fg='red'  # 前景颜色，就是字体颜色
                  )

the_label.pack()  #这句不可少呀

mainloop()


print("------------------------------------------------------------")  # 60個


'''

print("------------------------------------------------------------")  # 60個



# album.py
# 只能用png ?

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work1.png'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work2.png'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work3.png'
filename4 = 'C:/_git/vcs/_1.data/______test_files1/__pic/_work/work4.png'

def fnSet(img):
    lblPhoto.config(image=img)
    
window = tk.Tk()
window.title('相簿')
window.geometry('1000x900')

imgPhoto1=tk.PhotoImage(file=filename1)
imgPhoto2=tk.PhotoImage(file=filename2)
imgPhoto3=tk.PhotoImage(file=filename3)
imgPhoto4=tk.PhotoImage(file=filename4)

imgPhoto1_s=imgPhoto1.subsample(4,4)
imgPhoto2_s=imgPhoto2.subsample(4,4)
imgPhoto3_s=imgPhoto3.subsample(4,4)
imgPhoto4_s=imgPhoto4.subsample(4,4)

lblPhoto=tk.Label(window,image=imgPhoto1)
lblPhoto.pack()
lfrmSet=tk.LabelFrame(window,text='選擇照片',relief='raised',borderwidth=2)
lfrmSet.pack()
btn1=tk.Button(lfrmSet,image=imgPhoto1_s,command=lambda:fnSet(imgPhoto1))
btn1.pack(side='left',padx=5)
btn2=tk.Button(lfrmSet,image=imgPhoto2_s,command=lambda:fnSet(imgPhoto2))
btn2.pack(side='left',padx=5)
btn3=tk.Button(lfrmSet,image=imgPhoto3_s,command=lambda:fnSet(imgPhoto3))
btn3.pack(side='left',padx=5)
btn4=tk.Button(lfrmSet,image=imgPhoto4_s,command=lambda:fnSet(imgPhoto4))
btn4.pack(side='left',padx=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





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

