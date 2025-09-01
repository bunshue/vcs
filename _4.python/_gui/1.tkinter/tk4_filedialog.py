"""



"""

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import tkinter as tk

import tkinter.filedialog

"""
from tkinter.filedialog import askopenfile #tk之openFileDialog
from tkinter.filedialog import asksaveasfile #tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
"""


def button00Click():
    print("你按了button00 選取檔案1")
    file = tkinter.filedialog.askopenfile(
        parent=window, mode="rb", title="選取檔案", filetypes=[("檔案", "*.*")]
    )
    if file:
        filename = file.name
        message = "檔案 :" + filename
        print(message)
        text1.insert("end", message)


def button01Click():
    print("你按了button01 選取檔案2 pdf")
    pdf_filename = tkinter.filedialog.askopenfilename(
        title="開啟PDF檔案",
        initialdir="C:/dddddddddd/____download",
        filetypes=[("PDF files", "*.pdf")],
    )
    print(pdf_filename)

    text1.delete("1.0", tk.END)

    current_text = pdf_filename
    text1.insert(tk.END, current_text)


def button02Click():
    print("你按了button02 另存新檔1")
    file = tkinter.filedialog.asksaveasfilename(defaultextension=".jpg")
    if file:
        filename = file
        message = "另存新檔, 檔案 :" + filename
        print(message)
        text1.insert("end", message)


def button03Click():
    print("你按了button03")
    ret = tk.messagebox.askyesno("python", "是否離開程式?")
    if ret == True:
        window.destroy()  # 結束程式
    else:
        return


def button04Click():
    print("你按了button04")


def button05Click():
    print("你按了button05")


def button10Click():
    print("你按了button10")


def button11Click():
    print("你按了button11")


def button12Click():
    print("你按了button12")


def button13Click():
    print("你按了button13")


def button14Click():
    print("你按了button14")


def button15Click():
    print("你按了button15")


def button20Click():
    print("你按了button20")


def button21Click():
    print("你按了button21")


def button22Click():
    print("你按了button22")


def button23Click():
    print("你按了button23")


def button24Click():
    print("你按了button24")
    # 清空Text
    text1.delete(1.0, "end")


def button25Click():
    # print('你按了button25')
    message = "匯入生產資料 完成\n"
    # print(message)
    text1.insert("end", message)


window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
# size = str(W)+'x'+str(H)
# size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
window.title("功能測試")

# 設定主視窗之背景色
# window.configure(bg = "#7AFEC6")

x_st = 50
y_st = 250
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, width=w, height=h, command=button00Click, text="選取檔案1")
button00.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button01 = tk.Button(window, width=w, height=h, command=button01Click, text="選取檔案2 pdf")
button01.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button02 = tk.Button(window, width=w, height=h, command=button02Click, text="另存新檔1")
button02.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button03 = tk.Button(window, width=w, height=h, command=button03Click, text="詢問是否離開程式")
button03.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button04 = tk.Button(window, width=w, height=h, command=button04Click, text="----")
button04.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button05 = tk.Button(window, width=w, height=h, command=button05Click, text="----")
button05.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button00.place(x=x_st + dx * 0, y=y_st + dy * 0)
button01.place(x=x_st + dx * 1, y=y_st + dy * 0)
button02.place(x=x_st + dx * 2, y=y_st + dy * 0)
button03.place(x=x_st + dx * 3, y=y_st + dy * 0)
button04.place(x=x_st + dx * 4, y=y_st + dy * 0)
button05.place(x=x_st + dx * 5, y=y_st + dy * 0)

button10 = tk.Button(window, width=w, height=h, command=button10Click, text="----")
button10.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button11 = tk.Button(window, width=w, height=h, command=button11Click, text="----")
button11.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button12 = tk.Button(window, width=w, height=h, command=button12Click, text="----")
button12.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button13 = tk.Button(window, width=w, height=h, command=button13Click, text="----")
button13.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button14 = tk.Button(window, width=w, height=h, command=button14Click, text="----")
button14.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button15 = tk.Button(window, width=w, height=h, command=button15Click, text="----")
button15.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button10.place(x=x_st + dx * 0, y=y_st + dy * 1)
button11.place(x=x_st + dx * 1, y=y_st + dy * 1)
button12.place(x=x_st + dx * 2, y=y_st + dy * 1)
button13.place(x=x_st + dx * 3, y=y_st + dy * 1)
button14.place(x=x_st + dx * 4, y=y_st + dy * 1)
button15.place(x=x_st + dx * 5, y=y_st + dy * 1)

