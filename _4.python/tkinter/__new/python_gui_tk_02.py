# ch12_1.py
from tkinter import *
    
root = Tk()
root.title("ch12_1")                            # 視窗標題
root.geometry("300x210")                        # 視窗寬300高210

lb1 = Listbox(root)                             # 建立listbox 1
lb1.pack(side=LEFT,padx=5,pady=10)
lb2 = Listbox(root,height=5,relief="raised")    # 建立listbox 2
lb2.pack(anchor=N,side=LEFT,padx=5,pady=10)

root.mainloop()


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_2.py

# ch12_2.py
from tkinter import *
    
root = Tk()
root.title("ch12_2")            # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              # 建立listbox 
lb.insert(END,"Banana")
lb.insert(END,"Watermelon")
lb.insert(END,"Pineapple")
lb.pack(pady=10)

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_3.py

# ch12_3.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_3")            # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              # 建立listbox
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_4.py

# ch12_4.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_4")                    # 視窗標題
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=MULTIPLE)  # 建立可以多選項的listbox
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_5.py

# ch12_5.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_5")                    # 視窗標題
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)  # 拖曳可以選擇多選項
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_6.py

# ch12_6.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple"]

root = Tk()
root.title("ch12_6")                        # 視窗標題
root.geometry("300x210")                    # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)      # 拖曳可以選擇多選項
for fruit in fruits:                        # 建立水果項目
    lb.insert(END,fruit)
lb.insert(ACTIVE,"Orange","Grapes","Mango") # 前面補充建立3個項目
lb.pack(pady=10)

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_7.py

# ch12_7.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_7")                        # 視窗標題
root.geometry("300x210")                    # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)      # 拖曳可以選擇多選項
for fruit in fruits:                        # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print("items數字 : ", lb.size())            # 列出選項數量

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_8.py

# ch12_8.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_8")            # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.selection_set(0)             # 預設選擇第0個項目

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_9.py

# ch12_9.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_9")                    # 視窗標題
root.geometry("300x210")                # 視窗寬300高210

lb = Listbox(root,selectmode=EXTENDED)  # 拖曳可以選擇多選項
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)    
lb.pack(pady=10)
lb.selection_set(0,3)                   # 預設選擇第0-3索引項目

root.mainloop()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_10.py

# ch12_10.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_10")           # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.delete(1)                    # 刪除索引1的項目

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_11.py

# ch12_11.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_11")           # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.delete(1,3)                  # 刪除索引1-3的項目

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_12.py

# ch12_12.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_12")           # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1))                # 列印索引1的項目

root.mainloop()









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_13.py

# ch12_13.py
from tkinter import *
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_13")           # 視窗標題
root.geometry("300x210")        # 視窗寬300高210

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=10)
print(lb.get(1,3))              # 列印索引1-3的項目

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_14.py

# ch12_14.py
from tkinter import *
def callback():                 # 列印所選的項目                
    indexs = lb.curselection()
    for index in indexs:        # 取得索引值
        print(lb.get(index))    # 列印所選的項目
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_14")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

lb = Listbox(root,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)
btn = Button(root,text="Print",command=callback)
btn.pack(pady=5)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_15.py

# ch12_15.py
from tkinter import *
def callback():                 # 列印檢查結果                
    print(lb.selection_includes(3))
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_15")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

lb = Listbox(root,selectmode=MULTIPLE)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.pack(pady=5)
btn = Button(root,text="Check",command=callback)
btn.pack(pady=5)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_16.py

# ch12_16.py
from tkinter import *
def itemSelected(event):        # 列出所選單一項目
    obj = event.widget          # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))     # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_16")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_16_1.py

# ch12_16_1.py
from tkinter import *
def itemSelected(event):        # 列出所選單一項目
    index = lb.curselection()   # 取得索引
    var.set(lb.get(index))      # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_16_1")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_17.py

# ch12_17.py
from tkinter import *
def itemSelected(event):        # 列出所選單一項目
    obj = event.widget          # 取得事件的物件
    index = obj.curselection()  # 取得索引
    var.set(obj.get(index))     # 設定標籤內容
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_17")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<Double-Button-1>",itemSelected) # 連按2下綁定
lb.pack(pady=5)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_18.py

