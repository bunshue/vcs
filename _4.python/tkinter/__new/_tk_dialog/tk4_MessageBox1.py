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

response = tk.messagebox.askyesno('糟糕!!!', '還好嗎？')

if(response == True):
    print('你按了 Yes');
else:
    print('你按了 No');

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

window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 5 訊息方塊元件(messagebox)')

def answer():
    tk.messagebox.showerror('顯示類訊息框', '這是messagebox.showerror的訊息框')

def callback():
    tk.messagebox.askyesno('詢問類訊息框', '這是messagebox.askyesno的訊息框')

tk.Button(window, text='顯示詢問訊息框的外觀', command = callback).pack()
tk.Button(window, text='顯示錯誤訊息框的外觀', command = answer).pack()

window.mainloop()



window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 1')

def answer():
    tk.messagebox.showerror('顯示類訊息框', '這是messagebox.showerror的訊息框')

def callback():
    tk.messagebox.askyesno('詢問類訊息框',  '這是messagebox.askyesno的訊息框')

tk.Button(window, text='顯示詢問訊息框的外觀', command = callback).pack()
tk.Button(window, text='顯示錯誤訊息框的外觀', command = answer).pack()

window.mainloop()


print("------------------------------------------------------------")  # 60個

""" lack pic
def more():
    if choice.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        tk.messagebox.showinfo("cattle的簡介",str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        tk.messagebox.showinfo("deer的簡介",str2)
    
window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 6')

lb = tk.Label(window,text="請點選想了解的動物簡介:").pack()
choice = tk.IntVar()
choice.set(0)

pic1 = tk.PhotoImage(file="cattle.gif")
pic2 = tk.PhotoImage(file="deer.gif")

tk.Radiobutton(window,image=pic1,variable=choice,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=choice,value=1).pack()
tk.Button(window,text="進一步了解", command=more).pack()

window.mainloop()
"""

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

import tkinter.messagebox
import tkinter.simpledialog

print('messagebox 1 顯示訊息')
tk.messagebox.showinfo("訊息框", "顯示訊息")
tk.messagebox.showinfo(title="訊息框", message="顯示訊息")

tk.messagebox.showwarning("showwarning", "This is a warning")

tk.messagebox.showerror("showerror", "This is an error")

print('messagebox 1 問答')

isYes = tk.messagebox.askyesno("ashyesno", "Continue?")
print(isYes)

isOK = tk.messagebox.askokcancel("ashokcancle", "OK?")
print(isOK)

isYesNoCancel = tk.messagebox.askyesnocancel("askyesnocancel", "Yes, No, Cancel?") 
print(isYesNoCancel)

name = tkinter.simpledialog.askstring("askstring", "Enter your name")
print(name)

age = tkinter.simpledialog.askinteger("askinteger", "Enter your age")
print(age)

weight = tkinter.simpledialog.askfloat("askfloat", "Enter your weight")
print(weight)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



"""
簡易單行 messagebox 指令


tk.messagebox.askokcancel(title="對話方塊", message="askokcancel")

tk.messagebox.showinfo("Error","This word is not present in our lexicon showing results for %s instead"% "aaaaa")
tk.messagebox.showinfo('圓周長','圓周長為 {:.2f} {}'.format(a,u))
tk.messagebox.showinfo('圓面積','圓面積為 {:.2f} 平方{}'.format(a,u))
tk.messagebox.showinfo('訊息',msg[:len(msg)-1])


tk.messagebox.askokcancel('注意','你的BMI指數為：{} {}'.format(bmi, msg))

tk.messagebox.askokcancel('Python Tkinter','askokcancel')		# 使用askokcancel函數
tk.messagebox.askquestion('Python Tkinter','skquestion')			# 使用askquestion函數
tk.messagebox.askyesno('Python Tkinter','askyesno')			# 使用askyesno函數
tk.messagebox.showerror('Python Tkinter','showerror')			# 使用showerror函數
tk.messagebox.showinfo('Python Tkinter','showinfo')			# 使用showinfo函數
tk.messagebox.showwarning('Python Tkinter','showwarning')		# 使用showwarning函數



"""







import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog

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




"""
新進mix


ret = messagebox.askretrycancel("Test1","安裝失敗,再試一次?")
print("安裝失敗",ret)

ret = messagebox.askyesnocancel("Test2","編輯完成,是或否或取消?")
print("編輯完成",ret)

import tkinter.messagebox as tkMessageBox
#import tkinter.messagebox

from tkinter import messagebox


from tkinter import filedialog, messagebox

import tkinter.messagebox as tkmessagebox






"""


