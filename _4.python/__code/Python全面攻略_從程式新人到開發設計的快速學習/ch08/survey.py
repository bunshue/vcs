import tkinter as tk

def fnOk():
    lfrmSpot=tk.LabelFrame(win,text='勾選建議地點(可複選)：')
    lfrmSpot.pack(pady=10)
    for i in range(3):
        check[i]=tk.BooleanVar()	#設check[]元素值為布林值物件
        tk.Checkbutton(lfrmSpot,text=spots[i],variable=check[i]).pack(anchor='w')
def fnMsg():
    if ok.get()==True:
        msg='勾選的地點為：'
        for i in range(3):
            if check[i].get()==True:	#若check[i]元素值為True
                msg += (spots[i]+'、')	#將spots[i]元素值加入msg字串
        tk.messagebox.showinfo('訊息',msg[:len(msg)-1])
    else:
        tk.messagebox.showinfo('訊息','期盼下次你能參加')
    win.destroy()
    
win = tk.Tk()
win.title('旅遊問卷')
win.geometry('220x180')
ok=tk.BooleanVar()
chkOK=tk.Checkbutton(win,text='參加旅遊',variable=ok, command=fnOk).pack()
spots=['九份與金瓜石','日月潭','墾丁國家公園']
check={}
btnSend = tk.Button(win, text=' 送出 ', command=fnMsg).pack(pady=5)
win.mainloop()