# ch12_18.py
from tkinter import *
def itemsSelected(event):       # 列印所選結果
    obj = event.widget          # 取得事件的物件
    indexs = obj.curselection() # 取得索引
    for index in indexs:        # 將元組內容列出
        print(obj.get(index))
    print("----------")         # 區隔輸出
    
          
fruits = ["Banana","Watermelon","Pineapple",
          "Orange","Grapes","Mango"]

root = Tk()
root.title("ch12_18")           # 視窗標題
root.geometry("300x250")        # 視窗寬300高250

var = StringVar()               # 建立標籤
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root,selectmode=EXTENDED)              
for fruit in fruits:            # 建立水果項目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemsSelected) # 點選綁定
lb.pack(pady=5)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_19.py

# ch12_19.py
from tkinter import *
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

root = Tk()
root.title("ch12_19")                   # 視窗標題

entry = Entry(root)                     # 建立Entry            
entry.grid(row=0,column=0,padx=5,pady=5)

# 建立增加按鈕
btnAdd = Button(root,text="增加",width=10,command=itemAdded)
btnAdd.grid(row=0,column=1,padx=5,pady=5)

# 建立Listbox
lb = Listbox(root)
lb.grid(row=1,column=0,columnspan=2,padx=5,sticky=W)

# 建立刪除按鈕
btnDel = Button(root,text="刪除",width=10,command=itemDeleted)
btnDel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_20.py

# ch12_20.py
from tkinter import *
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

root = Tk()
root.title("ch12_20")               # 視窗標題

lb = Listbox(root)                  # 建立Listbox          
for fruit in fruits:                # 建立水果項目
    lb.insert(END,fruit)
lb.pack(padx=10,pady=5)

# 建立排序按鈕
btn = Button(root,text="排序",command=itemsSorted)
btn.pack(side=LEFT,padx=10,pady=5)

# 建立排序設定核取方塊
var = BooleanVar()
cb = Checkbutton(root,text="大到小排序",variable=var)
cb.pack(side=LEFT)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_21.py

# ch12_21.py
from tkinter import *
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

root = Tk()
root.title("ch12_21")                   # 視窗標題

lb = Listbox(root)                      # 建立Listbox          
for fruit in fruits:                    # 建立水果項目
    lb.insert(END,fruit)
    lb.bind("<Button-1>",getIndex)      # 按一下綁定getIndex
    lb.bind("<B1-Motion>",dragJob)      # 拖曳綁定dragJob
lb.pack(padx=10,pady=10)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch12\ch12_22.py

# ch12_22.py
from tkinter import *


root = Tk()
root.title("ch12_22")                   # 視窗標題

scrollbar = Scrollbar(root)             # 建立捲軸
scrollbar.pack(side=RIGHT, fill=Y)

# 建立Listbox, yscrollcommand指向scrollbar.set方法
lb = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(50):                     # 建立50筆項目
    lb.insert(END, "Line " + str(i))
lb.pack(side=LEFT,fill=BOTH,expand=True)

scrollbar.config(command=lb.yview)

root.mainloop()












print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13a.py

# ch13_1.py
from tkinter import *

root = Tk()
root.title("ch13_1")                   # 視窗標題
root.geometry("300x180")

var = StringVar(root)
optionmenu = OptionMenu(root,var,"Python","Java","C")
optionmenu.pack()

root.mainloop()




#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_10.py

# ch13_10.py
from tkinter import *
from  tkinter.ttk  import *
def comboSelection(event):                      # 顯示選項
    labelVar.set(var.get())                     # 同步標籤內容                      
    
root = Tk()
root.title("ch13_10")                           # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)            # 建立Combobox
cb["value"] = ("Python","Java","C#","C")        # 設定選項內容
cb.current(0)                                   # 設定預設選項
cb.bind("<<ComboboxSelected>>",comboSelection)  # 綁定
cb.pack(side=LEFT,pady=10,padx=10)

labelVar = StringVar()
label = Label(root,textvariable=labelVar)       # 建立Label
labelVar.set(var.get())                         # 設定Label的初值
label.pack(side=LEFT)

root.mainloop()











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_2.py

# ch13_2.py
from tkinter import *

root = Tk()
root.title("ch13_2")                        # 視窗標題
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_3.py

# ch13_3.py
from tkinter import *

root = Tk()
root.title("ch13_3")                        # 視窗標題
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set("Python")                           # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_3_1.py

# ch13_3_1.py
from tkinter import *

root = Tk()
root.title("ch13_3_1")                        # 視窗標題
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set(omTuple[0])                         # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_4.py

