import tkinter as tk
def fnKey(str):
    global exp		#宣告exp為全域變數
    exp+=str        #運算式為原運算式加新輸入的字串
    lblExp.config(text=exp)  #重設lblExp的文字為新運算式

def fnCls():
    global exp
    exp=''	#運算式設為空字串
    lblExp.config(text=exp)
    
def fnCal():
    global exp
    exp=str(eval(exp))	#用eval方法計算運算式並轉型為字串
    lblExp.config(text=exp)    

win = tk.Tk()
win.title('簡易計算機')
win.geometry('180x140')
lblExp=tk.Label(win,text='',width=18,relief='raised',bg='yellow')
lblExp.grid(row=0,column=0,columnspan=4)
tk.Button(win,text='7',width=3,command=lambda:fnKey('7')).grid(row=1,column=0)
tk.Button(win,text='8',width=3,command=lambda:fnKey('8')).grid(row=1,column=1)
tk.Button(win,text='9',width=3,command=lambda:fnKey('9')).grid(row=1,column=2)
tk.Button(win,text='/',width=3,command=lambda:fnKey('/')).grid(row=1,column=3)
tk.Button(win,text='4',width=3,command=lambda:fnKey('4')).grid(row=2,column=0)
tk.Button(win,text='5',width=3,command=lambda:fnKey('5')).grid(row=2,column=1)
tk.Button(win,text='6',width=3,command=lambda:fnKey('6')).grid(row=2,column=2)
tk.Button(win,text='*',width=3,command=lambda:fnKey('*')).grid(row=2,column=3)
tk.Button(win,text='1',width=3,command=lambda:fnKey('1')).grid(row=3,column=0)
tk.Button(win,text='2',width=3,command=lambda:fnKey('2')).grid(row=3,column=1)
tk.Button(win,text='3',width=3,command=lambda:fnKey('3')).grid(row=3,column=2)
tk.Button(win,text='-',width=3,command=lambda:fnKey('-')).grid(row=3,column=3)
tk.Button(win,text='0',width=3,command=lambda:fnKey('0')).grid(row=4,column=0)
tk.Button(win,text='C',width=3,command=fnCls).grid(row=4,column=1)
tk.Button(win,text="=",width=3,command=fnCal).grid(row=4,column=2)
tk.Button(win,text="+",width=3,command=lambda:fnKey('+')).grid(row=4,column=3)
exp=''   #預設運算式為空字串
win.mainloop()

