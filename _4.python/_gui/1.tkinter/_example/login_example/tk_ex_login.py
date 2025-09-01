"""
各種登入範例

Label - Text - Button

"""

import tkinter as tk
from tkinter import messagebox

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("Login form")
window.geometry('450x440')
window.configure(bg='#333333')

def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tk.Frame(bg='#333333')

# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

# login.py

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
        window.destroy()
    else:
        tk.messagebox.showerror('注意','帳號或是密碼不正確！')
        userID.set('')	#清空帳號字串
        userPW.set('')	#清空密碼字串
        entID.focus_set()	#設entID成為作用元件
    
window = tk.Tk()
window.title('登入')
window.geometry('250x200')

tk.Label(window, text = '請輸入帳號：(小寫字母)').pack(anchor='w',pady=5)
userID=tk.StringVar()
entID= tk.Entry(window,textvariable=userID)
entID.pack(pady=5)
entID.bind('<KeyRelease>',fnID)	# KeyRelease事件綁定fnID事件處理函式
entID.focus_set()
tk.Label(window, text = '請輸入密碼：(數字)').pack(anchor='w',pady=5)
userPW=tk.StringVar()
entPW= tk.Entry(window,textvariable=userPW)
entPW.pack(pady=5)
entPW.bind('<KeyRelease>',fnPW) 	# KeyRelease事件綁定fnPW事件處理函式
btnLogin = tk.Button(window, text='登入', command=fnCheck).pack(pady=15)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
