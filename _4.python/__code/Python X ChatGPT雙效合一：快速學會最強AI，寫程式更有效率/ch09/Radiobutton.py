from tkinter import *
wnd = Tk()
wnd.title('Radiobutton元件')
def select():
    print('你的選項是 :', var.get())

ft = ('標楷體', 14)
Label(wnd, 
      text = "請問您的最高學歷: ", font = ft,
      justify = LEFT, padx = 20).pack()
place = [('博士', 1), ('碩士', 2),('大學', 3),
          ('高中', 4),('國中', 5),('國小', 6)]
var = IntVar()
var.set(2)
for item, val in place:
    Radiobutton(wnd, text = item, value = val,
        font = ft, variable = var, padx = 20,
        command = select).pack(anchor = W)
mainloop()
