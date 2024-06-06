import tkinter as tk

print('------------------------------------------------------------')	#60個

window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W) + 'x' + str(H)
#size = str(W) + 'x' + str(H) + '+' + str(x_st) + '+' + str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))

# 設定主視窗標題
title = 'Listbox 測試'
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

tk.Label(text = 'Listbox 測試').pack()
tk.Label(text = 'Scrollbar 測試').pack()

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

listbox = tk.Listbox(window, yscrollcommand = scrollbar.set)
#Listbox內加入項目
for i in range(100):
    listbox.insert(tk.END, str(i))
    
listbox.pack(side = tk.LEFT, fill = tk.BOTH)

scrollbar.config(command = listbox.yview)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

tk.Label(text = 'Listbox 測試').pack()

listbox = tk.Listbox(window)
#Listbox內加入項目
listbox.insert(tk.END, "a list entry")
for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)

listbox.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

print('------------------------------------------------------------')	#60個

print('Listbox + Scrollbar')

window = tk.Tk()
window.geometry("400x200")

scrollbar = tk.Scrollbar(window)
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

wordlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = tk.Listbox(window, yscrollcommand = scrollbar.set )

for line in range(26):
   list1.insert(tk.END, "字母: " + wordlist[line])

list1.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = list1.yview )

window.mainloop()

print('------------------------------------------------------------')	#60個



window = Tk()
window.geometry("600x400")

lb1 = Listbox(window)                             # 建立listbox 1
lb1.pack(side=LEFT,padx=5,pady=10)
lb2 = Listbox(window,height=5,relief="raised")    # 建立listbox 2
lb2.pack(anchor=N,side=LEFT,padx=5,pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = Tk()
window.geometry("600x400")

lb = Listbox(window)              # 建立listbox 
lb.insert(END,"AAAA")
lb.insert(END,"BBBB")
lb.insert(END,"CCCC")
lb.pack(pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

#多這個
lb = Listbox(window,selectmode=MULTIPLE)  # 建立可以多選項的listbox

for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

#多這個
lb = Listbox(window,selectmode=EXTENDED)  # 拖曳可以選擇多選項

for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window,selectmode=EXTENDED)      # 拖曳可以選擇多選項
for fruit in fruits:                        # 建立水果項目
    lb.insert(END,fruit)
lb.insert(ACTIVE,"Orange","Grapes","Mango") # 前面補充建立3個項目
lb.pack(pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window,selectmode=EXTENDED)      # 拖曳可以選擇多選項
for fruit in fruits:                        # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print("items數字 : ", lb.size())            # 列出選項數量

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.selection_set(0)             # 預設選擇第0個項目

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window,selectmode=EXTENDED)  # 拖曳可以選擇多選項
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)    
lb.pack(pady=10)
lb.selection_set(0,3)                   # 預設選擇第0-3索引項目

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.delete(1)                    # 刪除索引1的項目

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.delete(1,3)                  # 刪除索引1-3的項目

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1))                # 列印索引1的項目

window.mainloop()

print("------------------------------------------------------------")  # 60個

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1,3))              # 列印索引1-3的項目

window.mainloop()

print("------------------------------------------------------------")  # 60個

def callback():                 # 列印所選的項目                
    indexs = lb.curselection()
    for index in indexs:        # 取得索引值
        print(lb.get(index))    # 列印所選的項目
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)
button1 = Button(window,text="Print",command=callback)
button1.pack(pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def callback():                 # 列印檢查結果                
    print(lb.selection_includes(3))
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)

