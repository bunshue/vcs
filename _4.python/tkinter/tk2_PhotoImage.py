"""
PhotoImage


可能有圖片 目前還不能搬走

"""

import sys

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

print("------------------------------------------------------------")  # 60個

def msgShow():
    print('你按了xxxxxx')

print("------------------------------------------------------------")  # 60個
'''
print("將圖片貼在 Canvas 上")
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("600x900")

# 檔案 => PIL影像
image0 = Image.open(filename)
# PIL影像 => ImageTk影像
tk_image = ImageTk.PhotoImage(image0)

canvas1 = tk.Canvas(window, width=image0.size[0]+40, height=image0.size[1]+30)
canvas1.create_image(20,15,anchor=tk.NW,image=tk_image)
canvas1.pack(fill=tk.BOTH,expand=True)

#tk顯示一張圖片 在label上
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)
image = ImageTk.PhotoImage(image)

label1 = tk.Label(image = image)
label1.image = image
label1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

window = tk.Tk()
window.geometry("600x800")

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

gs = tk.Canvas(window,width=512,height=512) # 整個畫布
gs.create_image(256,256,image=tk_image)
gs.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("600x800")

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
window.geometry("600x800")

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

button1 = tk.Button(window,image=tk_image,command=msgShow)
button1.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("600x800")

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

button1 = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.TOP)
button1.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("600x800")

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

button1 = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.CENTER)
button1.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
html_gif = ImageTk.PhotoImage(file=filename)

tk.Label(window,image=html_gif).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

button1 = tk.Button(window,image=tk_image,command=msgShow)
button1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

button1 = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.TOP)
button1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
tk_image = ImageTk.PhotoImage(file=filename)

button1 = tk.Button(window,image=tk_image,command=msgShow,
             text="Click me",compound=tk.CENTER)
button1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")

from PIL import Image, ImageTk

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)        # 開啟圖片

# Image影像 => ImageTk影像
tk_image = ImageTk.PhotoImage(image)    # 轉換為 tk 圖片物件

label = tk.Label(window, image=tk_image, width=200, height=200)  # 在 Lable 中放入圖片
label.pack()

# 檔案 => ImageTk影像
html_gif = ImageTk.PhotoImage(file=filename)
tk.Label(window,image=html_gif).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageTk
                                
window = tk.Tk()
window.geometry("600x800")

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
window.geometry("600x800")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => ImageTk影像
html_gif = ImageTk.PhotoImage(file=filename)

label=tk.Label(window,image=html_gif)
label.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("600x800")

# 檔案 => PIL影像
image = Image.open(filename)
# PIL影像 => ImageTk影像
tk_image = ImageTk.PhotoImage(image)

label = tk.Label(window,image=tk_image)
label.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")

sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = ImageTk.PhotoImage(file="__new/sse.gif")
label=tk.Label(window,text=sseText,image=sse_gif,bg="lightyellow",
            compound="left")
label.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x800")

sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = ImageTk.PhotoImage(file="__new/sse.gif")
label=tk.Label(window,text=sseText,image=sse_gif,bg="lightyellow",
            justify="left",compound="right")
label.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x800")

sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = ImageTk.PhotoImage(file="__new/sse.gif")
label=tk.Label(window,text=sseText,image=sse_gif,bg="lightyellow",
            compound="center")
label.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

window = tk.Tk()
window.geometry("600x800")

photo = ImageTk.PhotoImage(file=filename)
the_label = tk.Label(window,
                  text='LENA',
                  justify=tk.LEFT,  #字符串进行左对齐
                  image=photo,
                  compound=tk.CENTER,  # 混合模式,文字在图片的正上方显示
                  font=("方正粗黑宋简体", 24),  #字体和大小
                  fg='red'  # 前景颜色，就是字体颜色
                  )

the_label.pack()  #这句不可少呀

window.mainloop()

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
window.geometry('1000x900')
window.title('相簿')

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

button1=tk.Button(lfrmSet,image=imgPhoto1_s,command=lambda:fnSet(imgPhoto1))
button1.pack(side='left',padx=5)
button2=tk.Button(lfrmSet,image=imgPhoto2_s,command=lambda:fnSet(imgPhoto2))
button2.pack(side='left',padx=5)
button3=tk.Button(lfrmSet,image=imgPhoto3_s,command=lambda:fnSet(imgPhoto3))
button3.pack(side='left',padx=5)
button4=tk.Button(lfrmSet,image=imgPhoto4_s,command=lambda:fnSet(imgPhoto4))
button4.pack(side='left',padx=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print('把圖片顯示在Label上')
filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

window = tk.Tk()
window.geometry("800x600")

night = ImageTk.PhotoImage(file=filename)
label1 = tk.Label(window,image=night)
label1.place(x=0,y=0,width=512,height=512)

label2=tk.Label(window,image=night)
label2.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

window.mainloop()

print('------------------------------------------------------------')	#60個

print('把圖片顯示在Label上')

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

window = tk.Tk()
window.geometry("640x480")

night = ImageTk.PhotoImage(file=filename)
label = tk.Label(window,image=night)
label.place(relx=0.1,rely=0.1,relheight=0.8)

print('把圖片顯示在Button上')

sunGif = ImageTk.PhotoImage(file="__new/sun.gif")                 # Image物件
button1 = tk.Button(window,image=sunGif,command=msgShow)     # 含影像的按鈕
button1.pack()

window.mainloop()

print('------------------------------')	#60個

window = tk.Tk()

sunGif = ImageTk.PhotoImage(file="__new/sun.gif")                 # Image物件
button1 = tk.Button(window,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=tk.TOP)          

button1.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

sunGif = ImageTk.PhotoImage(file="__new/sun.gif")                 # Image物件
button1 = tk.Button(window,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=tk.CENTER)          
button1.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

sunGif = ImageTk.PhotoImage(file="__new/sun.gif")                 # Image物件
button1 = tk.Button(window,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=tk.LEFT)          
button1.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

sunGif = ImageTk.PhotoImage(file="__new/sun.gif")                 # Image物件
button1 = tk.Button(window,image=sunGif,command=msgShow,     # 含影像的按鈕
             cursor="star")                         # star外形   
button1.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = ImageTk.PhotoImage(file="__new/sse.gif")     # Logo影像檔
logo = tk.Label(window,image=sseGif,text=msg,compound=tk.BOTTOM)
accountL = tk.Label(window,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = tk.Label(window,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = tk.Entry(window)                  # 文字方塊account
pwdE = tk.Entry(window,show="*")             # 文字方塊pwd
accountE.grid(row=1,column=1)           # 定位文字方塊account
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd

window.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo1():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    
window = tk.Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = ImageTk.PhotoImage(file="__new/sse.gif")     # Logo影像檔
logo = tk.Label(window,image=sseGif,text=msg,compound=tk.BOTTOM)
accountL = tk.Label(window,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = tk.Label(window,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = tk.Entry(window)                  # 文字方塊account
pwdE = tk.Entry(window,show="*")             # 文字方塊pwd
accountE.grid(row=1,column=1)           # 定位文字方塊account
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd
# 以下建立Login和Quit案鈕
loginButton = tk.Button(window,text="Login",command=printInfo1)
loginButton.grid(row=3,column=0)
quitButton = tk.Button(window,text="Quit",command=window.quit)
quitButton.grid(row=3,column=1)

window.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo2():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    
window = tk.Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = ImageTk.PhotoImage(file="__new/sse.gif")     # Logo影像檔
logo = tk.Label(window,image=sseGif,text=msg,compound=tk.BOTTOM)
accountL = tk.Label(window,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = tk.Label(window,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = tk.Entry(window)                  # 文字方塊account
pwdE = tk.Entry(window,show="*")             # 文字方塊pwd
accountE.grid(row=1,column=1)           # 定位文字方塊accou
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd

# 以下建立Login和Quit案鈕
loginButton = tk.Button(window,text="Login",command=printInfo2)
loginButton.grid(row=3,column=0,sticky=tk.W,pady=5)
quitButton = tk.Button(window,text="Quit",command=window.quit)
quitButton.grid(row=3,column=1,sticky=tk.W,pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo3():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    
window = tk.Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = ImageTk.PhotoImage(file="__new/sse.gif")     # Logo影像檔
logo = tk.Label(window,image=sseGif,text=msg,compound=tk.BOTTOM)
accountL = tk.Label(window,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = tk.Label(window,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = tk.Entry(window)                  # 文字方塊account
pwdE = tk.Entry(window,show="*")             # 文字方塊pwd
accountE.insert(0,"Kevin")              # 預設Account內容
pwdE.insert(0,"pwd")                    # 預設pwd內容
accountE.grid(row=1,column=1)           # 定位文字方塊accou
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd
# 以下建立Login和Quit案鈕
loginButton = tk.Button(window,text="Login",command=printInfo3)
loginButton.grid(row=3,column=0,sticky=tk.W,pady=5)
quitButton = tk.Button(window,text="Quit",command=window.quit)
quitButton.grid(row=3,column=1,sticky=tk.W,pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo4():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    accountE.delete(0,tk.END)              # 刪除account文字方塊的帳號內容
    pwdE.delete(0,tk.END)                  # 刪除pwd文字方塊的密碼內容
    
window = tk.Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = ImageTk.PhotoImage(file="__new/sse.gif")     # Logo影像檔
logo = tk.Label(window,image=sseGif,text=msg,compound=tk.BOTTOM)
accountL = tk.Label(window,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = tk.Label(window,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = tk.Entry(window)                  # 文字方塊account
pwdE = tk.Entry(window,show="*")             # 文字方塊pwd
accountE.insert(1,"Kevin")              # 預設Account內容
pwdE.insert(1,"pwd")                    # 預設pwd內容
accountE.grid(row=1,column=1)           # 定位文字方塊accou
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd
# 以下建立Login和Quit案鈕
loginButton = tk.Button(window,text="Login",command=printInfo4)
loginButton.grid(row=3,column=0,sticky=tk.W,pady=5)
quitButton = tk.Button(window,text="Quit",command=window.quit)
quitButton.grid(row=3,column=1,sticky=tk.W,pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    label.config(text="你選的是"+var.get())

window = tk.Tk()

imgStar = ImageTk.PhotoImage(file="__new/star.gif")
imgMoon = ImageTk.PhotoImage(file="__new/moon.gif")
imgSun = ImageTk.PhotoImage(file="__new/sun.gif")

var = tk.StringVar()                               # 選項紐綁定的變數
var.set("星星")                                 # 預設選項是男生
                       
label = tk.Label(window,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbStar = tk.Radiobutton(window,image=imgStar,        # 星星選項鈕
                     variable=var,value="星星",
                     command=printSelection)
rbStar.pack()

rbMoon = tk.Radiobutton(window,image=imgMoon,        # 月亮選項鈕
                     variable=var,value="月亮",
                     command=printSelection)
rbMoon.pack()

rbSun = tk.Radiobutton(window,image=imgSun,          # 太陽選項鈕
                    variable=var,value="太陽",
                    command=printSelection)
rbSun.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    label.config(text="你選的是"+var.get())

window = tk.Tk()

imgStar = ImageTk.PhotoImage(file="__new/star.gif")
imgMoon = ImageTk.PhotoImage(file="__new/moon.gif")
imgSun = ImageTk.PhotoImage(file="__new/sun.gif")

var = tk.StringVar()                               # 選項紐綁定的變數
var.set("星星")                                 # 預設選項是男生
                       
label = tk.Label(window,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbStar = tk.Radiobutton(window,image=imgStar,        # 星星選項鈕
                     text="星星",compound=tk.RIGHT,
                     variable=var,value="星星",
                     command=printSelection)
rbStar.pack()

rbMoon = tk.Radiobutton(window,image=imgMoon,        # 月亮選項鈕
                     text="月亮",compound=tk.RIGHT,
                     variable=var,value="月亮",
                     command=printSelection)
rbMoon.pack()

rbSun = tk.Radiobutton(window,image=imgSun,          # 太陽選項鈕
                    text="太陽",compound=tk.RIGHT,
                    variable=var,value="太陽",
                    command=printSelection)
rbSun.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = ImageTk.PhotoImage(file="__new/sse.gif")         # Logo影像檔
logo = tk.Label(window,image=sseGif,text=msg,compound=tk.BOTTOM)
logo.pack()

# 以下是LabelFrame標籤框架
labFrame = tk.LabelFrame(window,text="資料驗證") # 建立標籤框架
accountL = tk.Label(labFrame,text="Account")   # account標籤
accountL.grid(row=0,column=0)
pwdL = tk.Label(labFrame,text="Password")      # pwd標籤
pwdL.grid(row=1,column=0)

accountE = tk.Entry(labFrame)                  # 文字方塊account
accountE.grid(row=0,column=1)               # 定位文字方塊account
pwdE = tk.Entry(labFrame,show="*")             # 文字方塊pwd
pwdE.grid(row=1,column=1,pady=10)           # 定位文字方塊pwd
labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)   # 包裝與定位標籤框架

window.mainloop()
'''
print('------------------------------------------------------------')	#60個
    
