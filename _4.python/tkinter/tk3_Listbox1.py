import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 1")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

listbox = tk.Listbox(window)
listbox.pack()

# Listbox內加入項目
listbox.insert(tk.END, "鼠")
for item in ["牛", "虎", "兔"]:
    listbox.insert(tk.END, item)


lb = tk.Listbox(window)
lb.insert(tk.END, "鼠")
lb.insert(tk.END, "牛")
lb.insert(tk.END, "虎")
lb.pack(pady=10)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

lb1 = tk.Listbox(window)  # 建立listbox 1
lb1.pack()

lb2 = tk.Listbox(window, height=5, relief="raised")  # 建立listbox 2
lb2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 2")

animals = ["鼠", "牛", "虎", "兔"]

# 多這個
lb = tk.Listbox(window, selectmode=tk.MULTIPLE)  # 建立可以多選項的listbox

for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

# 多這個
lb = tk.Listbox(window, selectmode=tk.EXTENDED)  # 拖曳可以選擇多選項

for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window, selectmode=tk.EXTENDED)  # 拖曳可以選擇多選項
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.insert(tk.ACTIVE, "Orange", "Grapes", "Mango")  # 前面補充建立3個項目
lb.pack(pady=10)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window, selectmode=tk.EXTENDED)  # 拖曳可以選擇多選項
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)
print("你選了 ", lb.size(), "個")  # 列出選項數量

window.mainloop()

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 3")

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)
lb.selection_set(0)  # 預設選擇第0個項目

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window, selectmode=tk.EXTENDED)  # 拖曳可以選擇多選項
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)
lb.selection_set(0, 3)  # 預設選擇第0-3索引項目

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)
lb.delete(1)  # 刪除索引1的項目

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)
lb.delete(1, 3)  # 刪除索引1-3的項目

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 4")

animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)
print(lb.get(1))  # 列印索引1的項目

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=10)
print(lb.get(1, 3))  # 列印索引1-3的項目

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def callback():  # 列印所選的項目
    indexs = lb.curselection()
    for index in indexs:  # 取得索引值
        print(lb.get(index))  # 列印所選的項目


animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window, selectmode=tk.MULTIPLE)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=5)

button1 = tk.Button(window, text="Print", command=callback)
button1.pack(pady=5)

print("------------------------------------------------------------")  # 60個


def callback():  # 列印檢查結果
    print(lb.selection_includes(3))


animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window, selectmode=tk.MULTIPLE)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(pady=5)