# ch13_4.py
from tkinter import *
def printSelection():
    print("The selection is : ", var.get())
    
root = Tk()
root.title("ch13_4")                        # 視窗標題
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set("Python")                           # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack(pady=10)

btn = Button(root,text="Print",command=printSelection)
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_5.py

# ch13_5.py
from tkinter import *
from  tkinter.ttk  import *
 
root = Tk()
root.title("ch13_5")                        # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var,        # 建立Combobox
              value=("Python","Java","C#","C"))   
cb.pack(pady=10)

root.mainloop()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_6.py

# ch13_6.py
from tkinter import *
from  tkinter.ttk  import *
 
root = Tk()
root.title("ch13_6")                        # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)        # 建立Combobox
cb["value"] = ("Python","Java","C#","C")    # 設定選項內容  
cb.pack(pady=10)

root.mainloop()











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_7.py

# ch13_7.py
from tkinter import *
from  tkinter.ttk  import *
 
root = Tk()
root.title("ch13_7")                        # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)        # 建立Combobox
cb["value"] = ("Python","Java","C#","C")    # 設定選項內容
cb.current(0)                               # 設定預設選項
cb.pack(pady=10)

root.mainloop()











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_8.py

# ch13_8.py
from tkinter import *
from  tkinter.ttk  import *
 
root = Tk()
root.title("ch13_8")                        # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)        # 建立Combobox
cb["value"] = ("Python","Java","C#","C")    # 設定選項內容
var.set("Python")                           # 設定預設選項
cb.pack(pady=10)

root.mainloop()











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch13\ch13_9.py

# ch13_9.py
from tkinter import *
from  tkinter.ttk  import *
def printSelection():                               # 列印選項
    print(var.get())
    
root = Tk()
root.title("ch13_9")                                # 視窗標題
root.geometry("300x120")                    

var = StringVar()       
cb = Combobox(root,textvariable=var)                # 建立Combobox
cb["value"] = ("Python","Java","C#","C")            # 設定選項內容
cb.current(0)                                       # 設定預設選項
cb.pack(pady=10)

btn = Button(root,text="Print",command=printSelection) # 建立按鈕
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()











print("------------------------------------------------------------")  # 60個












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16a.py

# ch16_1.py
from tkinter import *
from tkinter import messagebox

def hello():
    messagebox.showinfo("Hello","歡迎使用功能表")

root = Tk()
root.title("ch16_1")
root.geometry("300x180")

# 建立最上層功能表
menubar = Menu(root)
menubar.add_command(label="Hello!",command=hello)
menubar.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()




#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_2.py

# ch16_2.py
from tkinter import *
from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","開新檔案")

root = Tk()
root.title("ch16_2")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_3.py

# ch16_3.py
from tkinter import *
from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","開新檔案")

root = Tk()
root.title("ch16_3")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_4.py

# ch16_4.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")
def openFile():
    messagebox.showinfo("New File","開啟舊檔")
def saveFile():
    messagebox.showinfo("New File","儲存檔案")
def saveAsFile():
    messagebox.showinfo("New File","另存新檔")
    
root = Tk()
root.title("ch16_4")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open File",command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_5.py

# ch16_5.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")
def openFile():
    messagebox.showinfo("New File","開啟舊檔")
def saveFile():
    messagebox.showinfo("New File","儲存檔案")
def saveAsFile():
    messagebox.showinfo("New File","另存新檔")
def aboutMe():
    messagebox.showinfo("New File","洪錦魁著")    
    
root = Tk()
root.title("ch16_5")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open File",command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy)
# 建立功能表類別物件,和將此功能表類別命名Help 
helpmenu = Menu(menubar)               
menubar.add_cascade(label="Help",menu=helpmenu)
# 在Help功能表內建立功能表清單
helpmenu.add_command(label="About me",command=aboutMe)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_6.py

# ch16_6.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")
def openFile():
    messagebox.showinfo("New File","開啟舊檔")
def saveFile():
    messagebox.showinfo("New File","儲存檔案")
def saveAsFile():
    messagebox.showinfo("New File","另存新檔")
def aboutMe():
    messagebox.showinfo("New File","洪錦魁著")    
    