import customtkinter as ctk
from PIL import Image, ImageTk

def stretch_image(event):
	global resized_tk

	# size 
	width = event.width
	height = event.height

	# create an image
	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)

	# place on the canvas
	canvas.create_image(0,0,image = resized_tk, anchor = 'nw')

def fill_image(event):
	global resized_tk

	# current ratio 
	canvas_ratio = event.width / event.height

	# get coordinates 
	if canvas_ratio > image_ratio: # canvas is wider than the image
		width = int(event.width) 
		height = int(width / image_ratio)
	else: # canvas is narrower than the image
		height = int(event.height)
		width = int(height * image_ratio) 

	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)
	canvas.create_image(
		int(event.width / 2),
		int(event.height / 2),
		anchor = 'center',
		image = resized_tk)

def show_full_image(event):
	global resized_tk

	# current ratio 
	canvas_ratio = event.width / event.height

	# get coordinates 
	if canvas_ratio > image_ratio: # canvas is wider than the image
		height = int(event.height)
		width = int(height * image_ratio) 
	else: # canvas is narrower than the image
		width = int(event.width) 
		height = int(width / image_ratio)



	resized_image = image_original.resize((width, height))
	resized_tk = ImageTk.PhotoImage(resized_image)
	canvas.create_image(
		int(event.width / 2),
		int(event.height / 2),
		anchor = 'center',
		image = resized_tk)

