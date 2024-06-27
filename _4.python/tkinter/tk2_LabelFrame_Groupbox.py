"""
LabelFrame 就是 Groupbox

"""

import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("LabelFrame 1")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# GroupBox測試
tk.Label(text="LabelFrame 測試").pack()

# GroupBox之大小, 若小於內附控件大小, 則會撐大
w = 10
h = 10
labelframe1 = tk.LabelFrame(window, text="LabelFrame", padx=w, pady=h)

# GroupBox之位置, 相較於目前表單位置
x_st = 0
y_st = 0
labelframe1.pack(padx=x_st, pady=y_st)

# GroupBox內 放幾個控件
w = tk.Entry(labelframe1).pack()
w = tk.Entry(labelframe1).pack()
w = tk.Entry(labelframe1).pack()
w = tk.Entry(labelframe1).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def printInfo2():
    selection = ""
    for i in checkboxes:  # 檢查此字典
        if checkboxes[i].get() == True:  # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)


# 以下建立標籤框架與和曲方塊
labelframe2 = tk.LabelFrame(window, text="選擇最喜歡的運動")
labelframe2.pack(ipadx=5, ipady=5, pady=10)  # 包裝定位標籤框架

sports = {0: "美式足球", 1: "棒球", 2: "籃球", 3: "網球"}  # 運動字典
checkboxes = {}  # 字典存放被選取項目
for i in range(len(sports)):  # 將運動字典轉成核取方塊
    checkboxes[i] = tk.BooleanVar()  # 布林變數物件
    tk.Checkbutton(labelframe2, text=sports[i], variable=checkboxes[i]).grid(
        row=i + 1, sticky=tk.W
    )

button1 = tk.Button(window, text="確定", width=10, command=printInfo2)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

from tkinter import ttk

# 創建一個容器,
labelframe3 = tk.LabelFrame(window, text="使用LabelFrame")  # 創建一個容器，其父容器為window
labelframe3.pack()

# button被點擊之后會被執行
def clickMe():  # 當acction被點擊時,該函數則生效
    action.configure(
        text="Hello " + name.get() + " " + numberChosen.get()
    )  # 設置button顯示的內容
    print("check3 is %s %s" % (type(chvarEn.get()), chvarEn.get()))


# 創建一個按鈕, text：顯示按鈕上面顯示的文字, command：當這個按鈕被點擊之后會調用command函數
action = tk.Button(labelframe3, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)  # 設置其在界面中出現的位置,column代表列,row 代表行

# 文本框
name = tk.StringVar()  # StringVar是Tk庫內部定義的字符串變量類型
nameEntered = tk.Entry(labelframe3, width=12, textvariable=name)  # 創建一個文本框，定義長度為12個字符長度
nameEntered.grid(column=0, row=1, sticky=tk.W)  # 設置其在界面中出現的位置,column代表列,row代表行
nameEntered.focus()  # 當程序運行時,光標默認會出現在該文本框中

# 創建一個下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(labelframe3, width=12, textvariable=number, state="readonly")
numberChosen["values"] = (1, 2, 4, 42, 100)  # 設置下拉列表的值
numberChosen.grid(column=1, row=1)  # 設置其在界面中出現的位置,column代表列,row 代表行
numberChosen.current(0)  # 設置下拉列表默認顯示的值，0為 numberChosen['values'] 的下標值

# 復選框
chVarDis = tk.IntVar()  # 用來獲取復選框是否被勾選，其狀態值為int類型,勾選為1,未勾選為0

