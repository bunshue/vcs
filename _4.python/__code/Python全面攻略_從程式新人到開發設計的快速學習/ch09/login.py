import tkinter as tk

def fnID(e):
    code=e.keycode		#取得字元的鍵盤碼
    if(code==8 or code==46):	#若是退位或刪除鍵就離開函式
        return
    if(e.keysym=='Return'): 	#若是 Enter 鍵
        entPW.focus_set()		#設entPW成為作用元件
        return  
    id=userID.get()			#取得帳號字串
    if(e.char.islower()==False):   #若輸入字元不是小寫字元
        userID.set(id.replace(e.char,''))  #重設帳號字串將輸入字元以空字串取代
        tk.messagebox.showerror('注意','請輸入小寫字母！')

def fnPW(e):
    sym=e.keysym		#取得字元的按鍵名稱
    if(sym=='BackSpace' or sym=='Delete'): 	#若是退位或刪除鍵就離開函式
        return
    pw=userPW.get()
    if(e.char.isdigit()==False):	#若輸入字元不是數字
        userPW.set(pw.replace(e.char,''))  #重設密碼字串將輸入字元以空字串取代
        tk.messagebox.showerror('注意','請輸入數字！')

def fnCheck():
    id=userID.get()
    pw=userPW.get()
    if (id == 'love' and pw == '1314'):#若帳號和密碼字串都正確
        tk.messagebox.showinfo('歡迎','帳號和密碼正確！')
        win.destroy()
    else:
        tk.messagebox.showerror('注意','帳號或是密碼不正確！')
        userID.set('')	#清空帳號字串
        userPW.set('')	#清空密碼字串
        entID.focus_set()	#設entID成為作用元件
    
win = tk.Tk()
win.title('登入')
win.geometry('220x180')
tk.Label(win, text = '請輸入帳號：(小寫字母)').pack(anchor='w',pady=5)
userID=tk.StringVar()
entID= tk.Entry(win,textvariable=userID)
entID.pack(pady=5)
entID.bind('<KeyRelease>',fnID)	# KeyRelease事件綁定fnID事件處理函式
entID.focus_set()
tk.Label(win, text = '請輸入密碼：(數字)').pack(anchor='w',pady=5)
userPW=tk.StringVar()
entPW= tk.Entry(win,textvariable=userPW)
entPW.pack(pady=5)
entPW.bind('<KeyRelease>',fnPW) 	# KeyRelease事件綁定fnPW事件處理函式
btnLogin = tk.Button(win, text='登入', command=fnCheck).pack(pady=15)
win.mainloop()