# exercise:
# create a third scaling behaviour to always show the full image without cutting off parts

# setup
window = tk.Tk()
window.geometry('600x400')

# grid layout
window.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
window.rowconfigure(0, weight = 1)

image_original = Image.open('__new/raccoon.jpg')
image_ratio = image_original.size[0] / image_original.size[1]
print(image_ratio)
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('__new/python_dark.png').resize((30,30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

img_ctk = ctk.CTkImage(
	light_image = Image.open('__new/python_dark.png'),
	dark_image = Image.open('__new/python_light.png'))

# widget
# label = ttk.Label(window, text = 'raccoon', image = image_tk)
# label.pack()
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text = '   A button', image = python_dark_tk, compound = 'left')
button.pack(pady = 10)

button_ctk = ctk.CTkButton(button_frame, text = 'A button', image = img_ctk, compound = 'left')
button_ctk.pack(pady = 10)

button_frame.grid(column = 0, row = 0, sticky = 'nsew')

# canvas -> image
canvas = tk.Canvas(window, background = 'black', bd = 0, highlightthickness = 0, relief = 'ridge')
canvas.grid(column = 1, columnspan = 3, row = 0, sticky = 'nsew')

canvas.bind('<Configure>', show_full_image)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *
from PIL import Image, ImageTk
      
window = tk.Tk()

Style().configure("Treeview",rowheight=35)  # 格式化擴充row高度

info = ["鳳凰新聞App可以獲得中國各地最新消息",
        "瑞士國家鐵路App提供全瑞士火車時刻表",
        "可口可樂App是一個娛樂的軟件"]

tree = Treeview(window,columns=("說明"))
tree.heading("#0",text="App")           # 圖標欄位icon column
tree.heading("#1",text="功能說明")
tree.column("#1",width=300)             # 格式化欄標題

img1 = Image.open("__new/news.jpg")           # 插入鳳凰新聞App圖示
imgObj1 = ImageTk.PhotoImage(img1)
tree.insert("",index=tk.END,text="鳳凰新聞",image=imgObj1,values=info[0])

img2 = Image.open("__new/sbb.jpg")            # 插入瑞士國家鐵路App圖示
imgObj2 = ImageTk.PhotoImage(img2)
tree.insert("",index=tk.END,text="瑞士鐵路",image=imgObj2,values=info[1])

img3 = Image.open("__new/coca.jpg")           # 插入可口可樂App圖示          
imgObj3 = ImageTk.PhotoImage(img3)
tree.insert("",index=tk.END,text="可口可樂",image=imgObj3,values=info[2])    
tree.pack()

window.mainloop()

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



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
"""
import tkinter.font
default_font = tkinter.font.nametofont('TkDefaultFont')
default_font.configure(size=15)
#然後沒用到
"""