root = Tk()
root.title("ch16_6")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile,underline=0)
filemenu.add_command(label="Open File",command=openFile,underline=0)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile,underline=0)
filemenu.add_command(label="Save As",command=saveAsFile,underline=5)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)
# 建立功能表類別物件,和將此功能表類別命名Help 
helpmenu = Menu(menubar)               
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
# 在Help功能表內建立功能表清單
helpmenu.add_command(label="About me",command=aboutMe,underline=1)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_7.py

# ch16_7.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")    
    
root = Tk()
root.title("ch16_7")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile,
                     accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)
root.config(menu=menubar)           # 顯示功能表物件
root.bind("<Control-N>",            # 快捷鍵綁定
          lambda event:messagebox.showinfo("New File","開新檔案"))

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_8.py

# ch16_8.py
from tkinter import *
from tkinter import messagebox
def findNext():
    messagebox.showinfo("Find Next","尋找下一筆")
def findPre():
    messagebox.showinfo("Find Pre","尋找上一筆")

root = Tk()
root.title("ch16_8")
root.geometry("300x180")

menubar = Menu(root)                        # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
# 首先在File功能表內建立find子功能表物件
findmenu = Menu(filemenu,tearoff=False)     # 取消分隔線
findmenu.add_command(label="Find Next",command=findNext)
findmenu.add_command(label="Find Pre",command=findPre)
filemenu.add_cascade(label="Find",menu=findmenu)
# 下列是增加分隔線和建立Exit!指令
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

root.config(menu=menubar)                   # 顯示功能表物件

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_9.py

# ch16_9.py
from tkinter import *
from tkinter import messagebox
def minimizeIcon():                     # 縮小視窗為圖示
    root.iconify()
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

root = Tk()
root.title("ch16_9")
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立2個指令清單
popupmenu.add_command(label="Minimize",command=minimizeIcon)
popupmenu.add_command(label="Exit",command=root.destroy)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

root.mainloop()













print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_10.py

# ch16_10.py
from tkinter import *

def status():                       # 設定是否顯示狀態列
    if demoStatus.get():
        statusLabel.pack(side=BOTTOM,fill=X)
    else:
        statusLabel.pack_forget()
       
root = Tk()
root.title("ch16_10")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單Exit
filemenu.add_command(label="Exit",command=root.destroy)
# 建立功能表類別物件,和將此功能表類別命名View 
viewmenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="View",menu=viewmenu)
# 在View功能表內建立Check menu button
demoStatus = BooleanVar()
demoStatus.set(True)
viewmenu.add_checkbutton(label="Status",command=status,
                         variable=demoStatus)
root.config(menu=menubar)           # 顯示功能表物件

statusVar = StringVar()
statusVar.set("顯示")
statusLabel = Label(root,textvariable=statusVar,relief="raised")
statusLabel.pack(side=BOTTOM,fill=X)

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch16\ch16_11.py

# ch16_11.py
from tkinter import *
       
root = Tk()
root.title("ch16_11")
root.geometry("300x180")

menubar = Menu(root)                    # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單Exit
filemenu.add_command(label="Exit",command=root.destroy)

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=3)
# 在工具列內建立按紐
sunGif = PhotoImage(file="sun.gif")
exitBtn = Button(toolbar,image=sunGif,command=root.destroy)
exitBtn.pack(side=LEFT,padx=3,pady=3)   # 包裝按鈕
toolbar.pack(side=TOP,fill=X)           # 包裝工具列
root.config(menu=menubar)               # 顯示功能表物件

root.mainloop()













print("------------------------------------------------------------")  # 60個









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17a.py

# ch17_1.py
from tkinter import *

root = Tk()
root.title("ch17_1")

text = Text(root,height=2,width=30)
text.pack()

root.mainloop()





#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_2.py

# ch17_2.py
from tkinter import *

root = Tk()
root.title("ch17_2")

text = Text(root,height=3,width=30)
text.pack()
text.insert(END,"Python王者歸來\nJava王者歸來\n")
text.insert(INSERT,"深石數位公司")

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_3.py

# ch17_3.py
from tkinter import *

root = Tk()
root.title("ch17_3")

text = Text(root,height=3,width=30)
text.pack()
str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END,str)

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_4.py

# ch17_4.py
from tkinter import *

root = Tk()
root.title("ch17_4")

yscrollbar = Scrollbar(root)                # y軸scrollbar物件
text = Text(root,height=5,width=30)         
yscrollbar.pack(side=RIGHT,fill=Y)          # y軸scrollbar包裝顯示
text.pack()
yscrollbar.config(command=text.yview)       # y軸scrollbar設定
text.config(yscrollcommand=yscrollbar.set)  # Text控件設定

