"""
# 以Menu元件建置功能表

"""

import sys
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="檔案(F)", menu=menu1)
menu1.add_command(label="開啟新檔", command=lambda: print("你按了 開啟新檔"))
menu1.add_command(label="開啟舊檔", command=lambda: print("你按了 開啟舊檔"))
menu1.add_command(label="儲存檔案", command=lambda: print("你按了 儲存檔案"))
menu1.add_command(label="另存新檔", command=lambda: print("你按了 另存新檔"))
menu1.add_separator()  # 增加分隔線
menu1.add_command(label="離開", command=window.destroy)

# 第2排功能選單 Edit
menu2 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="編輯(E)", menu=menu2)
menu2.add_command(label="復原", command=lambda: print("你按了 復原"))
menu1.add_separator()  # 增加分隔線
menu2.add_command(label="剪下", command=lambda: print("你按了 剪下"))
menu2.add_command(label="複製", command=lambda: print("你按了 複製"))
menu2.add_command(label="貼上", command=lambda: print("你按了 貼上"))

# 第3排功能選單 Help
menu3 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="說明(H)", menu=menu3)
menu3.add_command(label="關於(A)", command=lambda: print("你按了 關於"))

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="檔案(F)", menu=menu1)
menu1.add_command(label="開新檔案", command=lambda: print("你按了 開新檔案"), accelerator="Ctrl+N")
menu1.add_separator()  # 增加分隔線
menu1.add_command(label="離開", command=window.destroy)

window.bind(
    "<Control-N>", lambda event: messagebox.showinfo("New File", "開新檔案")  # 快捷鍵綁定
)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="檔案(F)", menu=menu1)

# 首先在File功能表內建立find子功能表物件
# 第2排功能選單
menu2 = tk.Menu(menu1, tearoff=False)  # 取消分隔線
menu2.add_command(label="尋找下一筆", command=lambda: print("你按了 尋找下一筆"))
menu2.add_command(label="尋找上一筆", command=lambda: print("你按了 尋找上一筆"))
menu1.add_cascade(label="尋找", menu=menu2)

menu1.add_separator()  # 增加分隔線
menu1.add_command(label="離開", command=window.destroy)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個


def status():  # 設定是否顯示狀態列
    if demoStatus.get():
        statusLabel.pack(side=tk.BOTTOM, fill=tk.X)
    else:
        statusLabel.pack_forget()


window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=False)
menu0.add_cascade(label="檔案(F)", menu=menu1)
menu1.add_command(label="離開", command=window.destroy)

# 第2排功能選單
menu2 = tk.Menu(menu0, tearoff=False)
menu0.add_cascade(label="View", menu=menu2)
# 在View功能表內建立Check menu button
demoStatus = tk.BooleanVar()
demoStatus.set(True)
menu2.add_checkbutton(label="Status", command=status, variable=demoStatus)

statusVar = tk.StringVar()
statusVar.set("顯示")
statusLabel = tk.Label(window, textvariable=statusVar, relief="raised")
statusLabel.pack(side=tk.BOTTOM, fill=tk.X)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=False)
menu0.add_cascade(label="檔案(F)", menu=menu1)
menu1.add_command(label="離開", command=window.destroy)

# 建立工具列
toolbar = tk.Frame(window, relief=tk.RAISED, borderwidth=3)
# 在工具列內建立按紐
tk_image = tk.PhotoImage(file="__new/sun.gif")
exitBtn = tk.Button(toolbar, image=tk_image, command=window.destroy)
exitBtn.pack(side=tk.LEFT, padx=3, pady=3)  # 包裝按鈕

toolbar.pack(side=tk.TOP, fill=tk.X)  # 包裝工具列

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=False)
menu0.add_cascade(label="檔案(F)", menu=menu1)
menu1.add_command(label="新增檔案", command=lambda: print("你按了 新增檔案"))
menu1.add_command(label="開啟檔案", command=lambda: print("你按了 開啟檔案"))
menu1.add_separator()  # 增加分隔線


# 第2排功能選單
menu2 = tk.Menu(menu0, tearoff=False)
menu2.add_command(
    label="Help entry", command=lambda: print("你按了", help_check_string.get())
)

help_check_string = tk.StringVar()
menu2.add_checkbutton(
    label="check", onvalue="on", offvalue="off", variable=help_check_string
)

menu0.add_cascade(label="Help", menu=menu2)

# 第3排功能選單
# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm
menu3 = tk.Menu(menu0, tearoff=False)
menu3.add_command(label="exercise test 1", command=lambda: print("你按了 exercise test 1"))
menu0.add_cascade(label="Exercise", menu=menu3)

menu3b = tk.Menu(menu0, tearoff=False)
menu3b.add_command(
    label="some more stuff", command=lambda: print("你按了 some more stuff")
)
menu3.add_cascade(label="more stuff", menu=menu3b)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu = tk.Menu(window)
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="計算", menu=menu1)
menu1.add_command(label="加", command=lambda: print("你按了 加"))
menu1.add_command(label="減", command=lambda: print("你按了 減"))
menu1.add_separator()  # 增加分隔線
menu1.add_command(label="乘", command=lambda: print("你按了 乘"))
menu1.add_command(label="除", command=lambda: print("你按了 除"))

# 第2排功能選單
menu2 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Exit", menu=menu2)
menu2.add_command(label="離開", command=window.destroy)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=0)
menu1.add_command(label="supermode", command=lambda: print("你按了 supermode"))
menu0.add_cascade(label="Operation", menu=menu1)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="檔案(F)", menu=menu1)

