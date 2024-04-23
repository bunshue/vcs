import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

ans = tkinter.messagebox.showinfo(title = 'IMS', message = "IMS show information")
print("取得 info 結果 : ", ans)
'''
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
'''


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# MessageBox測試

my_mesg = "大雄：1964年8月7日\n哆啦A夢：2112年9月3日\n靜香：1964年12月2日\n小夫：1964年2月29日\n胖虎：1964年6月15日\n哆啦美：2114年12月2日"
msg = tk.Message(window, text = my_mesg)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def confirm_exit():
    if tkinter.messagebox.askyesno("關閉窗口","確認關閉窗口嗎"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", confirm_exit)

window.mainloop()
