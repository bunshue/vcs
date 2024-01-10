from tkinter import *

wnd = Tk()
wnd.title('運動類型調查表')
def select():
    print('你的選項是 :', var.get())
ft = ('標楷體', 14)
Label(wnd, 
      text = "請選擇喜愛的運動: ", font = ft,
      justify = RIGHT, padx = 20).pack()
place = [('籃球', 1), ('桌球', 2),
          ('游泳', 3)]
var = IntVar()
var.set(3)

for item, val in place:
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = NE)
