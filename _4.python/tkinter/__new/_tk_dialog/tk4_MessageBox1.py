import sys

import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog

print("------------------------------------------------------------")  # 60個
'''
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
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def confirm_exit():
    if tkinter.messagebox.askyesno("關閉窗口","確認關閉窗口嗎"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", confirm_exit)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

window.withdraw()

response = tk.messagebox.askyesno('糟糕!!!', '還好嗎？')

if(response == True):
    print('沒問題');
else:
    print('有問題');

print('------------------------------------------------------------')	#60個

def newfile():
    tkinter.messagebox.showinfo("開新檔案","可在此撰寫開新檔案程式碼")
    
def savefile():
    tkinter.messagebox.showinfo("儲存檔案","可在此撰寫儲存檔案程式碼")
   
def about():
    tkinter.messagebox.showinfo("程式說明","作者:洪錦魁")

window = tk.Tk()
window.title("")
window.geometry("300x160")          # 視窗寬300高160

menu = tk.Menu(window)                 # 建立功能表物件
window.config(menu=menu)

filemenu = tk.Menu(menu)               # 建立檔案功能表
menu.add_cascade(label="檔案",menu=filemenu)
filemenu.add_command(label="開新檔案",command=newfile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="儲存檔案",command=savefile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="結束",command=window.destroy)

helpmenu = tk.Menu(menu)               # 建立說明功能表
menu.add_cascade(label="說明",menu=helpmenu)
helpmenu.add_command(label="程式說明",command=about)

window.mainloop()

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

# 创建顶层窗口
window = tk.Tk()
# 设置窗口大小
window.geometry('240x160')
# 设置窗口标题
window.title('小游戏')

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
window.title('訊息方塊元件(messagebox)')
window.geometry('180x120+20+50')

def answer():
    tk.messagebox.showerror('顯示類訊息框', '這是messagebox.showerror的訊息框')

def callback():
    tk.messagebox.askyesno('詢問類訊息框', '這是messagebox.askyesno的訊息框')

tk.Button(window, text='顯示詢問訊息框的外觀', command = callback).pack(side = 'left', padx = 10)
tk.Button(window, text='顯示錯誤訊息框的外觀', command = answer).pack(side = 'left')

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

def myMsg():
    tk.messagebox.showinfo("My Message Box","Python tkinter早安")
    
window = tk.Tk()
window.geometry("300x300")

tk.Button(window,text="Good Morning",command=myMsg).pack()

print("------------------------------------------------------------")  # 60個

def newfile():
    tk.messagebox.showinfo("開新檔案","可在此撰寫開新檔案程式碼")
    
def savefile():
    tk.messagebox.showinfo("儲存檔案","可在此撰寫儲存檔案程式碼")
   
def about():
    tk.messagebox.showinfo("程式說明","作者:洪錦魁")

menu = tk.Menu(window)                 # 建立功能表物件
window.config(menu=menu)

filemenu = tk.Menu(menu)               # 建立檔案功能表
menu.add_cascade(label="檔案",menu=filemenu)
filemenu.add_command(label="開新檔案",command=newfile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="儲存檔案",command=savefile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="結束",command=window.destroy)

helpmenu = tk.Menu(menu)               # 建立說明功能表
menu.add_cascade(label="說明",menu=helpmenu)
helpmenu.add_command(label="程式說明",command=about)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

def answer():
    tk.messagebox.showerror('顯示類訊息框',
            '這是messagebox.showerror的訊息框')

def callback():
    tk.messagebox.askyesno('詢問類訊息框', 
            '這是messagebox.askyesno的訊息框')

tk.Button(window, text='顯示詢問訊息框的外觀', command =
          callback).pack(side = 'left', padx = 10)
tk.Button(window, text='顯示錯誤訊息框的外觀', command =
          answer).pack(side = 'left')

window.mainloop()

print("------------------------------------------------------------")  # 60個

# end.py

def fnEnd():
    res = tkinter.messagebox.askokcancel('注意','確定要結束程式嗎？')
    if(res == True):	#若傳回值為 True
        window.destroy()   #結束程式執行
        
window=tk.Tk()
window.geometry('300x150')
window.title('對話方塊')

lblTitle=tk.Label(window, text = '按鈕結束程式',font=('標楷體', 16))
btnEnd=tk.Button(window, text = '結束',pady=5,padx=10,command=fnEnd)
lblTitle.pack(pady=20)
btnEnd.pack(pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter.messagebox
import tkinter.simpledialog

tkinter.messagebox.showinfo("showinfo", "This is an info msg")

tkinter.messagebox.showwarning("showwarning", "This is a warning")

tkinter.messagebox.showerror("showerror", "This is an error")

isYes = tkinter.messagebox.askyesno("ashyesno", "Continue?")
print(isYes)

isOK = tkinter.messagebox.askokcancel("ashokcancle", "OK?")
print(isOK)

isYesNoCancel = tkinter.messagebox.askyesnocancel(
    "askyesnocancel", "Yes, No, Cancel?") 
print(isYesNoCancel)

name = tkinter.simpledialog.askstring(
    "askstring", "Enter your name")
print(name)

age = tkinter.simpledialog.askinteger(
    "askinteger", "Enter your age")
print(age)

weight = tkinter.simpledialog.askfloat(
    "askfloat", "Enter your weight")
print(weight)

print("------------------------------------------------------------")  # 60個

import tkinter.messagebox									# 匯入tkMessageBox模組

def cmd():										# 按鈕訊息處理函數
	global n									# 使用全局變數n
	global buttontext								# 使用全局變數buttontext
	n = n + 1
	if n == 1:									# 判斷n的值，顯示不同的訊息框
		tkinter.messagebox.askokcancel('Python Tkinter','askokcancel')		# 使用askokcancel函數
		buttontext.set('skquestion')						# 變更按鈕上的文字
	elif n == 2:
		tk.messagebox.askquestion('Python Tkinter','skquestion')			# 使用askquestion函數
		buttontext.set('askyesno')
	elif n == 3:
		tk.messagebox.askyesno('Python Tkinter','askyesno')			# 使用askyesno函數
		buttontext.set('showerror')
	elif n == 4:
		tk.messagebox.showerror('Python Tkinter','showerror')			# 使用showerror函數
		buttontext.set('showinfo')
	elif n == 5:
		tk.messagebox.showinfo('Python Tkinter','showinfo')			# 使用showinfo函數
		buttontext.set('showwarning')
	else :
		n = 0									# 將n給予值為0重新開始循環
		tk.messagebox.showwarning('Python Tkinter','showwarning')		# 使用showwarning函數
		buttontext.set('askokcancel')
n = 0											# 為n賦初值
window = tk.Tk()

buttontext = tk.StringVar() # 產生關聯按鈕文字的變數
buttontext.set('askokcancel')								# 設定buttontext值
button = tk.Button(window,								# 產生按鈕
		textvariable = buttontext,						# 設定關聯變數
		command = cmd)								# 設定事件處理函數
button.pack()

window.mainloop()										# 進入訊息循環

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

'''



print("------------------------------------------------------------")  # 60個



"""
tk.messagebox.askokcancel(title="對話方塊", message="askokcancel")

tk.messagebox.showinfo("Invoice Complete", "Invoice Complete")

tkinter.messagebox.showinfo("Error","This word is not present in our lexicon\nDouble check it.")
tkinter.messagebox.showinfo("Error","This word is not present in our lexicon showing results for %s instead"% "aaaaa")
tkinter.messagebox.showinfo('圓周長','圓周長為 {:.2f} {}'.format(a,u))
tkinter.messagebox.showinfo('圓面積','圓面積為 {:.2f} 平方{}'.format(a,u))
tkinter.messagebox.showinfo('訊息',msg[:len(msg)-1])
tkinter.messagebox.showinfo('訊息','期盼下次你能參加')
        messagebox.showinfo("Notebook","歡迎使用Notebook")

tkinter.messagebox.askokcancel('注意','你的BMI指數為：{} {}'.format(bmi, msg))


tkinter.messagebox.showinfo('AAAAAAAA')
tkinter.messagebox.showinfo("Check Sudoku Solution",  "The solution is valid")
tkinter.messagebox.showwarning("Check Sudoku Solution", "The solution is invalid")

"""



