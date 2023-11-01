from tkinter import *
wnd = Tk()
wnd.title('GUI介面-Radiobutton')
def select():
    print('你的選項是 :', var.get())
ft = ('標楷體', 14)
Label(wnd, 
      text = "請選擇喜愛的景點: ", font = ft,
      justify = LEFT, padx = 20).pack()
place = [('宜蘭', 1), ('台北', 2),
          ('高雄', 3)]
var = IntVar()
var.set(3)
for item, val in place:
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = W)