button20 = tk.Button(window, width=w, height=h, command=button20Click, text="----")
button20.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button21 = tk.Button(window, width=w, height=h, command=button21Click, text="----")
button21.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button22 = tk.Button(window, width=w, height=h, command=button22Click, text="----")
button22.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button23 = tk.Button(window, width=w, height=h, command=button23Click, text="----")
button23.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button24 = tk.Button(window, width=w, height=h, command=button24Click, text="----")
button24.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button25 = tk.Button(window, width=w, height=h, command=button25Click, text="----")
button25.pack(side=tk.LEFT, ipadx=25, ipady=25, expand=tk.YES)
button20.place(x=x_st + dx * 0, y=y_st + dy * 2)
button21.place(x=x_st + dx * 1, y=y_st + dy * 2)
button22.place(x=x_st + dx * 2, y=y_st + dy * 2)
button23.place(x=x_st + dx * 3, y=y_st + dy * 2)
button24.place(x=x_st + dx * 4, y=y_st + dy * 2)
button25.place(x=x_st + dx * 5, y=y_st + dy * 2)

# 加入 Text
text1 = tk.Text(window, width=100, height=20)  # 放入多行輸入框
text1.pack()
text1.place(x=x_st + dx * 0, y=y_st + dy * 3 + 10)


def open_file():
    button_ofd_text.set("開啟檔案...")
    file = tkinter.filedialog.askopenfile(
        parent=window, mode="rb", title="選取檔案", filetypes=[("Text file", "*.txt")]
    )
    if file:
        print("已選取檔案 : ", file.name)

    button_ofd_text.set("開啟檔案")


def save_file():
    button_sfd_text.set("另存新檔...")
    file = tkinter.filedialog.asksaveasfile(
        parent=window, mode="w", title="選取檔案", filetypes=[("Text file", "*.txt")]
    )
    if file:
        print("另存新檔 : ", file.name)

    button_sfd_text.set("另存新檔")


# 開啟檔案按鈕
button_ofd_text = tk.StringVar()
button_ofd = tk.Button(
    window,
    textvariable=button_ofd_text,
    command=lambda: open_file(),
    font="Raleway",
    bg="#20bebe",
    fg="white",
    height=2,
    width=15,
)
# button_ofd = tk.Button(window, text = '選取檔案', command = xxxxxxx)
button_ofd_text.set("開啟檔案")
button_ofd.pack()

# 另存新檔按鈕
button_sfd_text = tk.StringVar()
button_sfd = tk.Button(
    window,
    textvariable=button_sfd_text,
    command=lambda: save_file(),
    font="Raleway",
    bg="#20bebe",
    fg="white",
    height=2,
    width=15,
)
# button_sfd = tk.Button(window, text = '選取檔案', command = xxxxxxx)
button_sfd_text.set("另存新檔")
button_sfd.pack()

print("------------------------------------------------------------")  # 60個
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


# DIALOG_ICON = 'warning'
DIALOG_ICON = "questhead"


class Dialog(tk.Widget):
    def __init__(self, master=None, cnf={}, **kw):
        cnf = tk._cnfmerge((cnf, kw))
        self.widgetName = "__dialog__"
        tk.Widget._setup(self, master, cnf)
        self.num = self.tk.getint(
            self.tk.call(
                "tk_dialog",
                self._w,
                cnf["title"],
                cnf["text"],
                cnf["bitmap"],
                cnf["default"],
                *cnf["strings"]
            )
        )
        try:
            tk.Widget.destroy(self)
        except TclError:
            pass

    def destroy(self):
        pass