button1 = Button(window,text="Check",command=callback)
button1.pack(pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def itemAdded():                        # 增加項目處理程式
    varAdd = entry.get()                # 讀取Entry的項目
    if (len(varAdd.strip()) == 0):      # 沒有增加不處理
        return
    lb.insert(END,varAdd)               # 將項目增加到Listbox
    entry.delete(0,END)                 # 刪除Entry的內容

def itemDeleted():                      # 刪除項目處理程式
    index = lb.curselection()           # 取得所選項目索引
    if (len(index) == 0):               # 如果長度是0表示沒有選取
        return
    lb.delete(index)                    # 刪除選項    

window = Tk()
window.geometry("600x400")

entry = Entry(window)                     # 建立Entry            
entry.grid(row=0,column=0,padx=5,pady=5)

# 建立增加按鈕
buttonAdd = Button(window,text="增加",width=10,command=itemAdded)
buttonAdd.grid(row=0,column=1,padx=5,pady=5)

# 建立Listbox
lb = Listbox(window)
lb.grid(row=1,column=0,columnspan=2,padx=5,sticky=W)

# 建立刪除按鈕
buttonDel = Button(window,text="刪除",width=10,command=itemDeleted)
buttonDel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def itemsSorted():                  # 排序
    if (var.get() == True):         # 如果設定
        revBool = True              # 大到小排序是True
    else:
        revBool = False             # 大到小排序是False
    listTmp = list(lb.get(0,END))   # 取得項目內容
    sortedList = sorted(listTmp,reverse=revBool) # 執行排序
    lb.delete(0,END)                # 刪除原先Listbox內容
    for item in sortedList:         # 將排序結果插入Listbox
        lb.insert(END,item)
            
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window)                  # 建立Listbox          
for fruit in fruits:                # 建立水果項目
    lb.insert(END,fruit)
lb.pack(padx=10,pady=5)

# 建立排序按鈕
button1 = Button(window,text="排序",command=itemsSorted)
button1.pack(side=LEFT,padx=10,pady=5)

# 建立排序設定核取方塊
var = BooleanVar()
cb = Checkbutton(window,text="大到小排序",variable=var)
cb.pack(side=LEFT)

window.mainloop()


print('------------------------------------------------------------')	#60個

def itemSelected(event):        # 列出所選單一項目
    obj = event.widget          # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))     # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

var = StringVar()               # 建立標籤
lab = Label(window,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected) # 點選綁定
lb.pack(pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def itemSelected(event):        # 列出所選單一項目
    index = lb.curselection()   # 取得索引
    var.set(lb.get(index))      # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

var = StringVar()               # 建立標籤
lab = Label(window,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected) # 點選綁定
lb.pack(pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個


def itemSelected(event):        # 列出所選單一項目
    obj = event.widget          # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))     # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

var = StringVar()               # 建立標籤
lab = Label(window,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(window)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<Double-Button-1>",itemSelected) # 連按2下綁定
lb.pack(pady=5)

window.mainloop()


print('------------------------------------------------------------')	#60個


def itemsSelected(event):       # 列印所選結果
    obj = event.widget          # 取得事件的物件
    indexs = obj.curselection() # 取得索引
    for index in indexs:        # 將元組內容列出
        print(obj.get(index))
    print("----------")         # 區隔輸出
    
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

var = StringVar()               # 建立標籤
lab = Label(window,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(window,selectmode=EXTENDED)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemsSelected) # 點選綁定
lb.pack(pady=5)

window.mainloop()


print("------------------------------------------------------------")  # 60個

def getIndex(event):                    # 處理按一下選項
    lb.index = lb.nearest(event.y)      # 目前選項的索引
    
def dragJob(event):                     # 處理拖曳選項
    newIndex = lb.nearest(event.y)      # 目前選項的新索引
    if newIndex < lb.index:             # 往上拖曳
        x = lb.get(newIndex)            # 獲得新位置內容
        lb.delete(newIndex)             # 刪除新位置的內容
        lb.insert(newIndex+1,x)         # 放回原先新位置的內容
        lb.index = newIndex             # 選項的新索引
    elif newIndex > lb.index:           # 往下拖曳
        x = lb.get(newIndex)            # 獲得新位置內容
        lb.delete(newIndex)             # 刪除新位置的內容
        lb.insert(newIndex-1,x)         # 放回原先新位置的內容
        lb.index = newIndex             # 選項的新索引

fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

window = Tk()
window.geometry("600x400")

lb = Listbox(window)                      # 建立Listbox          
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
    lb.bind("<Button-1>",getIndex)      # 按一下綁定getIndex
    lb.bind("<B1-Motion>",dragJob)      # 拖曳綁定dragJob
lb.pack(padx=10,pady=10)

window.mainloop()



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


