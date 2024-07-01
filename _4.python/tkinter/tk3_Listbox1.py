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

listbox1 = tk.Listbox(window, width=30, height=5, selectmode=tk.EXTENDED)  # 拖曳可以選擇多選項

#多選
listbox1 = tk.Listbox(window, width=30, height=5, selectmode=tk.MULTIPLE)  # 建立可以多選項的listbox
#單選
listbox1 = tk.Listbox(window, width=30, height=5)
#listbox1 = tk.Listbox(window, width=30, height=5, relief="raised")
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")

listbox1.insert(tk.ACTIVE, "兔", "龍", "蛇")  # 前面補充建立3個項目

listbox1.selection_set(2)  # 預設選擇第2個項目
listbox1.selection_set(0, 3)  # 預設選擇第0-3索引項目
#listbox1.delete(1)  # 刪除索引1的項目
#listbox1.delete(1, 3)  # 刪除索引1-3的項目

print(listbox1.get(1))  # 列印索引1的項目
print(listbox1.get(1, 3))  # 列印索引1-3的項目

print("列出選項數量 :", listbox1.size(), "個")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def get_listbox_data1():  # 列印所選的項目
    indexs = listbox1.curselection()
    for index in indexs:  # 取得索引值
        print("你選取了 :", listbox1.get(index))  # 列印所選的項目


listbox1 = tk.Listbox(window, width=30, height=5, selectmode=tk.MULTIPLE)
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")

button1 = tk.Button(window, text="取得選取資料", command=get_listbox_data1)
button1.pack()

print("------------------------------------------------------------")  # 60個


def get_listbox_data2():  # 列印檢查結果
    print("選取是否包含第3項 :", listbox1.selection_includes(3))


listbox1 = tk.Listbox(window, width=30, height=5, selectmode=tk.MULTIPLE)
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")
listbox1.insert(tk.END, "兔")
listbox1.insert(tk.END, "龍")

button1 = tk.Button(window, text="選取是否包含第3項", command=get_listbox_data2)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個



separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def itemsSorted():  # 排序
    print('Checkbutton選取狀態 :', checkbutton_var.get())
    
    if checkbutton_var.get() == True:  # 如果設定
        revBool = True  # 大到小排序是True
    else:
        revBool = False  # 大到小排序是False
    listTmp = list(listbox1.get(0, tk.END))  # 取得項目內容
    sortedList = sorted(listTmp, reverse=revBool)  # 執行排序
    listbox1.delete(0, tk.END)  # 刪除原先Listbox內容
    for item in sortedList:  # 將排序結果插入Listbox
        listbox1.insert(tk.END, item)


listbox1 = tk.Listbox(window, width=30, height=5)
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")

# 建立排序按鈕
button1 = tk.Button(window, text="排序", command=itemsSorted)
button1.pack()

# 建立排序設定核取方塊
checkbutton_var = tk.BooleanVar()
cb = tk.Checkbutton(window, text="大到小排序", variable=checkbutton_var)
cb.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def get_listbox_data3(event):  # 列出所選單一項目
    obj = event.widget  # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))  # 設定標籤內容


var = tk.StringVar()  # 建立標籤
lab = tk.Label(window, width=30, height=5, text="", textvariable=var)
lab.pack()

listbox1 = tk.Listbox(window, width=30, height=5)
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")

listbox1.bind("<<ListboxSelect>>", get_listbox_data3)  # 點選綁定

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def get_listbox_data3(event):  # 列出所選單一項目
    index = listbox1.curselection()  # 取得索引
    var.set(listbox1.get(index))  # 設定標籤內容


var = tk.StringVar()  # 建立標籤
lab = tk.Label(window, width=30, height=5, text="", textvariable=var)
lab.pack()

listbox1 = tk.Listbox(window, width=30, height=5)
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")

listbox1.bind("<<ListboxSelect>>", get_listbox_data3)  # 點選綁定

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def get_listbox_data3(event):  # 列出所選單一項目
    obj = event.widget  # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))  # 設定標籤內容


var = tk.StringVar()  # 建立標籤
lab = tk.Label(window, width=30, height=5, text="", textvariable=var)
lab.pack()

listbox1 = tk.Listbox(window, width=30, height=5)
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")

listbox1.bind("<Double-Button-1>", get_listbox_data3)  # 連按2下綁定

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def get_listbox_data4(event):  # 列印所選結果
    obj = event.widget  # 取得事件的物件
    indexs = obj.curselection()  # 取得索引
    for index in indexs:  # 將元組內容列出
        print(obj.get(index))
    print("----------")  # 區隔輸出


var = tk.StringVar()
lab = tk.Label(window, text="", textvariable=var)
lab.pack()

listbox1 = tk.Listbox(window, width=30, height=5, selectmode=tk.EXTENDED)
listbox1.pack()

listbox1.insert(tk.END, "鼠")
listbox1.insert(tk.END, "牛")
listbox1.insert(tk.END, "虎")