str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END,str)

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_5.py

# ch17_5.py
from tkinter import *

root = Tk()
root.title("ch17_5")

xscrollbar = Scrollbar(root,orient=HORIZONTAL)  # x軸scrollbar物件
yscrollbar = Scrollbar(root)                    # y軸scrollbar物件
text = Text(root,height=5,width=30,wrap="none")
xscrollbar.pack(side=BOTTOM,fill=X)             # x軸scrollbar包裝顯示
yscrollbar.pack(side=RIGHT,fill=Y)              # y軸scrollbar包裝顯示
text.pack()
xscrollbar.config(command=text.xview)           # x軸scrollbar設定
yscrollbar.config(command=text.yview)           # y軸scrollbar設定
text.config(xscrollcommand=xscrollbar.set)      # x軸scrollbar綁定text
text.config(yscrollcommand=yscrollbar.set)      # y軸scrollbar綁定text

str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END,str)

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_6.py

# ch17_6.py
from tkinter import *

root = Tk()
root.title("ch17_6")

xscrollbar = Scrollbar(root,orient=HORIZONTAL)  # x軸scrollbar物件
yscrollbar = Scrollbar(root)                    # y軸scrollbar物件
text = Text(root,height=5,width=30,wrap="none",bg="lightyellow")
xscrollbar.pack(side=BOTTOM,fill=X)             # x軸scrollbar包裝顯示
yscrollbar.pack(side=RIGHT,fill=Y)              # y軸scrollbar包裝顯示
text.pack(fill=BOTH,expand=True)
xscrollbar.config(command=text.xview)           # x軸scrollbar設定
yscrollbar.config(command=text.yview)           # y軸scrollbar設定
text.config(xscrollcommand=xscrollbar.set)      # x軸scrollbar綁定text
text.config(yscrollcommand=yscrollbar.set)      # y軸scrollbar綁定text

str = """Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system and
test content databases. The content for each topic is created
by experts and is all carefully designed with a comprehensive
knowledge to greatly benefit all candidates who participate. 
"""
text.insert(END,str)

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_7.py

# ch17_7.py
from tkinter import *
from tkinter.font import Font

def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
      
root = Tk()
root.title("ch17_7")
root.geometry("300x180")

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(root,familyVar,*familyFamily,command=familyChanged)
family.pack(pady=2)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_7_1.py

# ch17_7_1.py
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
      
root = Tk()
root.title("ch17_7_1")
root.geometry("300x180")

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(root,familyVar,*familyFamily,command=familyChanged)
family.pack(pady=2)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_8.py

# ch17_8.py
from tkinter import *
from tkinter.font import Font

def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
def weightChanged(event):                   # weight family更新
    f=Font(weight=weightVar.get())          # 取得新font weight
    text.configure(font=f)                  # 更新text的font weight
      
root = Tk()
root.title("ch17_8")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

# 建立font weight OptionMenu 
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_8_1.py

# ch17_8_1.py
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
def weightChanged(event):                   # weight family更新
    f=Font(weight=weightVar.get())          # 取得新font weight
    text.configure(font=f)                  # 更新text的font weight
      
root = Tk()
root.title("ch17_8_1")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

# 建立font weight OptionMenu 
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_9.py

# ch17_9.py
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
def familyChanged(event):                   # font family更新
    f=Font(family=familyVar.get())          # 取得新font family
    text.configure(font=f)                  # 更新text的font family
def weightChanged(event):                   # weight family更新
    f=Font(weight=weightVar.get())          # 取得新font weight
    text.configure(font=f)                  # 更新text的font weight
def sizeSelected(event):                    # size family更新
    f=Font(size=sizeVar.get())              # 取得新font size
    text.configure(font=f)                  # 更新text的font size    
      
root = Tk()
root.title("ch17_9")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font family OptionMenu 
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

# 建立font weight OptionMenu 
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack(side=LEFT)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()



print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_10.py

# ch17_10.py
from tkinter import *

def selectedText():                             # 列印所選的文字
    try:
        selText = text.get(SEL_FIRST,SEL_LAST)
        print("選取文字: ",selText)
    except TclError:
        print("沒有選取文字")
      