# text為該復選框后面顯示的名稱, variable將該復選框的狀態賦值給一個變量，當state='disabled'時，該復選框為灰色，不能點的狀態
check1 = tk.Checkbutton(labelframe3, text="Disabled", variable=chVarDis, state="disabled")
check1.select()  # 該復選框是否勾選,select為勾選, deselect為不勾選
check1.grid(
    column=0, row=4, sticky=tk.W
)  # sticky=tk.W(N：北/上對齊,S：南/下對齊,W：西/左對齊,E：東/右對齊)
chvarUn = tk.IntVar()
check2 = tk.Checkbutton(labelframe3, text="UnChecked", variable=chvarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chvarEn = tk.IntVar()
check3 = tk.Checkbutton(labelframe3, text="Enabled", variable=chvarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def fnRed():
    frame1.config(bg="red")


def fnGreen():
    frame1.config(bg="green")


def fnBlue():
    frame1.config(bg="blue")


print("顏色切換")

frame1 = tk.Frame(
    window, width=200, height=100, relief="raised", borderwidth=3, bg="white"
)
frame1.pack(pady=5)

# 建立1個 LabelFrame 在 window 下
labelframe4 = tk.LabelFrame(window, text="顏色切換")
labelframe4.pack(pady=20, fill="x")

# 建立3個 button 在 LabelFrame 下
button1 = tk.Button(labelframe4, text="紅色", width=8, command=fnRed).pack(
    side="left", padx=5
)
button2 = tk.Button(labelframe4, text="綠色", width=8, command=fnGreen).pack(
    side="left", padx=5
)
button3 = tk.Button(labelframe4, text="藍色", width=8, command=fnBlue).pack(
    side="left", padx=5
)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

labelframe5 = tk.LabelFrame(window, text="錄影設定：", relief="raised", borderwidth=2)
labelframe5.pack(pady=5)

tk.Label(labelframe5, text="編碼器：").grid(row=0, column=0, pady=3)

spinboxFourcc = tk.Spinbox(
    labelframe5, value=("XVID", "DIVX", "MJPG", "I420"), width=10
)
spinboxFourcc.grid(row=0, column=1, pady=3, sticky="w")

tk.Label(labelframe5, text="檔名：").grid(row=2, column=0, pady=3)

entry1 = tk.Entry(labelframe5, width=20)
entry1.grid(row=2, column=1, pady=3, sticky="w")

tk.Label(labelframe5, text="AAAAA").grid(row=3, column=0, columnspan=2)

button1 = tk.Button(labelframe5, text="BBBBB")
button1.grid(row=4, column=0, columnspan=1)

button2 = tk.Button(labelframe5, text="CCCCC")
button2.grid(row=4, column=1, columnspan=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("LabelFrame 2")

def fnCal():
    r = userR.get()
    u = unid.get()
    if kind.get() == "圓周長":  # 若選取圓周長
        a = 3.14 * 2 * r
        print("圓周長為 {:.2f} {}".format(a, u))
    else:
        a = 3.14 * r * r
        print("圓面積為 {:.2f} 平方{}".format(a, u))


print("圓形計算")

lfrmR = tk.LabelFrame(window, text="輸入半徑：")
lfrmR.pack(pady=10)
userR = tk.IntVar()
userR.set(10)
entR = tk.Entry(lfrmR, textvariable=userR).pack(pady=3)
labelMsg = tk.Label(lfrmR, text="請輸入半徑(整數)然後選擇項目").pack(pady=10)

lfrmKind = tk.LabelFrame(window, text="計算類別")
lfrmKind.pack(side="left", pady=10, padx=10, fill="x", expand=1)
kinds = ["圓周長", "圓面積"]
kind = tk.StringVar()
for k in kinds:
    tk.Radiobutton(lfrmKind, text=k, variable=kind, value=k, command=fnCal).pack(pady=3)
kind.set("圓周長")

lfrmUnid = tk.LabelFrame(window, text="單位")
lfrmUnid.pack(side="left", pady=10, padx=10, fill="x", expand=1)
unids = ["公分", "英吋"]
unid = tk.StringVar()
for u in unids:
    tk.Radiobutton(lfrmUnid, text=u, variable=unid, value=u, command=fnCal).pack(pady=3)
unid.set(unids[0])

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print('OK')
