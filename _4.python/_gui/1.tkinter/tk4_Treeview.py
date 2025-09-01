"""
tk Treeview 範例
"""

import sys
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Treeview範例")

# 設定 Treeview 之標題
column_name = ("第0欄", "第1欄", "第2欄", "第3欄")  # tuple
print(type(column_name))
print(column_name)

treeview = ttk.Treeview(window, columns=column_name, show="headings")

# 加入標題方法一
treeview.heading("第0欄", text="第0欄")
treeview.heading("第1欄", text="第1欄")
treeview.heading("第2欄", text="第2欄")
treeview.heading("第3欄", text="第3欄")

""" 加入標題方法二
for col_name in column_name:
    treeview.heading(col_name, text = col_name)
"""

# treeview.grid(row = 5, column = 0, columnspan = 3, padx = 20, pady = 10)#another
treeview.pack(fill="both", expand=True)
# treeview.pack(expand = True, fill = 'y') another

animal1 = 1, "aaaa", "AAAA", 111
animal2 = 2, "bbbb", "BBBB", 222
animal3 = 3, "cccc", "CCCC", 333
animal4 = 4, "dddd", "DDDD", 444

print("加入項目到 Treeview, 插入在最後 4 筆")
treeview.insert("", tk.END, values=animal1)  # 加入項目到 Treeview, 插入在最後
treeview.insert("", tk.END, values=animal2)  # 加入項目到 Treeview, 插入在最後
treeview.insert("", tk.END, values=animal3)  # 加入項目到 Treeview, 插入在最後
treeview.insert("", tk.END, values=animal4)  # 加入項目到 Treeview, 插入在最後

print("加入項目到 Treeview, 插入在 index = 0")
treeview.insert(parent="", index=0, values=animal3)  # 插入在index = 0
treeview.insert(parent="", index=0, values=animal3)  # 插入在index = 0
treeview.insert(parent="", index=0, values=animal3)  # 插入在index = 0
treeview.insert(parent="", index=0, values=animal3)  # 插入在index = 0
treeview.insert("", 0, values=animal2)  # 插入在index = 0

print("加入項目到 Treeview, 插入在最後 1 筆")
treeview.insert(parent="", index=tk.END, values=(5, "XXXXX", "YYYYY", "ZZZZZ"))  # 插入在最後

"""
item = treeview.insert("", tk.END, text="Item 1")
treeview.insert(item, tk.END, text="Subitem 1")
"""


def show_info():
    """
    # Get the text of the item whose Id is stored in `my_iid`.
    text = treeview.item(my_iid, option="text")
    print(text)

    x=treeview.get_children()
    for item in x:
        print(x)
    """
    print("show_info")
    for item in treeview.selection():
        item_text = treeview.item(item, "values")
        print(item_text)


def item_select(_):
    print("你點選了", treeview.selection())
    for i in treeview.selection():
        print(treeview.item(i)["values"])
    # treeview.item(treeview.selection())


def delete_items(_):
    print("你刪除了", treeview.selection())
    for i in treeview.selection():
        treeview.delete(i)


def treeview_bind_function1(_):
    print("AAAA")


def treeview_bind_function2(_):
    print("BBBB")


def treeview_bind_function3(_):
    print("CCCC")


def treeview_bind_function4(_):
    print("DDDD")


treeview.bind("<<TreeviewSelect>>", item_select)
treeview.bind("<Delete>", delete_items)

treeview.bind("<<TreeviewOpen>>", treeview_bind_function1)
treeview.bind("<<TreeviewClose>>", treeview_bind_function2)
treeview.bind("<1>", treeview_bind_function3)

treeview.bind("<ButtonRelease-1>", treeview_bind_function4)


# 刪除 Treeview 內的所有項目
# treeview.delete(*treeview.get_children())

button = ttk.Button(text="Show info", command=show_info)
button.pack()

window.mainloop()

sys.exit()

print("------------------------------------------------------------")  # 60個

from random import randint, choice

window = tk.Tk()
window.geometry("600x800")
window.title("Scrolling")

