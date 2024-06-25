# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    pass
def usr_sign_up():
    pass

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 42")

accountL = tk.Label(window, text="Account ")  # account標籤
accountL.grid(row=0)
pwdL = tk.Label(window, text="Password")  # pwd標籤
pwdL.grid(row=1)

accountE = tk.Entry(window)  # 文字方塊account
pwdE = tk.Entry(window)  # 文字方塊pwd
pwdE = tk.Entry(window, show="*")  # 文字方塊pwd
accountE.grid(row=0, column=1)  # 定位文字方塊account
pwdE.grid(row=1, column=1)  # 定位文字方塊pwd

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 42")

def get_entry_text():
    print("取得帳號 :", entry1a.get())
    print("取得密碼 :", entry2a.get())


# 新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame3 = tk.Frame(window)
frame3.pack()

label1 = tk.Label(frame3, text="Username:")
entry1a = tk.Entry(frame3)

label2 = tk.Label(frame3, text="Password:")
entry2a = tk.Entry(frame3, show="*")

button = tk.Button(frame3, text="取得Entry資料", command=get_entry_text)

label1.pack()
entry1a.pack()
label2.pack()
entry2a.pack()
button.pack()

# 新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame4 = tk.Frame(window)
frame4.pack()

# get username and password
username = tk.StringVar()
password = tk.StringVar()
entry1b = tk.Entry(frame4, textvariable=username, font=(14))
entry2b = tk.Entry(frame4, textvariable=password, font=(14), show="*")
entry1b.pack()
entry2b.pack()


def get_entry_data():
    print("取得帳號 :", username.get())
    print("取得密碼 :", password.get())


button1 = tk.Button(frame4, command=get_entry_data, text="取得Entry資料", font=(20))
button1.pack()









window.mainloop()

