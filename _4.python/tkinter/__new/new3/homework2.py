from tkinter import *
wnd = Tk()
wnd.title('程式語言能力調查：')
def select():
    print('你的選項是 :', var.get())
ft = ('標楷體', 14)
Label(wnd, 
      text = "請選擇精通的程式語言: ", font = ft,
      justify = LEFT, padx = 20).pack()
place = [('Python語言', 1), ('C語言', 2),
          ('C++語言', 3),('Java語言', 4)]
var = IntVar()
var.set(3)
for item, val in place:
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = NW)