# canvas
# canvas = tk.Canvas(window, bg = 'white', scrollregion = (0,0,2000,5000))
# canvas.create_line(0,0,2000,5000, fill = 'green', width = 10)
# for i in range(100):
# 	l = randint(0,2000)
# 	t = randint(0,5000)
# 	r = l + randint(10,500)
# 	b = t + randint(10,500)
# 	color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
# 	canvas.create_rectangle(l,t,r,b, fill = color)
# canvas.pack(expand = True, fill = 'both')

# # mousewheel scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

# # scrollbar
# scrollbar = ttk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
# canvas.configure(yscrollcommand = scrollbar.set)
# scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# # exercise:
# # create a horizontal scrollbar at the bottom and use it to scroll the canvas left and right
# scrollbar_bottom = ttk.Scrollbar(window, orient = 'horizontal', command = canvas.xview)
# canvas.configure(xscrollcommand = scrollbar_bottom.set)
# scrollbar_bottom.place(relx = 0, rely = 1, relwidth = 1, anchor = 'sw')

# # also add an event to scroll left / right on Ctrl + mousewheel
# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), "units"))

# text
# text = tk.Text(window)
# for i in range(1, 200):
# 	text.insert(f'{i}.0', f'text: {i} \n')
# text.pack(expand = True, fill = 'both')

# scrollbar_text = ttk.Scrollbar(window, orient = 'vertical', command = text.yview)
# text.configure(yscrollcommand = scrollbar_text.set)
# scrollbar_text.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# treeview
table = ttk.Treeview(window, columns=(1, 2), show="headings")
table.heading(1, text="First name")
table.heading(2, text="Last name")
first_names = [
    "Bob",
    "Maria",
    "Alex",
    "James",
    "Susan",
    "Henry",
    "Lisa",
    "Anna",
    "Lisa",
]
last_names = [
    "Smith",
    "Brown",
    "Wilson",
    "Thomson",
    "Cook",
    "Taylor",
    "Walker",
    "Clark",
]
for i in range(100):
    table.insert(
        parent="", index=tk.END, values=(choice(first_names), choice(last_names))
    )
table.pack(expand=True, fill="both")

scrollbar_table = ttk.Scrollbar(window, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor="ne")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("Treeview in Tk")
treeview = ttk.Treeview()

print("加入項目到 Treeview, 插入在最後 1 筆")
item = treeview.insert(parent="", index=tk.END, text="主項目")  # 插入在最後
print("加入子項目")
subitem = treeview.insert(item, tk.END, text="加入子項目")
print("加入子項目")
treeview.insert(subitem, tk.END, text="加入孫項目")

treeview.pack()
window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import ttk

window = tk.Tk()
window.title("Treeview in Tk")
treeview = ttk.Treeview()
my_iid = "unique_id"
treeview.insert("", tk.END, text="Item 1", iid=my_iid)
treeview.pack()

button = ttk.Button(text="Show info", command=show_info)
button.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

li = ["王記", "12", "男"]
window = tk.Tk()
window.title("測試")
tree = ttk.Treeview(window, columns=["1", "2", "3"], show="headings")
tree.column("1", width=100, anchor="center")
tree.column("2", width=100, anchor="center")
tree.column("3", width=100, anchor="center")
tree.heading("1", text="姓名")
tree.heading("2", text="學號")
tree.heading("3", text="性別")
tree.insert("", "end", values=li)
tree.grid()

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("標題點擊排序")

import random

window = tk.Tk()
columns = ("aaa", "bbb", "ccc")
treeview = ttk.Treeview(window, height=18, show="headings", columns=columns)  # 表格

treeview.column("aaa", width=50, anchor="center")
treeview.column("bbb", width=100, anchor="center")
treeview.column("ccc", width=80, anchor="center")
treeview.heading("aaa", text="列1")
treeview.heading("bbb", text="列2")
treeview.heading("ccc", text="列3")
treeview.pack(side=tk.LEFT, fill=tk.BOTH)

for i in range(10):
    treeview.insert(
        "",
        i,
        values=(
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
            str(random.randint(0, 9)),
        ),
    )


