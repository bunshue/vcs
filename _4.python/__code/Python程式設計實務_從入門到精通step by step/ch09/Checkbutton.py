from tkinter import *
wnd = Tk()
wnd.title('Checkbutton 核取方塊')

def check(): #回應核取方塊變數狀態
   print('這學期預定選修的科目包括:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=Label(wnd, text = '選修的科目：', font = ft1).pack()
item1 = '人工智慧'
var1 = StringVar()
chk1 = Checkbutton(wnd, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk1.pack()
item2 = '程式語言'
var2 = StringVar()
chk2 = Checkbutton(wnd, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.pack()
item3 = '數位行銷'
var3 = StringVar()
chk3 = Checkbutton(wnd, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.pack()
btnShow = Button(wnd, text = '列出選修結果', font = ft2,
    command = check)
btnShow.pack()
mainloop()
