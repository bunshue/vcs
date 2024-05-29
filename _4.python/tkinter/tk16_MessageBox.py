import sys

import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.colorchooser

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


print("------------------------------------------------------------")  # 60個

window = tk.Tk()


def hello():
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

B1 = tk.Button(window, text = "Say Hello", command = hello)
B1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

window = tk.Tk()
window.title('訊息方塊元件(messagebox)')
window.geometry('180x120+20+50')

def first():
    tk.messagebox.showinfo('顯示類對話方塊',
            '「顯示」類是以「show」開頭，只會顯示一個「確定」鈕。')

def second():
    tk.messagebox.askretrycancel('詢問類對話方塊', 
            '「詢問」類是以「ask」為開頭，伴隨2~3個按鈕來產生互動。')

tk.Button(window, text='顯示類對話方塊', command = first).pack(side = 'left', padx = 10)
tk.Button(window, text='詢問類對話方塊', command = second).pack(side = 'left')

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")
window.title("試題與測驗分析程式")

tk.messagebox.askokcancel(title="對話方塊", message="askokcancel")

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter.messagebox

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

from PIL import Image, ImageTk

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

"""
img = Image.open(filename)        # 開啟圖片
tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件

label = tk.Label(window, image=tk_img, width=200, height=200)  # 在 Lable 中放入圖片
label.pack()

html_gif = ImageTk.PhotoImage(file=filename)
tk.Label(window,image=html_gif).pack()

"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import tkinter.messagebox as msg

response = msg.askyesno('糟糕了!!!', '還好嗎？')

if (response == True):
	print('還 OK')
else:
	print('有點麻煩')

print("------------------------------------------------------------")  # 60個

import tkinter.messagebox as msg

window = tk.Tk()

window.withdraw()
response = msg.askyesno('糟糕!!!', '還好嗎？')

if(response==True):
	print('沒問題');
else:
	print('有問題');

print('------------------------------------------------------------')	#60個

from tkinter import messagebox

def newfile():
    messagebox.showinfo("開新檔案","可在此撰寫開新檔案程式碼")
    
def savefile():
    messagebox.showinfo("儲存檔案","可在此撰寫儲存檔案程式碼")
   
def about():
    messagebox.showinfo("程式說明","作者:洪錦魁")

window = tk.Tk()
window.title("ch18_36")
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
import tkinter
import tkinter.messagebox

def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tk.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tk.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象
    label = tk.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tk.Frame(top)
    # 创建按钮对象
    button1 = tk.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tk.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    
    # 开启主事件循环
    window.mainloop()

if __name__ == '__main__':
    main()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

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
'''
print("------------------------------------------------------------")  # 60個

def myMsg():
    tk.messagebox.showinfo("My Message Box","Python tkinter早安")
    
window = tk.Tk()
window.geometry("300x300")

tk.Button(window,text="Good Morning",command=myMsg).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

tk.messagebox.showinfo("Invoice Complete", "Invoice Complete")

print("------------------------------------------------------------")  # 60個

#from tkinter import messagebox
tk.messagebox.showinfo("Invoice Complete", "Invoice Complete")


print("------------------------------------------------------------")  # 60個

def myMsg():                    # 按Good Morning按鈕時執行
    tk.messagebox.showinfo("My Message Box","Python tkinter早安")
    
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

mainloop()



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