def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children("")]
    print(tv.get_children(""))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根據排序后索引移動
        tv.move(k, "", index)
        print(k)
    tv.heading(
        col, command=lambda: treeview_sort_column(tv, col, not reverse)
    )  # 重寫標題，使之成為再點倒序的標題


"""
#莫名其妙？？？？寫循環的話只有最后一列管用,看論壇說的好像是python2.7管用
for col in columns:
    treeview.heading(col, text=col, command=lambda: treeview_sort_column(treeview, col, False))
"""

"""
#基本用法（上邊注釋的只有最后一列管用、索性手工試驗一下可用性，證實可行）
treeview.heading('a', text='123', command=lambda: treeview_sort_column(tree, 'a', False))#重建標題，添加控件排序方法
treeview.heading('b', text='111', command=lambda: treeview_sort_column(tree, 'b', False))#重建標題，添加控件排序方法
treeview.heading('c', text='223', command=lambda: treeview_sort_column(tree, 'c', False))#重建標題，添加控件排序方法
"""

# 這個代碼對于python3就管用了
for col in columns:  # 給所有標題加（循環上邊的“手工”）
    treeview.heading(
        col,
        text=col,
        command=lambda _col=col: treeview_sort_column(treeview, _col, False),
    )

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import ttk  # 导入内部包

li = ["王记", "12", "男"]
window = tk.Tk()
window.title("测试")
tree = ttk.Treeview(window, columns=["1", "2", "3"], show="headings")

tree.column("1", width=100, anchor="center")
tree.column("2", width=100, anchor="center")
tree.column("3", width=100, anchor="center")

tree.heading("1", text="姓名")
tree.heading("2", text="学号")
tree.heading("3", text="性别")

tree.insert("", "end", values=li)
tree.grid()


def treeviewClick(event):  # 单击
    print("单击")
    for item in tree.selection():
        item_text = tree.item(item, "values")
        print(item_text[0])  # 输出所选行的第一列的值


tree.bind("<ButtonRelease-1>", treeviewClick)  # 绑定单击离开事件===========

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Treeview")
print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

