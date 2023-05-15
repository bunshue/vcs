from tkinter import *
from tkinter import messagebox

#create a window

window = Tk()
window.title('Login')
window.geometry('400x150+50+50')

#add textfields
l1=Label(window, text='Username:', font=(14))
l2=Label(window, text='Password:', font=(14))
l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=1, column=0, padx=5, pady=5)

#get username and password
username=StringVar()
password=StringVar()
t1=Entry(window, textvariable=username, font=(14))
t2=Entry(window, textvariable=password, font=(14), show='*')
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)

#add login and cancel buttons
b1=Button(window, text='Login', font=(14))
b2=Button(window, text='Cancel', font=(14))

#action when login button is clicked
def login():
    if username.get()=='admin' and password.get()=='admin':
        messagebox.showinfo(title='Login status', message='You have logged in.')
    else:
        messagebox.showerror(title='Login error', message='Username/Password is incorrect.')

b1=Button(window, command=login, text='Login', font=(14))

#action when cancel button is clicked
def cancel():
    status=messagebox.askyesno(title='Question', message='Do you want to close the window?')
    if status==True:
        window.destroy()
    else:
        messagebox.showwarning(title='Warning', message='Please login again!')

b2=Button(window, command=cancel, text='Cancel', font=(14))
b1.grid(row=2, column=1, sticky=W)
b2.grid(row=2, column=1, sticky=E)

window.mainloop()
