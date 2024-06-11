
import tkinter as tk


print("------------------------------------------------------------")  # 60個

print('綁定鍵盤滑鼠事件 Button')

print("------------------------------------------------------------")  # 60個

def enter(event):                       # Enter事件處理程式
    x.set("滑鼠進入Exit功能鈕")   
def leave(event):                       # Leave事件處理程式
    x.set("滑鼠離開Exit功能鈕")
    
window = tk.Tk()
window.geometry("600x400")

button1 = tk.Button(window,text="離開",command=window.destroy)
button1.pack(pady=30)
button1.bind("<Enter>",enter)               # 進入綁定enter
button1.bind("<Leave>",leave)               # 離開綁定leave

x = tk.StringVar()
lab = tk.Label(window,textvariable=x,        # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(pady=30)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def buttonClicked1():                  # Button按鈕事件處理程式1
    print("Command event handler, I like tkinter")
def buttonClicked2(event):             # Button按鈕事件處理程式2
    print("Bind event handler, I like tkinter")
    
window = tk.Tk()
window.geometry("600x400")

button1 = tk.Button(window,text="tkinter",command=buttonClicked1)
button1.pack(anchor=tk.W,padx=10,pady=10)

button1.bind("<Button-1>",buttonClicked2,add="+")  # 增加事件處理程式

window.mainloop()

print("------------------------------------------------------------")  # 60個


def buttonClicked(event):           # Button按鈕事件處理程式
    print("I like tkinter")

# 所傳遞的物件onoff是btn物件    
def toggle(onoff):                  # 切換綁定
    if var.get() == True:           # 如果True綁定
        onoff.bind("<Button-1>",buttonClicked)
    else:                           # 如果False不綁定
        onoff.unbind("<Button-1>")
    
window = tk.Tk()
window.geometry("600x400")

button1 = tk.Button(window,text="tkinter")
button1.pack(anchor=W,padx=10,pady=10)

var = tk.BooleanVar()                  # 建立核取方塊
button2 = tk.Checkbutton(window,text="bind/unbind",variable=var,
                   command=lambda:toggle(button1))
button2.pack(anchor=tk.W,padx=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個



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
title = '綁定鍵盤滑鼠事件 Window'
window.title(title)

button1 = tk.Button(window,text="Click me")
button1.pack()
button1.bind("<Button-1>",buttonClicked)  # 按一下Click me綁定buttonClicked方法

varPython = tk.BooleanVar()
cbnPython = tk.Checkbutton(window,text="Python",variable=varPython, command=pythonClicked)
cbnPython.pack()

varJava = tk.BooleanVar()
cbnJava = tk.Checkbutton(window,text="Java",variable=varJava, command=javaClicked)
cbnJava.pack()
lab = tk.Label(window,bg="yellow",fg="blue", height=2,width=12, font="Times 16 bold")
lab.pack()

window.mainloop()



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