def open_dialog():
    d = Dialog(
        None,
        {
            "title": "File Modified",
            "text": 'File "Python.h" has been modified'
            " since the last time it was saved."
            " Do you want to save it before"
            " exiting the application.",
            "bitmap": DIALOG_ICON,
            "default": 0,
            "strings": ("Save File", "Discard Changes", "Return to Editor"),
        },
    )
    print("你選擇了", d.num)


print(tk.TkVersion)

button1 = tk.Button(window, {"text": "Test", "command": open_dialog, tk.Pack: {}})
button2 = tk.Button(window, {"text": "Quit", "command": window.destroy, tk.Pack: {}})

print("------------------------------------------------------------")  # 60個
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


def FileOpen():  # 按鈕事件處理函數
    r = tk.filedialog.askopenfilename(
        title="Python Tkinter",  # 建立開啟檔案交談視窗
        filetypes=[("Python", "*.py *.pyw"), ("All files", "*")],
    )  # 指定檔案型態為Python指令稿
    print(r)  # 輸出傳回值


def FileSave():  # 按鈕事件處理函數
    r = tk.filedialog.asksaveasfilename(
        title="Python Tkinter",  # 建立儲存檔案交談視窗
        initialdir=r"E:\Python\code",  # 指定起始化目錄
        initialfile="test.py",
    )  # 指定起始化檔案
    print(r)


button1 = tk.Button(window, text="File Open", command=FileOpen)  # 建立按鈕  # 指定按鈕事件處理函數
button1.pack()
button2 = tk.Button(window, text="File Save", command=FileSave)  # 指定按鈕事件處理函數
button2.pack()


print("------------------------------------------------------------")  # 60個
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

""" 詢問是否離開程式
def callback():
    res = tk.messagebox.askokcancel("OKCANCEL","結束或取消?")
    if res == True:
        window.destroy()
    else:
        return
window.protocol("WM_DELETE_WINDOW",callback)  # 更改協定綁定
"""

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
from tkinter.filedialog import asksaveasfilename


def newFile():  # 開新檔案
    text.delete("1.0", END)  # 刪除Text控件內容
    window.title("Untitled")  # 視窗標題改為Untitled


def saveAsFile():  # 另存新檔
    global filename
    textContent = text.get("1.0", END)
    # 開啟另存新檔對話方塊, 所輸入的檔案路徑會回傳給filename
    # filename = asksaveasfilename()
    # 開啟另存新檔對話方塊, 預設所存的檔案副檔名是txt
    filename = asksaveasfilename(defaultextension=".txt")
    if filename == "":  # 如果沒有輸入檔案名稱
        return  # 不往下執行
    with open(filename, "w") as output:
        output.write(textContent)
        window.title(filename)  # 更改window視窗標題


filename = "Untitled"
window = Tk()
window.title(filename)
window.geometry("300x180")

menubar = Menu(window)  # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save As", command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy)
window.config(menu=menubar)  # 顯示功能表物件

# 建立Text
text = Text(window, undo=True)
text.pack(fill=BOTH, expand=True)
text.insert(END, "Five Hundred Miles\n")
text.insert(END, "If you miss the rain I am on,\n")
text.insert(END, "You will knw that I am gone.\n")
text.insert(END, "You can hear the whistle blw\n")
text.insert(END, "A hunded miles,\n")

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename


def newFile():  # 開新檔案
    text.delete("1.0", END)  # 刪除Text控件內容
    window.title("Untitled")  # 視窗標題改為Untitled


def openFile():  # 開啟舊檔
    global filename
    filename = askopenfilename()  # 讀取開啟的檔案
    if filename == "":  # 如果沒有選擇檔案
        return  # 返回
    with open(filename, "r") as fileObj:  # 開啟檔案
        content = fileObj.read()  # 讀取檔案內容
    text.delete("1.0", END)  # 刪除Text控件內容
    text.insert(END, content)  # 插入所讀取的檔案
    window.title(filename)  # 更改視窗標題