# 建立Treeview
tree = Treeview(window, columns=("cities"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("#1", text="City")
# 建立內容
tree.insert("", index=tk.END, text="伊利諾", values="芝加哥")
tree.insert("", index=tk.END, text="加州", values="洛杉磯")
tree.insert("", index=tk.END, text="江蘇", values="南京")
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

# 建立Treeview
tree = Treeview(window, columns=("cities"), show="headings")
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("#1", text="City")
# 建立內容
tree.insert("", index=tk.END, text="伊利諾", values="芝加哥")
tree.insert("", index=tk.END, text="加州", values="洛杉磯")
tree.insert("", index=tk.END, text="江蘇", values="南京")
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

# 建立Treeview
tree = Treeview(window, columns=("cities"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("cities", text="City")
# 建立內容
tree.insert("", index=tk.END, text="伊利諾", values="芝加哥")
tree.insert("", index=tk.END, text="加州", values="洛杉磯")
tree.insert("", index=tk.END, text="江蘇", values="南京")
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

# 建立Treeview
tree = Treeview(window, columns=("cities", "populations"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("#1", text="City")
tree.heading("#2", text="Populations")
# 建立內容
tree.insert("", index=tk.END, text="伊利諾", values=("芝加哥", "800"))
tree.insert("", index=tk.END, text="加州", values=("洛杉磯", "1000"))
tree.insert("", index=tk.END, text="江蘇", values=("南京", "900"))
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

list1 = ["芝加哥", "800"]  # 以串列方式設定欄內容
list2 = ["洛杉磯", "1000"]
list3 = ["南京", "900"]
# 建立Treeview
tree = Treeview(window, columns=("cities", "populations"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("#1", text="City")
tree.heading("#2", text="Populations")
# 建立內容
tree.insert("", index=tk.END, text="伊利諾", values=list1)
tree.insert("", index=tk.END, text="加州", values=list2)
tree.insert("", index=tk.END, text="江蘇", values=list3)
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

# 建立Treeview
tree = Treeview(window, columns=("cities", "populations"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("#1", text="City")
tree.heading("#2", text="Populations")
# 格式化欄位
tree.column("#1", anchor=tk.CENTER, width=150)
tree.column("#2", anchor=tk.CENTER, width=150)
# 建立內容
tree.insert("", index=tk.END, text="伊利諾", values=("芝加哥", "800"))
tree.insert("", index=tk.END, text="加州", values=("洛杉磯", "1000"))
tree.insert("", index=tk.END, text="江蘇", values=("南京", "900"))
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

# 建立Treeview
tree = Treeview(window, columns=("cities", "populations"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("#1", text="City")
tree.heading("#2", text="Populations")
# 格式化欄位
tree.column("#1", anchor=tk.CENTER, width=150)
tree.column("#2", anchor=tk.CENTER, width=150)
# 建立內容
tree.insert("", index=tk.END, text="伊利諾", values=("芝加哥", "800"))
tree.insert("", index=tk.END, text="加州", values=("洛杉磯", "1000"))
tree.insert("", index=tk.END, text="江蘇", values=("南京", "900"))
tree.pack()
cityDict = tree.column("cities")
print(cityDict)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

stateCity = {
    "伊利諾": "芝加哥",
    "加州": "洛杉磯",
    "德州": "休士頓",
    "華盛頓州": "西雅圖",
    "江蘇": "南京",
    "山東": "青島",
    "廣東": "廣州",
    "福建": "廈門",
}
# 建立Treeview
tree = Treeview(window, columns=("cities"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("cities", text="City")
# 格式欄位
tree.column("cities", anchor=tk.CENTER)
# 建立內容,行號從1算起偶數行是用淺藍色底
tree.tag_configure("evenColor", background="lightblue")  # 設定標籤
rowCount = 1  # 行號從1算起
for state in stateCity.keys():
    if rowCount % 2 == 1:  # 如果True則是奇數行
        tree.insert("", index=tk.END, text=state, values=stateCity[state])
    else:
        tree.insert(
            "", index=tk.END, text=state, values=stateCity[state], tags=("evenColor")
        )  # 建立淺藍色底
    rowCount += 1  # 行號數加1
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

asia = {"中國": "北京", "日本": "東京", "泰國": "曼谷", "韓國": "首爾"}
euro = {"英國": "倫敦", "法國": "巴黎", "德國": "柏林", "挪威": "奧斯陸"}

# 建立Treeview
tree = Treeview(window, columns=("capital"))
# 建立欄標題
tree.heading("#0", text="國家")  # 圖標欄位icon column
tree.heading("capital", text="首都")
# 建立id
idAsia = tree.insert("", index=tk.END, text="Asia")
idEuro = tree.insert("", index=tk.END, text="Europe")
# 建立idAsia底下內容
for country in asia.keys():
    tree.insert(idAsia, index=tk.END, text=country, values=asia[country])
# 建立idEuro底下內容
for country in euro.keys():
    tree.insert(idEuro, index=tk.END, text=country, values=euro[country])
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *


def removeItem():  # 刪除所選項目
    iids = tree.selection()  # 取得所選項目
    for iid in iids:  # 所選項目可能很多所以用迴圈
        tree.delete(iid)  # 刪除所選項目


window = tk.Tk()
window.geometry("600x400")

stateCity = {
    "伊利諾": "芝加哥",
    "加州": "洛杉磯",
    "德州": "休士頓",
    "華盛頓州": "西雅圖",
    "江蘇": "南京",
    "山東": "青島",
    "廣東": "廣州",
    "福建": "廈門",
}
# 建立Treeview,可以有多項選擇selectmode=tk.EXTENDED
tree = Treeview(window, columns=("cities"), selectmode=tk.EXTENDED)
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("cities", text="City")
# 格式欄位
tree.column("cities", anchor=tk.CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("", index=tk.END, text=state, values=stateCity[state])
tree.pack()

rmButton = Button(window, text="Remove", command=removeItem)  # 刪除鈕
rmButton.pack(pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *


def removeItem():  # 刪除所選項目
    ids = tree.selection()  # 取得所選項目
    for id in ids:  # 所選項目可能很多所以用迴圈
        tree.delete(id)  # 刪除所選項目


def insertItem():
    state = stateEntry.get()  # 獲得stateEntry的輸入
    city = cityEntry.get()  # 獲得cityEntry的輸入
    # 如果輸入資料未完全不往下執行
    if len(state.strip()) == 0 or len(city.strip()) == 0:
        return
    tree.insert("", tk.END, text=state, values=(city))  # 插入
    stateEntry.delete(0, tk.END)  # 刪除stateEntry
    cityEntry.delete(0, tk.END)  # 刪除cityEntry


window = tk.Tk()
window.geometry("600x400")

stateCity = {
    "伊利諾": "芝加哥",
    "加州": "洛杉磯",
    "德州": "休士頓",
    "華盛頓州": "西雅圖",
    "江蘇": "南京",
    "山東": "青島",
    "廣東": "廣州",
    "福建": "廈門",
}
# 以下3行主要是應用在縮放視窗
window.rowconfigure(1, weight=1)  # row1會隨視窗縮放1:1變化
window.columnconfigure(1, weight=1)  # column1會隨視窗縮放1:1變化
window.columnconfigure(3, weight=1)  # column3會隨視窗縮放1:1變化

stateLab = Label(window, text="State :")  # 建立State :標籤
stateLab.grid(row=0, column=0, padx=5, pady=3, sticky=tk.W)

stateEntry = Entry()  # 建立State :文字方塊
stateEntry.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5, pady=3)

cityLab = Label(window, text="City : ")  # 建立City :標籤
cityLab.grid(row=0, column=2, sticky=tk.E)

cityEntry = Entry()  # 建立City :文字方塊
cityEntry.grid(row=0, column=3, sticky=tk.W + tk.E, padx=5, pady=3)
# 建立Insert按鈕
inButton = Button(window, text="插入", command=insertItem)
inButton.grid(row=0, column=4, padx=5, pady=3)
# 建立Treeview,可以有多項選擇selectmode=EXTENDED
tree = Treeview(window, columns=("cities"), selectmode=tk.EXTENDED)
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("cities", text="City")
# 格式欄位
tree.column("cities", anchor=tk.CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("", index=tk.END, text=state, values=stateCity[state])
tree.grid(row=1, column=0, columnspan=5, padx=5, sticky=tk.W + tk.E + tk.N + tk.S)

rmButton = Button(window, text="刪除", command=removeItem)  # 刪除鈕
rmButton.grid(row=2, column=2, padx=5, pady=3, sticky=tk.W)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *

window = tk.Tk()
window.geometry("600x400")

stateCity = {
    "Illinois": "芝加哥",
    "California": "洛杉磯",
    "Texas": "休士頓",
    "Washington": "西雅圖",
    "Jiangsu": "南京",
    "Shandong": "青島",
    "Guangdong": "廣州",
    "Fujian": "廈門",
    "Mississippi": "Oxford",
    "Kentucky": "Lexington",
    "Florida": "Miama",
    "Indiana": "West Lafeyette",
}

tree = Treeview(window, columns=("cities"))
yscrollbar = Scrollbar(window)  # y軸scrollbar物件
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)  # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("cities", text="City")
# 格式欄位
tree.column("cities", anchor=tk.CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("", index=tk.END, text=state, values=stateCity[state])

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *


def treeview_sortColumn(col):
    global reverseFlag  # 定義排序旗標全域變數
    lst = [(tree.set(st, col), st) for st in tree.get_children("")]
    print(lst)  # 列印串列
    lst.sort(reverse=reverseFlag)  # 排序串列
    print(lst)  # 列印串列
    for index, item in enumerate(lst):  # 重新移動項目內容
        tree.move(item[1], "", index)
    reverseFlag = not reverseFlag  # 更改排序旗標


window = tk.Tk()
window.geometry("600x400")

reverseFlag = False  # 排序旗標註明是否反向排序

myStates = {
    "Illinois",
    "California",
    "Texas",
    "Washington",
    "Jiangsu",
    "Shandong",
    "Guangdong",
    "Fujian",
    "Mississippi",
    "Kentucky",
    "Florida",
    "Indiana",
}

tree = Treeview(window, columns=("states"), show="headings")
yscrollbar = Scrollbar(window)  # y軸scrollbar物件
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)  # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("states", text="State")
# 建立內容
for state in myStates:  # 第一次的Treeview內容
    tree.insert("", index=tk.END, values=(state,))
# 點選標題欄將啟動treeview_sortColumn
tree.heading("#1", text="State", command=lambda c="states": treeview_sortColumn(c))

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *


def treeSelect(event):
    widgetObj = event.widget  # 取得控件
    itemselected = widgetObj.selection()[0]  # 取得選項
    col1 = widgetObj.item(itemselected, "text")  # 取得圖標欄內容
    col2 = widgetObj.item(itemselected, "values")[0]  # 取得第0索引欄位內容
    mesg = "{0} : {1}".format(col1, col2)  # 取得所選項目內容
    var.set(mesg)  # 設定狀態列內容


window = tk.Tk()
window.geometry("600x400")

stateCity = {
    "伊利諾": "芝加哥",
    "加州": "洛杉磯",
    "德州": "休士頓",
    "華盛頓州": "西雅圖",
    "江蘇": "南京",
    "山東": "青島",
    "廣東": "廣州",
    "福建": "廈門",
}
# 建立Treeview
tree = Treeview(window, columns=("cities"), selectmode=tk.BROWSE)
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("cities", text="City")
# 格式欄位
tree.column("cities", anchor=tk.CENTER)
# 建立內容,行號從1算起偶數行是用淺藍色底
tree.tag_configure("evenColor", background="lightblue")  # 設定標籤
rowCount = 1  # 行號從1算起
for state in stateCity.keys():
    if rowCount % 2 == 1:  # 如果True則是奇數行
        tree.insert("", index=tk.END, text=state, values=stateCity[state])
    else:
        tree.insert(
            "", index=tk.END, text=state, values=stateCity[state], tags=("evenColor")
        )  # 建立淺藍色底
    rowCount += 1  # 行號數加1

tree.bind("<<TreeviewSelect>>", treeSelect)  # Treeview控件Select發生
tree.pack()

var = tk.StringVar()
label = Label(window, textvariable=var, relief="groove")  # 建立狀態列
label.pack(fill=tk.BOTH, expand=True)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.ttk import *


def doubleClick(event):
    e = event.widget  # 取得事件控件
    iid = e.identify("item", event.x, event.y)  # 取得連按2下項目id
    state = e.item(iid, "text")  # 取得State
    city = e.item(iid, "values")[0]  # 取得City
    mesg = "{0} : {1}".format(state, city)  # 格式化
    print("Double Clicked :", mesg)  # 輸出


window = tk.Tk()
window.geometry("600x400")

stateCity = {
    "伊利諾": "芝加哥",
    "加州": "洛杉磯",
    "德州": "休士頓",
    "華盛頓州": "西雅圖",
    "江蘇": "南京",
    "山東": "青島",
    "廣東": "廣州",
    "福建": "廈門",
}

# 建立Treeview
tree = Treeview(window, columns=("cities"))
# 建立欄標題
tree.heading("#0", text="State")  # 圖標欄位icon column
tree.heading("cities", text="City")
# 格式欄位
tree.column("cities", anchor=tk.CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("", index=tk.END, text=state, values=stateCity[state])
tree.bind("<Double-1>", doubleClick)  # 連按2下綁定doubleClick方法
tree.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
Treeview之各種點擊事件

鼠標左鍵單擊按下	1/Button-1/ButtonPress-1
鼠標左鍵單擊松開	ButtonRelease-1
鼠標右鍵單擊	3
鼠標左鍵雙擊	Double-1/Double-Button-1
鼠標右鍵雙擊	Double-3
鼠標滾輪單擊	2
鼠標滾輪雙擊	Double-2
鼠標移動	B1-Motion
鼠標移動到區域	Enter
鼠標離開區域	Leave
獲得鍵盤焦點	FocusIn
失去鍵盤焦點	FocusOut
鍵盤事件	Key
回車鍵	Return
控件尺寸變	Configure

"""
