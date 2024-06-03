"""
Button 排列 與 空函數


"""


import os
import sys

import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog

print('------------------------------------------------------------')	#60個

def button00Click():
    print('你按了button00')
    tk.messagebox.showinfo('訊息框', "showinfo")
    tk.messagebox.showwarning('訊息框', "showwarning")
    tk.messagebox.showerror('訊息框', "showerror")
    result =tk.messagebox.askquestion('訊息框', "askquestion")
    print(result)
    result=tk.messagebox.askokcancel('訊息框', "askokcancel")
    print(result)
    result=tk.messagebox.askyesno('訊息框', "showeraskyesnoror")
    print(result)
    result=tk.messagebox.askretrycancel('訊息框', "askretrycancel")
    print(result)

def button01Click():
    print('你按了button01')

def button02Click():
    print('你按了button02')

def button03Click():
    print('你按了button03')

def button04Click():
    print('你按了button04')

def button05Click():
    print('你按了button05')

def button10Click():
    print('你按了button10')

def button11Click():
    print('你按了button11')

def button12Click():
    print('你按了button12')

def button13Click():
    print('你按了button13')

def button14Click():
    print('你按了button14')

def button15Click():
    print('你按了button15')

def button20Click():
    print('你按了button20')

def button21Click():
    print('你按了button21')

def button22Click():
    print('你按了button22')

def button23Click():
    print('你按了button23')

def button24Click():
    print('你按了button24')
    #清空Text
    text1.delete(1.0, 'end')

def button25Click():
    #print('你按了button25')
    message = "匯入生產資料 完成\n"
    #print(message)
    text1.insert('end', message)


window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W)+'x'+str(H)
#size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
window.title('功能測試')

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

x_st = 50
y_st = 200
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, width = w, height = h, command = button00Click, text = '測試00')
button00.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01 = tk.Button(window, width = w, height = h, command = button01Click, text = '----')
button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button02 = tk.Button(window, width = w, height = h, command = button02Click, text = '----')
button02.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button03 = tk.Button(window, width = w, height = h, command = button03Click, text = '----')
button03.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button04 = tk.Button(window, width = w, height = h, command = button04Click, text = '----')
button04.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button05 = tk.Button(window, width = w, height = h, command = button05Click, text = '----')
button05.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button00.place(x = x_st + dx * 0, y = y_st + dy * 0)
button01.place(x = x_st + dx * 1, y = y_st + dy * 0)
button02.place(x = x_st + dx * 2, y = y_st + dy * 0)
button03.place(x = x_st + dx * 3, y = y_st + dy * 0)
button04.place(x = x_st + dx * 4, y = y_st + dy * 0)
button05.place(x = x_st + dx * 5, y = y_st + dy * 0)

button10 = tk.Button(window, width = w, height = h, command = button10Click, text = '----')
button10.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button11 = tk.Button(window, width = w, height = h, command = button11Click, text = '----')
button11.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button12 = tk.Button(window, width = w, height = h, command = button12Click, text = '----')
button12.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button13 = tk.Button(window, width = w, height = h, command = button13Click, text = '----')
button13.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button14 = tk.Button(window, width = w, height = h, command = button14Click, text = '----')
button14.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button15 = tk.Button(window, width = w, height = h, command = button15Click, text = '----')
button15.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button10.place(x = x_st + dx * 0, y = y_st + dy * 1)
button11.place(x = x_st + dx * 1, y = y_st + dy * 1)
button12.place(x = x_st + dx * 2, y = y_st + dy * 1)
button13.place(x = x_st + dx * 3, y = y_st + dy * 1)
button14.place(x = x_st + dx * 4, y = y_st + dy * 1)
button15.place(x = x_st + dx * 5, y = y_st + dy * 1)

button20 = tk.Button(window, width = w, height = h, command = button20Click, text = '----')
button20.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button21 = tk.Button(window, width = w, height = h, command = button21Click, text = '----')
button21.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button22 = tk.Button(window, width = w, height = h, command = button22Click, text = '----')
button22.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button23 = tk.Button(window, width = w, height = h, command = button23Click, text = '----')
button23.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button24 = tk.Button(window, width = w, height = h, command = button24Click, text = '----')
button24.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button25 = tk.Button(window, width = w, height = h, command = button25Click, text = '----')
button25.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button20.place(x = x_st + dx * 0, y = y_st + dy * 2)
button21.place(x = x_st + dx * 1, y = y_st + dy * 2)
button22.place(x = x_st + dx * 2, y = y_st + dy * 2)
button23.place(x = x_st + dx * 3, y = y_st + dy * 2)
button24.place(x = x_st + dx * 4, y = y_st + dy * 2)
button25.place(x = x_st + dx * 5, y = y_st + dy * 2)

# 加入 Text
text1 = tk.Text(window, width = 100, height = 24)  # 放入多行輸入框
text1.pack()
text1.place(x = x_st + dx * 0, y = y_st + dy * 3 + 10)

print("------------------------------------------------------------")  # 60個


ans = tkinter.messagebox.showinfo(title = 'IMS', message = "IMS show information")
print("取得 info 結果 : ", ans)
"""
ans = tkinter.messagebox.showwarning('IMS', "IMS show warning")
print("取得 warning 結果 : ", ans)

ans = tkinter.messagebox.showerror('IMS', "IMS show error")
print("取得 error 結果 : ", ans)

ans = tkinter.messagebox.askquestion('IMS', "IMS ask question")
print("取得 question 結果 : ", ans)

ans = tkinter.messagebox.askokcancel('IMS', "IMS ask ok cancel")
print("取得 ok/cancel 結果 : ", ans)

ans = tkinter.messagebox.askyesno('IMS', "IMS ask yes no")
print("取得 yes/no 結果 : ", ans)

ans = tkinter.messagebox.askyesnocancel('IMS', "IMS ask yes no cancel") 
print("取得 yes/no/cancel 結果 : ", ans)

ans = tkinter.messagebox.askretrycancel("IMS", "IMS ask retry cancel")
print("取得 retry/cancel 結果 : ", ans)

ans = tkinter.simpledialog.askstring("askstring", "Enter your name")
print("取得 字串 結果 : ", ans)

ans = tkinter.simpledialog.askinteger("askinteger", "Enter your age")
print("取得 整數 結果 : ", ans)

ans = tkinter.simpledialog.askfloat("askfloat", "Enter your weight")
print("取得 浮點數 結果 : ", ans)
"""



print("------------------------------------------------------------")  # 60個

print('訊息方塊元件(messagebox)')

def first():
    tk.messagebox.showinfo('顯示類對話方塊',
            '「顯示」類是以「show」開頭，只會顯示一個「確定」鈕。')

def second():
    tk.messagebox.askretrycancel('詢問類對話方塊', 
            '「詢問」類是以「ask」為開頭，伴隨2~3個按鈕來產生互動。')

tk.Button(window, text='顯示類對話方塊', command = first).pack()
tk.Button(window, text='詢問類對話方塊', command = second).pack()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