root = Tk()
root.title("ch17_10")
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print selection",command=selectedText)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song")    # 插入文字

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_11.py

# ch17_11.py
from tkinter import *

def selectedText():                             # 列印所選的文字
    try:
        selText = text.get(SEL_FIRST,SEL_LAST)
        print("選取文字: ",selText)
        print("selectionstart: ", text.index(SEL_FIRST))
        print("selectionend  : ", text.index(SEL_LAST))
    except TclError:
        print("沒有選取文字")
      
root = Tk()
root.title("ch17_11")
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print selection",command=selectedText)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song")    # 插入文字

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_12.py

# ch17_12.py
from tkinter import *

def printIndex():                               # 列印索引        
    print("INSERT : ", text.index(INSERT))
    print("CURRENT: ", text.index(CURRENT))
    print("END    : ", text.index(END))
      
root = Tk()
root.title("ch17_12")
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print index",command=printIndex)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song\n")  # 插入文字
text.insert(END,"夢醒時分")                     # 插入文字

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_13.py

# ch17_13.py
from tkinter import *
      
root = Tk()
root.title("ch17_13")
root.geometry("300x180")

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song\n")  # 插入文字
text.insert(1.14,"夢醒時分 ")                   # 插入文字

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_14.py

# ch17_14.py
from tkinter import *

root = Tk()
root.title("ch17_14")
root.geometry("300x180")

text = Text(root)

for i in range(1,10):
    text.insert(END,str(i) + ' Python GUI設計王者歸來 \n')

# 設定書籤
text.mark_set("mark1","5.0")
text.mark_set("mark2","8.0")

print(text.get("mark1","mark2"))
text.pack(fill=BOTH,expand=True)
              
root.mainloop()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_15.py

# ch17_15.py
from tkinter import *

root = Tk()
root.title("ch17_15")
root.geometry("300x180")

text = Text(root)

for i in range(1,10):
    text.insert(END,str(i) + ' Python GUI設計王者歸來 \n')

# 設定書籤
text.mark_set("mark1","5.0")
text.mark_set("mark2","8.0")

# 設定標籤
text.tag_add("tag1","mark1","mark2")
text.tag_config("tag1",foreground="blue",background="lightyellow")
text.pack(fill=BOTH,expand=True)
              
root.mainloop()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_16.py

# ch17_16.py
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                    # size family更新
    f=Font(size=sizeVar.get())              # 取得新font size
    text.tag_config(SEL,font=f)
      
root = Tk()
root.title("ch17_16")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")
text.focus_set()

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_17.py

# ch17_17.py
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def sizeSelected(event):                        # size family更新
    f=Font(size=sizeVar.get())                  # 取得新font size
    text.tag_config(SEL,font=f)
      
root = Tk()
root.title("ch17_17")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font size Combobox
sizeVar = IntVar()
size = Combobox(toolbar,textvariable=sizeVar)
sizeFamily = [x for x in range(8,30)]
size["value"] = sizeFamily
size.current(4)
size.bind("<<ComboboxSelected>>",sizeSelected)
size.pack()

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n","a")     # 插入時同時設定Tag
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")
text.focus_set()
# 將Tag a設為置中,藍色,含底線
text.tag_config("a",foreground="blue",justify=CENTER,underline=True)

root.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_18.py

# ch17_18.py
from tkinter import *
from tkinter import messagebox
def cutJob():                           # Cut方法
    copyJob()                           # 複製選取文字
    text.delete(SEL_FIRST,SEL_LAST)     # 刪除選取文字
def copyJob():                          # Copy方法
    try:
        text.clipboard_clear()          # 清除剪貼簿
        copyText = text.get(SEL_FIRST,SEL_LAST)             # 複製選取區域
        text.clipboard_append(copyText) # 寫入剪貼簿
    except TclError:
        print("沒有選取")
def pasteJob():                         # Paste方法
    try:
        copyText = text.selection_get(selection="CLIPBOARD") # 讀取剪貼簿內容
        text.insert(INSERT,copyText)        # 插入內容
    except TclError:
        print("剪貼簿沒有資料")
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

root = Tk()
root.title("ch17_18")
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_19.py

# ch17_19.py
from tkinter import *
from tkinter import messagebox
def cutJob():                           # Cut方法
    text.event_generate("<<Cut>>")
def copyJob():                          # Copy方法
    text.event_generate("<<Copy>>")
