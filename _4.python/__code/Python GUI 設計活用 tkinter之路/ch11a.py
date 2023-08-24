# ch11_1.py
from tkinter import *
def pythonClicked():            # Python核取方塊事件處理程式     
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():              # Java核取方塊事件處理程式
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked():            # Button按鈕事件處理程式
    lab.config(text="Button clicked")
    
root = Tk()
root.title("ch11_1")            # 視窗標題
root.geometry("300x180")        # 視窗寬300高160

btn = Button(root,text="Click me",command=buttonClicked)
btn.pack(anchor=W)
varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()





#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_1_1.py

# ch11_1_1.py
from tkinter import *
def pythonClicked():            # Python核取方塊事件處理程式     
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():              # Java核取方塊事件處理程式
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked(event):       # Button按鈕事件處理程式
    lab.config(text="Button clicked")
    
root = Tk()
root.title("ch11_1_1")          # 視窗標題
root.geometry("300x180")        # 視窗寬300高160

btn = Button(root,text="Click me")
btn.pack(anchor=W)
btn.bind("<Button-1>",buttonClicked)  # 按一下Click me綁定buttonClicked方法

varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_2.py

# ch11_2.py
from tkinter import *
def callback(event):                        # 事件處理程式
    print("Clicked at", event.x, event.y)   # 列印座標
    
root = Tk()
root.title("ch11_2")
frame = Frame(root,width=300,height=180)
frame.bind("<Button-1>",callback)           # 按一下綁定callback
frame.pack()

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_2_1.py

# ch11_2_1.py
from tkinter import *
def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "Mouse location - x:{}, y:{}".format(x,y)
    var.set(textvar)
    
root = Tk()
root.title("ch11_2_1")              # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

x, y = 0, 0                         # x,y座標
var = StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = Label(root,textvariable=var)  # 建立標籤
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

root.bind("<Motion>",mouseMotion)   # 增加事件處理程式

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_3.py

# ch11_3.py
from tkinter import *
def enter(event):                       # Enter事件處理程式
    x.set("滑鼠進入Exit功能鈕")   
def leave(event):                       # Leave事件處理程式
    x.set("滑鼠離開Exit功能鈕")
    
root = Tk()
root.title("ch11_3")
root.geometry("300x180")

btn = Button(root,text="離開",command=root.destroy)
btn.pack(pady=30)
btn.bind("<Enter>",enter)               # 進入綁定enter
btn.bind("<Leave>",leave)               # 離開綁定leave

x = StringVar()
lab = Label(root,textvariable=x,        # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(pady=30)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_4.py

# ch11_4.py
from tkinter import *
from tkinter import messagebox

def leave(event):                       # <Esc>事件處理程式
    ret = messagebox.askyesno("ch11_4","是否離開?")
    if ret == True:
        root.destroy()                  # 結束程式
    else:
        return
   
root = Tk()
root.title("ch11_4")

root.bind("<Escape>",leave)             # Esc鍵綁定leave函數
lab = Label(root,text="測試Esc鍵",      # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(padx=30,pady=30)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_5.py

# ch11_5.py
from tkinter import *
def key(event):                     # 處理鍵盤按a ... z
    print("按了 " + repr(event.char) + " 鍵") 
   
root = Tk()
root.title("ch11_5")

root.bind("<Key>",key)              # <Key>鍵綁定key函數

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_6.py

# ch11_6.py
from tkinter import *
def key(event):                     # 列出所按的鍵
    print("按了 " + repr(event.char) + " 鍵")

def coordXY(event):                 # 列出滑鼠座標
    frame.focus_set()               # frame物件取得焦點
    print("滑鼠座標 : ", event.x, event.y)
    
root = Tk()
root.title("ch11_6")

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)            # frame物件的<Key>綁定key
frame.bind("<Button-1>", coordXY)   # frame物件按一下綁定coordXY
frame.pack()

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_7.py

# ch11_7.py
from tkinter import *
def buttonClicked(event):           # Button按鈕事件處理程式
    print("I like tkinter")

# 所傳遞的物件onoff是btn物件    
def toggle(onoff):                  # 切換綁定
    if var.get() == True:           # 如果True綁定
        onoff.bind("<Button-1>",buttonClicked)
    else:                           # 如果False不綁定
        onoff.unbind("<Button-1>")
    
root = Tk()
root.title("ch11_7")                # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter")   # 建立按鈕tkinter
btn.pack(anchor=W,padx=10,pady=10)

var = BooleanVar()                  # 建立核取方塊
cbtn = Checkbutton(root,text="bind/unbind",variable=var,
                   command=lambda:toggle(btn))
cbtn.pack(anchor=W,padx=10)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_8.py

# ch11_8.py
from tkinter import *
def btnClicked1():                  # Button按鈕事件處理程式1
    print("Command event handler, I like tkinter")
def btnClicked2(event):             # Button按鈕事件處理程式2
    print("Bind event handler, I like tkinter")
    
root = Tk()
root.title("ch11_8")                # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter",   # 建立按鈕tkinter
             command=btnClicked1)
btn.pack(anchor=W,padx=10,pady=10)
btn.bind("<Button-1>",btnClicked2,add="+")  # 增加事件處理程式

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_9.py

# ch11_9.py
from tkinter import *
from tkinter import messagebox

def callback():
    res = messagebox.askokcancel("OKCANCEL","結束或取消?")
    if res == True:
        root.destroy()
    else:
        return
    
root = Tk()
root.title("ch11_9")
root.geometry("300x180")
root.protocol("WM_DELETE_WINDOW",callback)  # 更改協定綁定

root.mainloop()









print('------------------------------------------------------------')	#60個