listbox1.bind("<<ListboxSelect>>", get_listbox_data4)  # 點選綁定

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def getIndex(event):  # 處理按一下選項
    listbox1.index = listbox1.nearest(event.y)  # 目前選項的索引


def dragJob(event):  # 處理拖曳選項
    newIndex = listbox1.nearest(event.y)  # 目前選項的新索引
    if newIndex < listbox1.index:  # 往上拖曳
        x = listbox1.get(newIndex)  # 獲得新位置內容
        listbox1.delete(newIndex)  # 刪除新位置的內容
        listbox1.insert(newIndex + 1, x)  # 放回原先新位置的內容
        listbox1.index = newIndex  # 選項的新索引
    elif newIndex > listbox1.index:  # 往下拖曳
        x = listbox1.get(newIndex)  # 獲得新位置內容
        listbox1.delete(newIndex)  # 刪除新位置的內容
        listbox1.insert(newIndex - 1, x)  # 放回原先新位置的內容
        listbox1.index = newIndex  # 選項的新索引

listbox1 = tk.Listbox(window, width=30, height=5)
listbox1.pack()

animals = ["鼠", "牛", "虎", "兔"]

for animal in animals:  # 建立動物項目
    listbox1.insert(tk.END, animal)
    listbox1.bind("<Button-1>", getIndex)  # 按一下綁定getIndex
    listbox1.bind("<B1-Motion>", dragJob)  # 拖曳綁定dragJob

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("Listbox + Scrollbar")

window = tk.Tk()
window.geometry("600x800")
window.title("Listbox 3")

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

wordlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listbox1 = tk.Listbox(window, width=30, height=5, yscrollcommand=scrollbar.set)

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
    listbox1.insert(tk.END,varAdd)               # 將項目增加到Listbox
    entry.delete(0,tk.END)                 # 刪除Entry的內容

def itemDeleted():                      # 刪除項目處理程式
    index = listbox1.curselection()           # 取得所選項目索引
    if (len(index) == 0):               # 如果長度是0表示沒有選取
        return
    listbox1.delete(index)                    # 刪除選項    

entry = tk.Entry(window)
entry.grid(row=0,column=0,padx=5,pady=5)

# 建立增加按鈕
buttonAdd = tk.Button(window,text="增加",width=10,command=itemAdded)
buttonAdd.grid(row=0,column=1,padx=5,pady=5)

# 建立Listbox
listbox1 = tk.Listbox(window, width=30, height=5)
listbox1.grid(row=1,column=0,columnspan=2,padx=5,sticky=tk.W)

# 建立刪除按鈕
buttonDel = tk.Button(window,text="刪除",width=10,command=itemDeleted)
buttonDel.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)


"""


window = tk.Tk()
window.title("Listbox 4")

# 單選
LB1 = tk.Listbox(window, width=30, height=5)
tk.Label(window, text="單選：選擇你的課程").pack()

for item in ["Chinese", "English", "Math"]:
    LB1.insert(tk.END, item)
LB1.pack()

# 多選
listbox1 = tk.Listbox(window, width=30, height=5, selectmode=tk.EXTENDED)
tk.Label(window, text="多選：你會幾種編程語言").pack()

for item in ["python", "C++", "C", "Java", "Php"]:
    listbox1.insert(tk.END, item)

listbox1.insert(1, "JS", "Go", "R")
listbox1.delete(5, 6)
listbox1.select_set(0, 3)
listbox1.select_clear(0, 1)
print(listbox1.size())
print(listbox1.get(3))
print(listbox1.select_includes(3))
listbox1.pack()
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("200x200")
window.title("Listbox 5")

var1 = tk.StringVar()
l = tk.Label(window, bg="yellow", width=4, textvariable=var1)
l.pack()


def get_listbox_data6():
    value = listbox1.get(listbox1.curselection())
    var1.set(value)


b1 = tk.Button(
    window, text="print selection", width=15, height=2, command=get_listbox_data6
)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))

listbox1 = tk.Listbox(window, width=30, height=5, listvariable=var2)
listbox1.pack()

list_items = [1, 2, 3, 4]
for item in list_items:
    listbox1.insert("end", item)
listbox1.insert(1, "first")
listbox1.insert(2, "second")
listbox1.delete(2)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")
window.title("Listbox + Scrollbar use window")

yscrollbar = tk.Scrollbar(window)  # y軸scrollbar物件
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)# 靠右安置與父物件高度相同

# 建立Listbox, yscrollcommand指向yscrollbar.set方法
listbox1 = tk.Listbox(window, yscrollcommand=yscrollbar.set)
listbox1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#listbox1.pack(side=tk.LEFT, fill=tk.BOTH)

for i in range(50):  # 建立50筆項目
    listbox1.insert(tk.END, "第" + str(i) + "列")

yscrollbar.config(command=listbox1.yview)

window.mainloop()

print("------------------------------------------------------------")  # 60個