menu1.add_command(label="開啟新檔", accelerator="Ctrl+N", command=lambda: print("你按了 開啟新檔"))
menu1.add_command(label="開啟", accelerator="Ctrl+O", command=lambda: print("你按了 開啟舊檔"))
menu1.add_separator()  # 增加分隔線
menu1.add_command(label="儲存", accelerator="Ctrl+S", command=lambda: print("你按了 另存新檔"))
menu1.add_separator()  # 增加分隔線
menu1.add_command(label="離開", accelerator="Ctrl+Q", command=lambda: window.destroy())

# 第2排功能選單
menu2 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="字體大小", menu=menu2)

labels = ("大", "中", "小")
for item in labels:
    menu2.add_radiobutton(label=item)

# 第3排功能選單 Help
menu3 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="說明(H)", menu=menu3)
menu3.add_command(label="關於(A)", command=lambda: print("你按了 關於"))

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter.messagebox as tkmessagebox
import tkinter.filedialog as tkfiledialog


def Cal():
    options = {}
    options["filetypes"] = [("allfiles", "*"), ("text", "*.txt")]
    options["initialdir"] = "c:\\"
    options["multiple"] = False
    options["title"] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)
    if fs:
        f = open(fs.name, "r")
        fc = f.readlines()
        f.close()
        fo = open("output.txt", "w")
        fo.write("試題分析結果\n")
        pitem = int(fc[0][0:3])
        fo.write("題數:" + str(pitem) + "\n")
        pmiss = fc[0][4:5]
        fo.write("缺失:" + pmiss + "\n")
        pomit = fc[0][6:7]
        fo.write("遺漏:" + pomit + "\n")
        pid = int(fc[0][8:10])
        fo.write("ID長度:" + str(pid) + "\n")
        pans = fc[1]
        fo.write("答案:" + pans)
        pnum = len(fc) - 2
        fo.write("人數:" + str(pnum) + "\n")
        psitem = []
        for j in range(0, pitem, 1):
            psitem.append(0)
        for i in range(0, pnum, 1):
            for j in range(0, pitem, 1):
                if fc[2 + i][pid + j] == pans[j]:
                    psitem[j] = psitem[j] + 1
        for j in range(0, pitem):
            fo.write(
                "第"
                + str(j + 1).rjust(2, "0")
                + "題，難度值p="
                + str(round(psitem[j] / pnum, 2)).ljust(4, "0")
                + "\n"
            )
        fo.close()
        tkmessagebox.showinfo(title="試題分析", message="分析完成")
    else:
        print("沒有選擇檔案")


def View():
    options = {}
    options["filetypes"] = [("allfiles", "*")]
    options["initialdir"] = "c:\\"
    options["multiple"] = False
    options["title"] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)
    if fs:
        f = open(fs.name, "r")
        fc = f.readlines()
        f.close()
        ptext = tk.Text(window, width=800, height=600)
        for i in range(0, len(fc), 1):
            ptext.insert(tk.INSERT, fc[i])
        ptext.pack()
        ptext.config(state=tk.DISABLED)
    else:
        print("沒有選擇檔案")


window = tk.Tk()
window.geometry("400x300")

# 建立功能選單 menu0
menu0 = tk.Menu(window, tearoff=0)

# 第1排功能選單 File
menu1 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="計算", menu=menu1)
menu1.add_command(label="計算", command=Cal)
menu1.add_command(label="檢視", command=View)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('窗口菜單')
window.geometry('200x200') 

l = tk.Label(window, text='', bg='blue')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1
 
#創建一個菜單欄，這里我們可以把他理解成一個容器，在窗口的上方
menubar = tk.Menu(window)
#定義一個空菜單單元
filemenu = tk.Menu(menubar, tearoff=0)
#將上面定義的空菜單命名為`File`，放在菜單欄中，就是裝入那個容器中
menubar.add_cascade(label='文件', menu=filemenu)
#在`File`中加入`New`的小菜單，即我們平時看到的下拉菜單，每一個小菜單對應命令操作。
#如果點擊這些單元, 就會觸發`do_job`的功能
filemenu.add_command(label='新建', command=do_job)
filemenu.add_command(label='打開', command=do_job)#同樣的在`文件`中加入`打開`小菜單
filemenu.add_command(label='保存', command=do_job)#同樣的在`文件`中加入`保存`小菜單
filemenu.add_separator()#這里就是一條分割線
#同樣的在`文件`中加入`編輯`小菜單,此處對應命令為`window.quit`
filemenu.add_command(label='編輯', command=window.quit)
 
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='編輯', menu=editmenu)
editmenu.add_command(label='剪切', command=do_job)
editmenu.add_command(label='復制', command=do_job)
editmenu.add_command(label='粘貼', command=do_job)
#和上面定義菜單一樣，不過此處實在`文件`上創建一個空的菜單
submenu = tk.Menu(filemenu)
#給放入的菜單`子菜單`命名為`導入`
filemenu.add_cascade(label='導入', menu=submenu, underline=0)
#這里和上面也一樣，在`導入`中加入一個小菜單命令`子菜單1`
submenu.add_command(label="子菜單1", command=do_job)
window.config(menu=menubar) 
window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, text='', bg='yellow')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)

window.mainloop()

print("------------------------------------------------------------")  # 60個