def saveAsFile():  # 另存新檔
    global filename
    textContent = text.get("1.0", END)
    # 開啟另存新檔對話方塊, 所輸入的檔案路徑會回傳給filename
    # filename = asksaveasfilename()
    # 開啟另存新檔對話方塊, 預設所存的檔案副檔名是txt
    filename = asksaveasfilename(defaultextension=".txt")
    if filename == "":  # 如果沒有輸入檔案名稱
        return  # 不往下執行
    with open(filename, "w") as output:
        output.write(textContent)
        window.title(filename)  # 更改window視窗標題


filename = "Untitled"
window = Tk()
window.title(filename)
window.geometry("300x180")

menubar = Menu(window)  # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open File ...", command=openFile)
filemenu.add_command(label="Save As ...", command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy)
window.config(menu=menubar)  # 顯示功能表物件

# 建立Text
text = Text(window, undo=True)
text.pack(fill=BOTH, expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText


def newFile():  # 開新檔案
    text.delete("1.0", END)  # 刪除Text控件內容
    window.title("Untitled")  # 視窗標題改為Untitled


def openFile():  # 開啟舊檔
    global filename
    filename = askopenfilename()  # 讀取開啟的檔案
    if filename == "":  # 如果沒有選擇檔案
        return  # 返回
    with open(filename, "r") as fileObj:  # 開啟檔案
        content = fileObj.read()  # 讀取檔案內容
    text.delete("1.0", END)  # 刪除Text控件內容
    text.insert(END, content)  # 插入所讀取的檔案
    window.title(filename)  # 更改視窗標題


def saveAsFile():  # 另存新檔
    global filename
    textContent = text.get("1.0", END)
    # 開啟另存新檔對話方塊, 預設所存的檔案副檔名是txt
    filename = asksaveasfilename(defaultextension=".txt")
    if filename == "":  # 如果沒有輸入檔案名稱
        return  # 不往下執行
    with open(filename, "w") as output:
        output.write(textContent)
        window.title(filename)  # 更改window視窗標題


filename = "Untitled"
window = Tk()
window.title(filename)
window.geometry("300x180")

menubar = Menu(window)  # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File
filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open File ...", command=openFile)
filemenu.add_command(label="Save As ...", command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.destroy)
window.config(menu=menubar)  # 顯示功能表物件

# 建立Text
text = ScrolledText(window, undo=True)
text.pack(fill=BOTH, expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


""" 新進待整理



print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter.filedialog import asksaveasfilename    # 導入文件保存對話框函數
 
def generate_report():
    # 生成報告的函數, 從文本框中獲取報告內容
    report_content = text_report.get("1.0", tk.END)
    # 打開一個對話框讓使用者選擇保存報告的路徑
    file_path = asksaveasfilename(
        defaultextension=".txt",                    # 預設副檔名為.txt
        filetypes=[("Text documents", ".txt")],     # 文件類型過濾
    )
    # 如果使用者選擇了文件路徑, 則將報告內容寫入文件
    if file_path:
        with open(file_path, "w") as file:
            file.write(report_content)

root = tk.Tk()
root.title("報告生成器")                             # 視窗標題
text_report = tk.Text(root)                 # 建立文字區域用於編輯報告內容
text_report.pack()                          # 將文本區域添加到視窗中
# 建一個按鈕，點擊時會呼叫generate_report()函數
button_generate = tk.Button(root, text="生成報告", command=generate_report)
button_generate.pack()                      # 將按鈕添加到視窗中
root.mainloop()

print("------------------------------------------------------------")  # 60個


import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


save_dir = open_file_dialog()
print(save_dir)


print('測試另存新檔對話框')
import tkinter.filedialog

filename = tkinter.filedialog.asksaveasfilename(title="儲存檔案", initialfile="qrcode.png")
print("取得 :", filename)

def open_file():
    filename = filedialog.askopenfilename()
    print('open file => ' + filename)

def save_as():
    filename = filedialog.asksaveasfilename()
    print('save file as => ' + filename)


def open():
    filename = tkinter.filedialog.askopenfilename()
    print('open file => ' + filename)

def open():
	filename = tkinter.filedialog.askopenfilename()
	print('open file => ' + filename)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder





"""
