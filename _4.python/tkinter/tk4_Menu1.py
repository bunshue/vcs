"""
# 以Menu元件建置功能表

"""

import sys
import tkinter as tk
from tkinter import ttk

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
menu1 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="檔案(F)", menu=menu1)
menu1.add_command(label="新增檔案", command=lambda: print("你按了 新增檔案"), accelerator="Ctrl+N")
menu1.add_command(label="開啟舊檔", command=lambda: print("你按了 開啟舊檔"), accelerator="Ctrl+O")
menu1.add_command(label="儲存檔案", command=lambda: print("你按了 儲存檔案"), accelerator="Ctrl+S")
menu1.add_command(label="另存新檔", command=lambda: print("你按了 另存新檔"))
menu1.add_separator()  # 增加分隔線
menu1.add_command(label="離開", command=window.destroy, accelerator="Ctrl+Q")

# 第2排功能選單 Edit
menu2 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="編輯(E)", menu=menu2)
menu2.add_command(label="復原", command=lambda: print("你按了 復原"))
menu1.add_separator()  # 增加分隔線
menu2.add_command(label="剪下", command=lambda: print("你按了 剪下"))
menu2.add_command(label="複製", command=lambda: print("你按了 複製"))
menu2.add_command(label="貼上", command=lambda: print("你按了 貼上"))

# 第3排功能選單 Search
menu3 = tk.Menu(menu0, tearoff=False)  # 取消分隔線
menu0.add_cascade(label="尋找(S)", menu=menu3)
menu3.add_command(label="尋找下一筆", command=lambda: print("你按了 尋找下一筆"))
menu3.add_command(label="尋找上一筆", command=lambda: print("你按了 尋找上一筆"))

# 第4排功能選單
menu4 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="字體大小", menu=menu4)

labels = ("大", "中", "小")
for item in labels:
    menu4.add_radiobutton(label=item)

# 第5排功能選單 Help
menu5 = tk.Menu(menu0, tearoff=0)
menu0.add_cascade(label="說明(H)", menu=menu5)
menu5.add_command(label="關於(A)", command=lambda: print("你按了 關於"))
demoStatus = tk.BooleanVar()
demoStatus.set(True)
menu5.add_checkbutton(label="Status", command=status, variable=demoStatus)

help_check_string = tk.StringVar()
menu5.add_checkbutton(label="check", onvalue="on", offvalue="off", variable=help_check_string)

#menu5.add_command(label="Status", command=lambda: print("你按了 status"))
#menu5.add_command(label="Info", command=lambda: print("你按了 Info"))
menu5.add_command(label="Info", command=lambda: print("你按了", help_check_string.get()))

# 第6排功能選單 多層
menu6 = tk.Menu(menu0, tearoff=False)
menu0.add_cascade(label="測試多層", menu=menu6)
menu6b = tk.Menu(menu0, tearoff=False)
menu6b.add_command(label="再多一層a", command=lambda: print("你按了 再多一層a"))
menu6b.add_command(label="再多一層b", command=lambda: print("你按了 再多一層b"))
menu6b.add_command(label="再多一層c", command=lambda: print("你按了 再多一層c"))
menu6.add_cascade(label="還有下一層", menu=menu6b)



"""
# 建立Text
text1 = tk.Text(window, undo=True)
text1.pack(fill=tk.BOTH, expand=True)

text1.insert(tk.END, "黃鶴樓送孟浩然之廣陵\n李白\n")
text1.insert(tk.END, "故人西辭黃鶴樓，\n")
text1.insert(tk.END, "煙花三月下揚州。\n")
text1.insert(tk.END, "孤帆遠影碧空盡，\n")
text1.insert(tk.END, "唯見長江天際流。\n")
"""

statusVar = tk.StringVar()
statusVar.set("顯示")
statusLabel = tk.Label(window, textvariable=statusVar, relief="raised")
statusLabel.pack(side=tk.BOTTOM, fill=tk.X)

window.config(menu=menu0)  # 顯示功能表單, 將功能表物件 menu0 佈置到主視窗的頂部
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

l = tk.Label(window, text='', bg='pink', width = 50, height = 10)
l.pack()

#創建一個菜單欄，這里我們可以把他理解成一個容器，在窗口的上方
menubar = tk.Menu(window)
#定義一個空菜單單元
filemenu = tk.Menu(menubar, tearoff=0)
#將上面定義的空菜單命名為`File`，放在菜單欄中，就是裝入那個容器中
menubar.add_cascade(label='文件', menu=filemenu)

#和上面定義菜單一樣，不過此處實在`文件`上創建一個空的菜單
submenu = tk.Menu(filemenu)
#給放入的菜單`子菜單`命名為`導入`
filemenu.add_cascade(label='導入', menu=submenu, underline=0)
#這里和上面也一樣，在`導入`中加入一個小菜單命令`子菜單1`
submenu.add_command(label="子菜單1", command=lambda: print("你按了 子菜單1"))
window.config(menu=menubar) 

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x300")

l = tk.Label(window, text='', bg='pink', width = 50, height = 10)
l.pack()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='導入', menu=submenu, underline=0)
submenu.add_command(label="子菜單1", command=lambda: print("你按了 子菜單1"))

window.config(menu=menubar)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




"""
menubar = tk.Menu(window)  # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File
filemenu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Exit", command=window.destroy)
window.config(menu=menubar)  # 顯示功能表物件

"""




"""

messagebox.showinfo("New File", "開新檔案")


"""


# 快捷鍵綁定
window.bind(
    "<Control-n>", lambda event: print("你按了 開新檔案")
)

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
exitBtn = tk.Button(toolbar, image=tk_image, command=lambda: print("你按了 太陽"))
exitBtn.pack(side=tk.LEFT, padx=3, pady=3)  # 包裝按鈕

toolbar.pack(side=tk.TOP, fill=tk.X)  # 包裝工具列

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