def pasteJob():                         # Paste方法
    text.event_generate("<<Paste>>")
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

root = Tk()
root.title("ch17_19")
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_20.py

# ch17_20.py
from tkinter import *
from tkinter import messagebox
def cutJob():                           # Cut方法
    text.event_generate("<<Cut>>")
def copyJob():                          # Copy方法
    text.event_generate("<<Copy>>")
def pasteJob():                         # Paste方法
    text.event_generate("<<Paste>>")
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)
def undoJob():                          # 復原undo方法
    try:
        text.edit_undo()
    except:
        print("先前未有動作")
def redoJob():                          # 重複redo方法
    try:
        text.edit_redo()
    except:
        print("先前未有動作")

root = Tk()
root.title("ch17_20")
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

# 建立Button
undoBtn = Button(toolbar,text="Undo",command=undoJob)
undoBtn.pack(side=LEFT,pady=2)
redoBtn = Button(toolbar,text="Redo",command=redoJob)
redoBtn.pack(side=LEFT,pady=2)

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_21.py

# ch17_21.py
from tkinter import *

def mySearch():
    text.tag_remove("found","1.0",END)              # 刪除標籤但是不刪除標籤定義
    start = "1.0"                                   # 設定搜尋起始位置
    key = entry.get()                               # 讀取搜尋關鍵字

    if (len(key.strip()) == 0):                     # 沒有輸入
        return
    while True:                                     # while迴圈搜尋        
        pos = text.search(key,start,END)            # 執行搜尋
        if (pos == ""):                             # 找不到結束while迴圈
            break
        text.tag_add("found",pos,"%s+%dc" % (pos, len(key)))    # 加入標籤
        start = "%s+%dc" % (pos, len(key))          # 更新搜尋起始位置
                         
root = Tk()
root.title("ch17_21")
root.geometry("300x180")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

entry = Entry()
entry.grid(row=0,column=0,padx=5,sticky=W+E)

btn = Button(root,text="搜尋",command=mySearch)
btn.grid(row=0,column=1,padx=5,pady=5)

# 建立Text
text = Text(root,undo=True)
text.grid(row=1,column=0,columnspan=2,padx=3,pady=5,
          sticky=N+S+W+E)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

text.tag_configure("found", background="yellow")    # 定義未來找到的標籤定義

root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_22.py

# ch17_22.py
from tkinter import *

def spellingCheck():
    text.tag_remove("spellErr","1.0",END)           # 刪除標籤但是不刪除標籤定義
    textwords = text.get("1.0",END).split()         # Text控件的內文
    print("字典內容\n",textwords)                   # 列印字典內容

    startChar = ("(")                               # 可能的啟始字元
    endChar = (".", ",", ":", ";", "?", "!", ")")   # 可能的結束字元
        
    start = "1.0"                                   # 檢查起始索引位置
    for word in textwords:     
        if word[0] in startChar:                    # 是否含非字母的啟始字元
            word = word[1:]                         # 刪除非字母的啟始字元         
        if word[-1] in endChar:                     # 是否含非字母的結束字元
            word = word[:-1]                        # 刪除非字母的結束字元                        
        if  (word not in dicts and word.lower() not in dicts):
            print("error", word)
            pos = text.search(word, start, END)
            text.tag_add("spellErr", pos, "%s+%dc" % (pos,len(word)))            
            pos = "%s+%dc" % (pos,len(word))     
    
def clrText():
    text.tag_remove("spellErr","1.0",END)
                            
root = Tk()
root.title("ch17_22")
root.geometry("300x180")

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

chkBtn = Button(toolbar,text="拼字檢查",command=spellingCheck)
chkBtn.pack(side=LEFT,padx=5,pady=5)

clrBtn = Button(toolbar,text="清除",command=clrText)
clrBtn.pack(side=LEFT,padx=5,pady=5)

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")

text.tag_configure("spellErr", foreground="red")    # 定義未來找到的標籤定義
with open("myDict.txt", "r") as dictObj:
    dicts = dictObj.read().split("\n")              # 自訂字典串列
    
root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_23.py

# ch17_23.py
from tkinter import *   
    
def saveFile():
    textContent = text.get("1.0",END)
    filename = "ch17_23.txt"
    with open(filename,"w") as output:
        output.write(textContent)
        root.title(filename)
                            
root = Tk()
root.title("Untitled")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")
    
root.mainloop()













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch17\ch17_29.py


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



