from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("test_all")

label=Label(root,text="I like tkinter", fg="blue",bg="yellow")
label.pack()

label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15)

label.pack()
label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="nw")
label.pack()
label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="se")
label.pack()

label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor=SE)
label.pack()

label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="nw",
            wraplength = 40)
label.pack()

label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            font="Helvetica 20 bold")
label.pack()



label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            font=("Helvetica",20,"bold"))
label.pack()


label=Label(root,text="abcdefghijklmnopqrstuvwy",
            fg="blue",bg="lightyellow",
            wraplength=80)
label.pack()


label=Label(root,text="abcdefghijklmnopqrstuvwy",
            fg="blue",bg="lightyellow",
            wraplength=80,
            justify="left")
label.pack()


label=Label(root,text="abcdefghijklmnopqrstuvwy",
            fg="blue",bg="lightyellow",
            wraplength=80,
            justify="center")
label.pack()

label=Label(root,text="abcdefghijklmnopqrstuvwy",
            fg="blue",bg="lightyellow",
            wraplength=80,
            justify="right")
label.pack()  

label=Label(root,bitmap="hourglass")
label.pack()  

label=Label(root,bitmap="hourglass",
            compound="left",text="我的天空")
label.pack()  


label=Label(root,bitmap="hourglass",
            compound="top",text="我的天空")
label.pack()  


label=Label(root,bitmap="hourglass",
            compound="center",text="我的天空")
label.pack()  


label=Label(root,text="raised",relief="raised")
label.pack()

label=Label(root,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10)
label.pack()


html_gif = PhotoImage(file="html.gif")
label=Label(root,image=html_gif)
label.pack()


'''
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch2_19_1")
root.geometry("680x400")

image = Image.open("yellowstone.jpg")
yellowstone = ImageTk.PhotoImage(image)
label = Label(root,image=yellowstone)
label.pack()

root.mainloop()






root = Tk()
root.title("ch2_20")
sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif")
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            compound="left")
label.pack()

root.mainloop()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch2\ch2_21.py

# ch2_21.py
from tkinter import *

root = Tk()
root.title("ch2_21")
sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif")
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            justify="left",compound="right")
label.pack()

root.mainloop()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch2\ch2_22.py

# ch2_22.py
from tkinter import *

root = Tk()
root.title("ch2_22")
sseText = """SSE全名是Silicon Stone Education,這家公司在美國,
這是國際專業證照公司,產品多元與豐富."""
sse_gif = PhotoImage(file="sse.gif")
label=Label(root,text=sseText,image=sse_gif,bg="lightyellow",
            compound="center")
label.pack()

root.mainloop()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch2\ch2_23.py

# ch2_23.py
from tkinter import *

counter = 0                                 # 計數的全域變數
def run_counter(digit):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        global counter
        counter += 1                        # 定義這是全域變數
        digit.config(text=str(counter))     # 列出標籤數字內容
        digit.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 啟動呼叫

root = Tk()
root.title("ch2_23")
digit=Label(root,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=10,              # 寬10高3
            font="Helvetic 20 bold")        # 字型設定
digit.pack()
run_counter(digit)                          # 呼叫數字更動方法

root.mainloop()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch2\ch2_24.py

# ch2_24.py
from tkinter import *

root = Tk()
root.title("ch2_24")

label=Label(root,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10,
            cursor="heart")     # 滑鼠外形
label.pack()

root.mainloop()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch2\ch2_25.py

# ch2_25.py
from tkinter import *

root = Tk()
root.title("ch2_25")
label=Label(root,text="I like tkinter")
label.pack()        # 包裝與定位元件
print(label.keys())

root.mainloop()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch2\ch2_26.py

# ch2_26.py
from tkinter import *
from tkinter.ttk import Separator

root = Tk()
root.title("ch2_26")

myTitle = "一個人的極境旅行"
myContent = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""

lab1 = Label(root,text=myTitle,
             font="Helvetic 20 bold")
lab1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL)
sep.pack(fill=X,padx=5)

lab2 = Label(root,text=myContent)
lab2.pack(padx=10,pady=10)

root.mainloop()









print('------------------------------------------------------------')	#60個








'''


root.mainloop()