button1 = tk.Button(window, text="Check", command=callback)
button1.pack(pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個


def itemsSorted():  # 排序
    if var.get() == True:  # 如果設定
        revBool = True  # 大到小排序是True
    else:
        revBool = False  # 大到小排序是False
    listTmp = list(lb.get(0, tk.END))  # 取得項目內容
    sortedList = sorted(listTmp, reverse=revBool)  # 執行排序
    lb.delete(0, tk.END)  # 刪除原先Listbox內容
    for item in sortedList:  # 將排序結果插入Listbox
        lb.insert(tk.END, item)


animals = ["鼠", "牛", "虎", "兔"]

window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 5")

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.pack(padx=10, pady=5)

# 建立排序按鈕
button1 = tk.Button(window, text="排序", command=itemsSorted)
button1.pack()

# 建立排序設定核取方塊
var = tk.BooleanVar()
cb = tk.Checkbutton(window, text="大到小排序", variable=var)
cb.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def itemSelected(event):  # 列出所選單一項目
    obj = event.widget  # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))  # 設定標籤內容


animals = ["鼠", "牛", "虎", "兔"]

var = tk.StringVar()  # 建立標籤
lab = tk.Label(window, text="", textvariable=var)
lab.pack(pady=5)

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.bind("<<ListboxSelect>>", itemSelected)  # 點選綁定
lb.pack(pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def itemSelected(event):  # 列出所選單一項目
    index = lb.curselection()  # 取得索引
    var.set(lb.get(index))  # 設定標籤內容


animals = ["鼠", "牛", "虎", "兔"]

var = tk.StringVar()  # 建立標籤
lab = tk.Label(window, text="", textvariable=var)
lab.pack(pady=5)

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.bind("<<ListboxSelect>>", itemSelected)  # 點選綁定
lb.pack(pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()


def itemSelected(event):  # 列出所選單一項目
    obj = event.widget  # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))  # 設定標籤內容


window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 6")

animals = ["鼠", "牛", "虎", "兔"]

var = tk.StringVar()
lab = tk.Label(window, text="", textvariable=var)
lab.pack(pady=5)

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.bind("<Double-Button-1>", itemSelected)  # 連按2下綁定
lb.pack(pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def itemsSelected(event):  # 列印所選結果
    obj = event.widget  # 取得事件的物件
    indexs = obj.curselection()  # 取得索引
    for index in indexs:  # 將元組內容列出
        print(obj.get(index))
    print("----------")  # 區隔輸出


animals = ["鼠", "牛", "虎", "兔"]

var = tk.StringVar()
lab = tk.Label(window, text="", textvariable=var)
lab.pack(pady=5)

lb = tk.Listbox(window, selectmode=tk.EXTENDED)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
lb.bind("<<ListboxSelect>>", itemsSelected)  # 點選綁定
lb.pack(pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def getIndex(event):  # 處理按一下選項
    lb.index = lb.nearest(event.y)  # 目前選項的索引


def dragJob(event):  # 處理拖曳選項
    newIndex = lb.nearest(event.y)  # 目前選項的新索引
    if newIndex < lb.index:  # 往上拖曳
        x = lb.get(newIndex)  # 獲得新位置內容
        lb.delete(newIndex)  # 刪除新位置的內容
        lb.insert(newIndex + 1, x)  # 放回原先新位置的內容
        lb.index = newIndex  # 選項的新索引
    elif newIndex > lb.index:  # 往下拖曳
        x = lb.get(newIndex)  # 獲得新位置內容
        lb.delete(newIndex)  # 刪除新位置的內容
        lb.insert(newIndex - 1, x)  # 放回原先新位置的內容
        lb.index = newIndex  # 選項的新索引


animals = ["鼠", "牛", "虎", "兔"]

lb = tk.Listbox(window)
for animal in animals:  # 建立動物項目
    lb.insert(tk.END, animal)
    lb.bind("<Button-1>", getIndex)  # 按一下綁定getIndex
    lb.bind("<B1-Motion>", dragJob)  # 拖曳綁定dragJob
lb.pack(padx=10, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("Listbox + Scrollbar")

window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 7")

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

wordlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listbox1 = tk.Listbox(window, yscrollcommand=scrollbar.set)
listbox1 = tk.Listbox(window, yscrollcommand=scrollbar.set)

# Listbox內加入項目
for line in range(26):
    listbox1.insert(tk.END, "字母: " + wordlist[line])

"""
for i in range(100):
    listbox1.insert(tk.END, str(i))
"""
listbox1.pack(side=tk.LEFT, fill=tk.BOTH)
listbox1.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox1.yview)
scrollbar.config(command=listbox1.yview)


window.mainloop()


""" grid

def itemAdded():                        # 增加項目處理程式
    varAdd = entry.get()                # 讀取Entry的項目
    if (len(varAdd.strip()) == 0):      # 沒有增加不處理
        return
    lb.insert(tk.END,varAdd)               # 將項目增加到Listbox
    entry.delete(0,tk.END)                 # 刪除Entry的內容

def itemDeleted():                      # 刪除項目處理程式
    index = lb.curselection()           # 取得所選項目索引
    if (len(index) == 0):               # 如果長度是0表示沒有選取
        return
    lb.delete(index)                    # 刪除選項    

entry = tk.Entry(window)
entry.grid(row=0,column=0,padx=5,pady=5)

# 建立增加按鈕
buttonAdd = tk.Button(window,text="增加",width=10,command=itemAdded)
buttonAdd.grid(row=0,column=1,padx=5,pady=5)

# 建立Listbox
lb = tk.Listbox(window)
lb.grid(row=1,column=0,columnspan=2,padx=5,sticky=tk.W)

# 建立刪除按鈕
buttonDel = tk.Button(window,text="刪除",width=10,command=itemDeleted)
buttonDel.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)


"""
