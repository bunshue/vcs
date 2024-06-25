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
