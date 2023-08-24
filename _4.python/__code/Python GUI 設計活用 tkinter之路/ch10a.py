# ch10_1.py
from tkinter import *

root = Tk()
root.title("ch10_1")

myText = "2016年12月,我一個人訂了機票和船票,開始我的南極旅行"
msg = Message(root,bg="yellow",text=myText,
              font="times 12 italic")
msg.pack(padx=10,pady=10)

root.mainloop()





#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_2.py

# ch10_2.py
from tkinter import *

root = Tk()
root.title("ch10_2")

var = StringVar()
msg = Message(root,textvariable=var,relief=RAISED)
var.set("2016年12月,我一個人訂了機票和船票,開始我的南極旅行")
msg.pack(padx=10,pady=10)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_3.py

# ch10_3.py
from tkinter import *

root = Tk()
root.title("ch10_3")

var = StringVar()
msg = Message(root,textvariable=var,relief=RAISED)
var.set("2016年12月,我一個人訂了機票和船票,開始我的南極旅行")
msg.config(bg="yellow")
msg.pack(padx=10,pady=10)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_4.py

# ch10_4.py
from tkinter import *
from tkinter import messagebox

def myMsg():                    # 按Good Morning按鈕時執行
    messagebox.showinfo("My Message Box","Python tkinter早安")
    
window = Tk()
window.title("ch10_4")          # 視窗標題
window.geometry("300x160")      # 視窗寬300高160

Button(window,text="Good Morning",command=myMsg).pack()

window.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_5.py

# ch10_5.py
from tkinter import *
from tkinter import messagebox

def myMsg1():
    ret = messagebox.askretrycancel("Test1","安裝失敗,再試一次?")
    print("安裝失敗",ret)
def myMsg2():
    ret = messagebox.askyesnocancel("Test2","編輯完成,是或否或取消?")
    print("編輯完成",ret)
root = Tk()
root.title("ch10_5")          # 視窗標題

Button(root,text="安裝失敗",command=myMsg1).pack()
Button(root,text="編輯完成",command=myMsg2).pack()

root.mainloop()







print('------------------------------------------------------------')	#60個





