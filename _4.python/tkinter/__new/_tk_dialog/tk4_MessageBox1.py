import sys

import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 1')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def confirm_exit():
    if tk.messagebox.askyesno("關閉窗口","確認關閉窗口嗎"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", confirm_exit)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 2')

window.withdraw()   # 何意? 不顯示視窗? 相對應於 window.mainloop??



print("------------------------------------------------------------")  # 60個

"""
使用tkinter创建GUI
- 顶层窗口
- 控件
- 布局
- 事件回调

"""

flag = True

# 修改标签上的文字
def change_label_text():
    global flag
    flag = not flag
    color, msg = ('red', 'Hello, world!')\
        if flag else ('blue', 'Goodbye, world!')
    label.config(text=msg, fg=color)

# 确认退出
def confirm_to_quit():
    if tk.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
        window.quit()

window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 4 小遊戲')

# 创建标签对象
label = tk.Label(window, text='Hello, world!', font='Arial -32', fg='red')
label.pack(expand=1)
# 创建一个装按钮的容器
panel = tk.Frame(window)
# 创建按钮对象
button1 = tk.Button(panel, text='修改', command=change_label_text)
button1.pack(side='left')
button2 = tk.Button(panel, text='退出', command=confirm_to_quit)
button2.pack(side='right')
panel.pack(side='bottom')

window.mainloop()

print("------------------------------------------------------------")  # 60個

def fnEnd():
    res = tk.messagebox.askokcancel('注意','確定要結束程式嗎？')
    if(res == True):	#若傳回值為 True
        window.destroy()   #結束程式執行
        
window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 1')

lblTitle=tk.Label(window, text = '按鈕結束程式',font=('標楷體', 16))
btnEnd=tk.Button(window, text = '結束',pady=5,padx=10,command=fnEnd)
lblTitle.pack(pady=20)
btnEnd.pack(pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個




""" OK
ans = tkinter.messagebox.showinfo(title = 'IMS', message = "顯示 訊息 information")
print("取得 info 結果 : ", ans)

ans = tkinter.messagebox.showwarning('IMS', "顯示 警告 warning")
print("取得 warning 結果 : ", ans)

ans = tkinter.messagebox.showerror('IMS', "顯示 錯誤 error")
print("取得 error 結果 : ", ans)

ans = tkinter.messagebox.askquestion('IMS', "詢問 問題 Yes/No askquestion")
print("取得 question 結果 : ", ans)

ans = tkinter.messagebox.askokcancel('IMS', "詢問 OK/Cancel askokcancel")
print("取得 ok/cancel 結果 : ", ans)

ans = tkinter.messagebox.askyesno('IMS', "詢問 Yes/No askyesno")
print("取得 yes/no 結果 : ", ans)

ans = tkinter.messagebox.askyesnocancel('IMS', "詢問 Yes/No/Cancel askyesnocancel") 
print("取得 yes/no/cancel 結果 : ", ans)

ans = tkinter.messagebox.askretrycancel("IMS", "詢問 Retry/Cancel askretrycancel")
print("取得 retry/cancel 結果 : ", ans)

ans = tkinter.simpledialog.askstring("請輸入字串", "請輸入字串")
print("取得 字串 結果 : ", ans)

ans = tkinter.simpledialog.askinteger("請輸入整數", "請輸入整數")
print("取得 整數 結果 : ", ans)

ans = tkinter.simpledialog.askfloat("請輸入浮點數", "請輸入浮點數")
print("取得 浮點數 結果 : ", ans)
"""


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



