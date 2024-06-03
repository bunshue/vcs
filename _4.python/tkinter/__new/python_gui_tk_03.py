# ch18_1.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_1")

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("#1",text="City")
# 建立內容
tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

root.mainloop()




#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_1_1.py

# ch18_1_1.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_1_1")

# 建立Treeview
tree = Treeview(root,columns=("cities"),show="headings")
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("#1",text="City")
# 建立內容
tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_2.py

# ch18_2.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_2")

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 建立內容
tree.insert("",index=END,text="伊利諾",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉磯")
tree.insert("",index=END,text="江蘇",values="南京")
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_3.py

# ch18_3.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_3")

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 建立內容
tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_3_1.py

# ch18_3_1.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_3_1")

list1 = ["芝加哥","800"]               # 以串列方式設定欄內容         
list2 = ["洛杉磯","1000"]
list3 = ["南京","900"]
# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 建立內容
tree.insert("",index=END,text="伊利諾",values=list1)
tree.insert("",index=END,text="加州",values=list2)
tree.insert("",index=END,text="江蘇",values=list3)
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_4.py

# ch18_4.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_4")

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 格式化欄位
tree.column("#1",anchor=CENTER,width=150)
tree.column("#2",anchor=CENTER,width=150)
# 建立內容
tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_5.py

# ch18_5.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_5")

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 格式化欄位
tree.column("#1",anchor=CENTER,width=150)
tree.column("#2",anchor=CENTER,width=150)
# 建立內容
tree.insert("",index=END,text="伊利諾",values=("芝加哥","800"))
tree.insert("",index=END,text="加州",values=("洛杉磯","1000"))
tree.insert("",index=END,text="江蘇",values=("南京","900"))
tree.pack()
cityDict = tree.column("cities")
print(cityDict)

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_6.py

# ch18_6.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_6")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")             # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容,行號從1算起偶數行是用淺藍色底
tree.tag_configure("evenColor", background="lightblue") # 設定標籤
rowCount = 1                                # 行號從1算起
for state in stateCity.keys():
    if (rowCount % 2 == 1):                 # 如果True則是奇數行
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],
                    tags=("evenColor"))     # 建立淺藍色底
    rowCount += 1                           # 行號數加1
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_7.py

# ch18_7.py
from tkinter import *
from tkinter.ttk import *
      
root = Tk()
root.title("ch18_7")

asia = {"中國":"北京","日本":"東京","泰國":"曼谷","韓國":"首爾"}
euro = {"英國":"倫敦","法國":"巴黎","德國":"柏林","挪威":"奧斯陸"}
             
# 建立Treeview
tree = Treeview(root,columns=("capital"))
# 建立欄標題
tree.heading("#0",text="國家")             # 圖標欄位icon column
tree.heading("capital",text="首都")
# 建立id
idAsia = tree.insert("",index=END,text="Asia")
idEuro = tree.insert("",index=END,text="Europe")
# 建立idAsia底下內容
for country in asia.keys():
    tree.insert(idAsia,index=END,text=country,values=asia[country])
# 建立idEuro底下內容
for country in euro.keys():
    tree.insert(idEuro,index=END,text=country,values=euro[country])     
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_8.py

# ch18_8.py
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
      
root = Tk()
root.title("ch18_8")

Style().configure("Treeview",rowheight=35)  # 格式化擴充row高度

info = ["鳳凰新聞App可以獲得中國各地最新消息",
        "瑞士國家鐵路App提供全瑞士火車時刻表",
        "可口可樂App是一個娛樂的軟件"]

tree = Treeview(root,columns=("說明"))
tree.heading("#0",text="App")           # 圖標欄位icon column
tree.heading("#1",text="功能說明")
tree.column("#1",width=300)             # 格式化欄標題

img1 = Image.open("news.jpg")           # 插入鳳凰新聞App圖示
imgObj1 = ImageTk.PhotoImage(img1)
tree.insert("",index=END,text="鳳凰新聞",image=imgObj1,values=info[0])

img2 = Image.open("sbb.jpg")            # 插入瑞士國家鐵路App圖示
imgObj2 = ImageTk.PhotoImage(img2)
tree.insert("",index=END,text="瑞士鐵路",image=imgObj2,values=info[1])

img3 = Image.open("coca.jpg")           # 插入可口可樂App圖示          
imgObj3 = ImageTk.PhotoImage(img3)
tree.insert("",index=END,text="可口可樂",image=imgObj3,values=info[2])    
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_9.py

# ch18_9.py
from tkinter import *
from tkinter.ttk import *
def treeSelect(event):
    widgetObj = event.widget                # 取得控件
    itemselected = widgetObj.selection()[0] # 取得選項
    col1 = widgetObj.item(itemselected,"text")  # 取得圖標欄內容
    col2 = widgetObj.item(itemselected,"values")[0] # 取得第0索引欄位內容
    str = "{0} : {1}".format(col1,col2)     # 取得所選項目內容
    var.set(str)                            # 設定狀態列內容
         
root = Tk()
root.title("ch18_9")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview
tree = Treeview(root,columns=("cities"),selectmode=BROWSE)
# 建立欄標題
tree.heading("#0",text="State")             # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容,行號從1算起偶數行是用淺藍色底
tree.tag_configure("evenColor", background="lightblue") # 設定標籤
rowCount = 1                                # 行號從1算起
for state in stateCity.keys():
    if (rowCount % 2 == 1):                 # 如果True則是奇數行
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],
                    tags=("evenColor"))     # 建立淺藍色底
    rowCount += 1                           # 行號數加1

tree.bind("<<TreeviewSelect>>",treeSelect)  # Treeview控件Select發生
tree.pack()

var = StringVar()
label = Label(root,textvariable=var,relief="groove")    # 建立狀態列
label.pack(fill=BOTH,expand=True)

root.mainloop()





print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_10.py

# ch18_10.py
from tkinter import *
from tkinter.ttk import *
def removeItem():                   # 刪除所選項目
    iids = tree.selection()         # 取得所選項目
    for iid in iids:                # 所選項目可能很多所以用迴圈
        tree.delete(iid)            # 刪除所選項目
         
root = Tk()
root.title("ch18_10")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 建立Treeview,可以有多項選擇selectmode=EXTENDED
tree = Treeview(root,columns=("cities"),selectmode=EXTENDED)
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.pack()

rmBtn = Button(root,text="Remove",command=removeItem)   # 刪除鈕
rmBtn.pack(pady=5)

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_11.py

# ch18_11.py
from tkinter import *
from tkinter.ttk import *
def removeItem():                   # 刪除所選項目
    ids = tree.selection()          # 取得所選項目
    for id in ids:                  # 所選項目可能很多所以用迴圈
        tree.delete(id)             # 刪除所選項目
def insertItem():
    state = stateEntry.get()        # 獲得stateEntry的輸入
    city = cityEntry.get()          # 獲得cityEntry的輸入
# 如果輸入資料未完全不往下執行
    if (len(state.strip())==0 or len(city.strip())==0):
        return
    tree.insert("",END,text=state,values=(city))    # 插入
    stateEntry.delete(0,END)        # 刪除stateEntry
    cityEntry.delete(0,END)         # 刪除cityEntry
         
root = Tk()
root.title("ch18_11")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}
# 以下3行主要是應用在縮放視窗
root.rowconfigure(1,weight=1)       # row1會隨視窗縮放1:1變化
root.columnconfigure(1,weight=1)    # column1會隨視窗縮放1:1變化
root.columnconfigure(3,weight=1)    # column3會隨視窗縮放1:1變化

stateLab = Label(root,text="State :")   # 建立State :標籤
stateLab.grid(row=0,column=0,padx=5,pady=3,sticky=W)
stateEntry = Entry()                    # 建立State :文字方塊
stateEntry.grid(row=0,column=1,sticky=W+E,padx=5,pady=3)
cityLab = Label(root,text="City : ")    # 建立City :標籤
cityLab.grid(row=0,column=2,sticky=E)
cityEntry = Entry()                     # 建立City :文字方塊
cityEntry.grid(row=0,column=3,sticky=W+E,padx=5,pady=3)
# 建立Insert按鈕
inBtn = Button(root,text="插入",command=insertItem)
inBtn.grid(row=0,column=4,padx=5,pady=3)            
# 建立Treeview,可以有多項選擇selectmode=EXTENDED
tree = Treeview(root,columns=("cities"),selectmode=EXTENDED)
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.grid(row=1,column=0,columnspan=5,padx=5,sticky=W+E+N+S)

rmBtn = Button(root,text="刪除",command=removeItem)   # 刪除鈕
rmBtn.grid(row=2,column=2,padx=5,pady=3,sticky=W)

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_12.py

# ch18_12.py
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def doubleClick(event):
    e = event.widget                        # 取得事件控件
    iid = e.identify("item",event.x,event.y)    # 取得連按2下項目id
    state = e.item(iid,"text")              # 取得State
    city = e.item(iid,"values")[0]          # 取得City
    str = "{0} : {1}".format(state,city)    # 格式化
    messagebox.showinfo("Double Clicked",str)   # 輸出
         
root = Tk()
root.title("ch18_12")

stateCity = {"伊利諾":"芝加哥","加州":"洛杉磯",
             "德州":"休士頓","華盛頓州":"西雅圖",
             "江蘇":"南京","山東":"青島",
             "廣東":"廣州","福建":"廈門"}

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立欄標題
tree.heading("#0",text="State")     # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.bind("<Double-1>",doubleClick)     # 連按2下綁定doubleClick方法
tree.pack()

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_13.py

# ch18_13.py
from tkinter import *
from tkinter.ttk import *
         
root = Tk()
root.title("ch18_13")

stateCity = {"Illinois":"芝加哥","California":"洛杉磯",
             "Texas":"休士頓","Washington":"西雅圖",
             "Jiangsu":"南京","Shandong":"青島",
             "Guangdong":"廣州","Fujian":"廈門",
             "Mississippi":"Oxford","Kentucky":"Lexington",
             "Florida":"Miama","Indiana":"West Lafeyette"}

tree = Treeview(root,columns=("cities"))
yscrollbar = Scrollbar(root)            # y軸scrollbar物件
yscrollbar.pack(side=RIGHT,fill=Y)      # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)   # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("#0",text="State")         # 圖標欄位icon column
tree.heading("cities",text="City")
# 格式欄位
tree.column("cities",anchor=CENTER)
# 建立內容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch18\ch18_14.py

# ch18_14.py
from tkinter import *
from tkinter.ttk import *
def treeview_sortColumn(col):
    global reverseFlag                  # 定義排序旗標全域變數
    lst = [(tree.set(st, col), st) 
            for st in tree.get_children("")]
    print(lst)                          # 列印串列
    lst.sort(reverse=reverseFlag)       # 排序串列
    print(lst)                          # 列印串列
    for index, item in enumerate(lst):  # 重新移動項目內容
        tree.move(item[1],"",index)
    reverseFlag = not reverseFlag       # 更改排序旗標
            
root = Tk()
root.title("ch18_14")
reverseFlag = False                     # 排序旗標註明是否反向排序

myStates = {"Illinois","California","Texas","Washington",
            "Jiangsu","Shandong","Guangdong","Fujian",
            "Mississippi","Kentucky","Florida","Indiana"}

tree = Treeview(root,columns=("states"),show="headings")
yscrollbar = Scrollbar(root)            # y軸scrollbar物件
yscrollbar.pack(side=RIGHT,fill=Y)      # y軸scrollbar包裝顯示
tree.pack()
yscrollbar.config(command=tree.yview)   # y軸scrollbar設定
tree.configure(yscrollcommand=yscrollbar.set)
# 建立欄標題
tree.heading("states",text="State")
# 建立內容
for state in myStates:                  # 第一次的Treeview內容
    tree.insert("",index=END,values=(state,))
# 點選標題欄將啟動treeview_sortColumn
tree.heading("#1",text="State",
             command=lambda c="states": treeview_sortColumn(c))

root.mainloop()





print("------------------------------------------------------------")  # 60個


# ch19_1.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])







#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_2.py

# ch19_2.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(100,100,500,100)
canvas.create_line(100,125,500,125,width=5)
canvas.create_line(100,150,500,150,width=10,fill='blue')
canvas.create_line(100,175,500,175,dash=(10,2,2,2))









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_3.py

# ch19_3.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(30,30,500,30,265,100,30,30,
                   width=20,joinstyle=ROUND)
canvas.create_line(30,130,500,130,265,200,30,130,
                   width=20,joinstyle=BEVEL)
canvas.create_line(30,230,500,230,265,300,30,230,
                   width=20,joinstyle=MITER)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_4.py

# ch19_4.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(30,30,500,30,width=10,capstyle=BUTT)
canvas.create_line(30,130,500,130,width=10,capstyle=ROUND)
canvas.create_line(30,230,500,230,width=10,capstyle=PROJECTING)
# 以下垂直線
canvas.create_line(30,20,30,240)
canvas.create_line(500,20,500,250)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_5.py

# ch19_5.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(30,30,500,30,width=10,stipple="gray25")
canvas.create_line(30,130,500,130,width=40,stipple="questhead")
canvas.create_line(30,230,500,230,width=10,stipple="info")










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_5_1.py

# ch19_5_1.py
from tkinter import * 
    
window = Tk()           
window.title("ch19_5_1")  

xWidth = 200
yHeight = 200
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
for i in range(19):
    canvas.create_line(10, 10+10*i, xWidth - 10, 10+10*i)
    canvas.create_line(10+10*i, 10, 10+10*i, yHeight - 10)
        
window.mainloop() 



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_6.py

# ch19_6.py
from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
for i in range(50):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas.create_rectangle(x1, y1, x2, y2)














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_7.py

# ch19_7.py
from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_rectangle(10, 10, 120, 60, fill='red')
canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_7_1.py

# ch19_7_1.py
from tkinter import * 
    
window = Tk()           
window.title("ch19_7_1")  

xWidth = 400
yHeight = 250
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
for i in range(20):
    canvas.create_rectangle(10 + i * 5, 10 + i * 5, 
        xWidth - 10 - i * 5, yHeight - 10 - i * 5)
        
window.mainloop() 



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_8.py

# ch19_8.py
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下以圓形為基礎
canvas.create_arc(10, 10, 110, 110, extent=45, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=90, style=ARC)
canvas.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
canvas.create_arc(10, 110, 110, 210, extent=270, style=ARC)
canvas.create_arc(210, 110, 310, 210, extent=359, style=ARC, width=5)
# 以下以橢圓形為基礎
canvas.create_arc(10, 250, 310, 350, extent=90, style=ARC, start=90)
canvas.create_arc(320, 250, 620, 350, extent=180, style=ARC)
canvas.create_arc(10, 360, 310, 460, extent=270, style=ARC, outline='blue')
canvas.create_arc(320, 360, 620, 460, extent=359, style=ARC)










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_9.py

# ch19_9.py
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下以圓形為基礎
canvas.create_arc(10, 10, 110, 110, extent=180, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=180, style=CHORD)
canvas.create_arc(410, 10, 510, 110, start=30, extent=120, style=PIESLICE)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_9_1.py

# ch19_9_1.py
from tkinter import * 
    
window = Tk()           
window.title("ch19_9_1")  

xWidth = 400
yHeight = 250
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
for i in range(20):
    canvas.create_oval(10+i*5, 10+i*5, xWidth-10-i*5, yHeight-10-i*5)
        
window.mainloop() 



print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_10.py

# ch19_10.py
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下是圓形
canvas.create_oval(10, 10, 110, 110)
canvas.create_oval(150, 10, 300, 160, fill='yellow')
# 以下是橢圓形
canvas.create_oval(10, 200, 310, 350)
canvas.create_oval(350, 200, 550, 300, fill='aqua', outline='blue', width=5)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_11.py

# ch19_11.py
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
canvas.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
canvas.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
canvas.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_12.py

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=640, height=480)
canvas.pack()
canvas.create_text(200, 50, text='Welcome to the United States')
canvas.create_text(200, 80, text='Welcome to the United States', fill='blue')
canvas.create_text(300, 120, text='Welcome to the United States', fill='blue',
                   font=('Old English Text MT',20))
canvas.create_text(300, 160, text='Welcome to the United States', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
canvas.create_text(300, 200, text='歡迎來到美國', fill='blue',
                   font=('華康新綜藝體 Std W7',20))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_13.py

# ch19_13.py
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=240, bg='yellow')
canvas.pack()












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_14.py


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_15.py

# ch19_15.py
from tkinter import *
def paint(event):                           # 拖曳可以繪圖
    x1,y1 = (event.x, event.y)              # 設定左上角座標
    x2,y2 = (event.x, event.y)              # 設定右下角座標
    canvas.create_oval(x1,y1,x2,y2,fill="blue")
def cls():                                  # 清除畫面
    canvas.delete("all")
    
tk = Tk()
lab = Label(tk,text="拖曳滑鼠可以繪圖")     # 建立標題
lab.pack()
canvas = Canvas(tk,width=640, height=300)   # 建立畫布
canvas.pack()

btn = Button(tk,text="清除",command=cls)    # 建立清除按鈕
btn.pack(pady=5)

canvas.bind("<B1-Motion>",paint)            # 滑鼠拖曳綁定paint

canvas.mainloop()














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_16.py

# ch19_16.py
from tkinter import *
import time

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 0)        # ID=1 x軸移動5像素, y軸不變
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_17.py

# ch19_17.py
from tkinter import *
import time

tk = Tk()
canvas= Canvas(tk, width=500, height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 2)        # ID=1 x軸移動5像素, y軸移動2像素
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_17_1.py

# ch19_17_1.py
from tkinter import *

tk = Tk()
canvas= Canvas(tk, width=500, height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 2)        # ID=1 x軸移動5像素, y軸移動2像素
    tk.update()                 # 強制tkinter重繪
    canvas.after(50)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_18.py

# ch19_18.py
from tkinter import *
import time

tk = Tk()
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow')
id2 = canvas.create_oval(10,150,60,200,fill='aqua')
for x in range(0, 80):
    canvas.move(id1, 5, 0)      # id1 x軸移動5像素, y軸移動0像素
    canvas.move(id2, 5, 0)      # id2 x軸移動5像素, y軸移動0像素
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_19.py

# ch19_19.py
from tkinter import *
from random import *
import time

tk = Tk()
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow')
id2 = canvas.create_oval(10,150,60,200,fill='aqua')
for x in range(0, 100):
    if randint(1,100) > 70:
        canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
    else:
        canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素    
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_20.py

# ch19_20.py
from tkinter import *
import time
def ballMove(event):
    if event.keysym == 'Left':  # 左移
        canvas.move(1, -5, 0)
    if event.keysym == 'Right': # 右移
        canvas.move(1, 5, 0)
    if event.keysym == 'Up':    # 上移
        canvas.move(1, 0, -5)
    if event.keysym == 'Down':  # 下移
        canvas.move(1, 0, 5)
tk = Tk()
canvas= Canvas(tk, width=500, height=300)
canvas.pack()
canvas.create_oval(225,125,275,175,fill='red')
canvas.bind_all('<KeyPress-Left>', ballMove)
canvas.bind_all('<KeyPress-Right>', ballMove)
canvas.bind_all('<KeyPress-Up>', ballMove)
canvas.bind_all('<KeyPress-Down>', ballMove)
mainloop()








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_20_4.py

# ch19_20_4.py
from tkinter import * 

window = Tk() 
window.title("ch19_20_4") 
        
xWidth = 300
yHeight = 100
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
x = 0
yMsg = 45
canvas.create_text(x, yMsg, text="王者歸來", tags="msg")
        
dx = 5
while True:
    canvas.move("msg", dx, 0)  
    canvas.after(100)       
    canvas.update()         
    if x < xWidth:
        x += dx             
    else:
        x = 0               
        canvas.delete("msg")                             
        canvas.create_text(x, yMsg, text = "王者歸來", tags = "msg")
                
window.mainloop() 



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_20_5.py

# ch19_20_5.py
from tkinter import * 

def up(event):
    global y
    canvas.create_line(x, y, x, y - 5)
    y -= 5       
def down(event):
    global y
    canvas.create_line(x, y, x, y + 5)
    y += 5       
def left(event):
    global x
    canvas.create_line(x, y, x - 5, y)
    x -= 5  
def right(event):
    global x
    canvas.create_line(x, y, x + 5, y)
    x += 5

xWidth = 200
yHeight = 200

window = Tk() 
window.title("ch19_20_5") 

canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()

x = xWidth / 2
y = yHeight / 2
       
canvas.bind("<Up>", up)
canvas.bind("<Down>", down)
canvas.bind("<Left>", left)
canvas.bind("<Right>", right)
canvas.focus_set()
        
window.mainloop() 




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_20_6.py

# ch19_20_6.py
from tkinter import *
def displayFan(startingAngle):
    canvas.delete("fan")    
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 0, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 120, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 240, extent = 60, fill = "green", tags = "fan")        

xWidth = 300
yHeight = 300
r = 120

window = Tk() 
window.title("ch19_20_6") 
        
canvas = Canvas(window,width=xWidth, height=yHeight)
canvas.pack()

startAngle = 0
while True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(50) 
    canvas.update()
            
window.mainloop() 
        
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_20_7.py

# ch19_20_7.py
from tkinter import *
from random import *
def display():
    if Flag:       
        if ball.get() == "1":
            raceResult.set("恭喜你贏了, Ball 1勝利")
        else:
            raceResult.set("抱歉你輸了, Ball 1勝利")
    else:
        if ball.get() == "1":
            raceResult.set("抱歉你輸了, Ball 2勝利")
        else:
            raceResult.set("恭喜你贏了, Ball 2勝利")
    startBtn.set("重置")

def running():
    global Flag
    if startBtn.get() == "重置":
        startBtn.set("開始")
        raceResult.set("")
        canvas.delete('all')
        canvas.create_text(10,50,text="1")
        id1 = canvas.create_oval(20,50,70,100,fill='yellow')
        canvas.create_text(10,150,text="2")
        id2 = canvas.create_oval(20,150,70,200,fill='aqua')
        return
    canvas.delete('all')
    canvas.create_text(10,50,text="1")
    id1 = canvas.create_oval(20,50,70,100,fill='yellow')
    canvas.create_text(10,150,text="2")
    id2 = canvas.create_oval(20,150,70,200,fill='aqua')
    id1Loc, id2Loc = 0, 0
    for x in range(0, 100):
        if ball.get() == '1':
            weight = 40
            raceResult.set("")
        elif ball.get() == '2':
            weight = 60
            raceResult.set("")
        else:
            raceResult.set("輸入錯誤!")
            return
        if randint(1,100) > weight:
            canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
            id2Loc += 1
        else:
            canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素
            id1Loc += 1
        tk.update()                 # 強制tkinter重繪
        canvas.after(50)
    if id1Loc > id2Loc:
        Flag = True
    else:
        Flag = False
    display()

tk = Tk()
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
canvas.create_text(10,50,text="1")
canvas.create_oval(20,50,70,100,fill='yellow')
canvas.create_text(10,150,text="2")
canvas.create_oval(20,150,70,200,fill='aqua')

Flag = True                         # 判斷那一球勝利

frame = Frame(tk)                   # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入獲勝的球, 按鈕Button
Label(frame, text="那一個球獲勝 : ").pack(side=LEFT)
ball = StringVar()
ball.set("1or2")
entry = Entry(frame, textvariable=ball).pack(side=LEFT,padx=3)
startBtn = StringVar()
startBtn.set("開始")
Button(frame, textvariable=startBtn,command=running).pack(side=LEFT)
raceResult = StringVar()

Label(frame,width=16,textvariable=raceResult).pack(side=LEFT,padx=3)

tk.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_21.py

# ch19_21.py 
from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
    def ballMove(self):
        self.canvas.move(self.id, 0, step)      # step是正值表示往下移動

winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.03                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_22.py

# ch19_22.py
from tkinter import *

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_23.py

# ch19_23.py 
from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        self.x = 0                                  # 水平不移動
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_24.py

# ch19_24.py 
from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_25.py

# ch19_25.py 
from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_26.py

# ch19_26.py 
from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)    # 綁定按往右鍵
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)      # 綁定按往左鍵        
    def racketMove(self):                       # 設計球拍移動
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:                         # 移動時是否碰到畫布左邊
            self.x = 0
        elif pos[2] >= winW:                    # 移動時是否碰到畫布右邊
            self.x = 0
    def moveLeft(self, event):                 # 球拍每次向左移動的單位數
        self.x = -3
    def moveRight(self, event):                # 球拍每次向右移動的單位數
        self.x = 3
       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_27.py

# ch19_27.py 
from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def hitRacket(self, ballPos):                                       
        racketPos = self.canvas.coords(self.racket.id)
        if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
            if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
                return True
        return False
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        if self.hitRacket(ballPos) == True:     # 偵測是否撞到球拍
            self.y = -step    
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)    # 綁定按往右鍵
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)      # 綁定按往左鍵        
    def racketMove(self):                       # 設計球拍移動
        self.canvas.move(self.id, self.x, 0)
        racketPos = self.canvas.coords(self.id)
        if racketPos[0] <= 0:                   # 移動時是否碰到畫布左邊
            self.x = 0
        elif racketPos[2] >= winW:              # 移動時是否碰到畫布右邊
            self.x = 0
    def moveLeft(self, event):                  # 球拍每次向左移動的單位數
        self.x = -3
    def moveRight(self, event):                 # 球拍每次向右移動的單位數
        self.x = 3
       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while True:
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_28.py

# ch19_28.py 
from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = -step                              # 球先往上垂直移動單位
        self.notTouchBottom = True                  # 未接觸畫布底端
    def hitRacket(self, ballPos):                                       
        racketPos = self.canvas.coords(self.racket.id)
        if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
            if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
                return True
        return False
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        if self.hitRacket(ballPos) == True:     # 偵測是否撞到球拍
            self.y = -step
        if ballPos[3] >= winH:                  # 如果球接觸到畫布底端
            self.notTouchBottom = False
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)    # 綁定按往右鍵
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)      # 綁定按往左鍵        
    def racketMove(self):                       # 設計球拍移動
        self.canvas.move(self.id, self.x, 0)
        racketPos = self.canvas.coords(self.id)
        if racketPos[0] <= 0:                   # 移動時是否碰到畫布左邊
            self.x = 0
        elif racketPos[2] >= winW:              # 移動時是否碰到畫布右邊
            self.x = 0
    def moveLeft(self, event):                  # 球拍每次向左移動的單位數
        self.x = -3
    def moveRight(self, event):                 # 球拍每次向右移動的單位數
        self.x = 3
       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while ball.notTouchBottom:                      # 如果球未接觸畫布底端                   
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_29.py

# ch19_29.py
from tkinter import * # Import tkinter
import random

# 傳回球的隨機顏色
def getColor():
    colorlist = ['red', 'green', 'blue', 'aqua', 'gold', 'purple']
    return random.choice(colorlist)
        
# 定義Ball類別
class Ball:
    def __init__(self):
        self.x = width / 2              # 發球的x軸座標 
        self.y = 0                      # 發球的y軸座標 
        self.dx = 3                     # 每次移動x距離
        self.dy = 3                     # 每次移動y距離
        self.radius = 5                 # 求半徑
        self.color = getColor()         # 隨機取得球的顏色

def addBall():                          # 增加球
    ballList.append(Ball())

def removeBall():                       # 刪除串列最後一個球 
    ballList.pop()

def stop():                             # 動畫停止
    global ballRunning
    ballRunning = True
    
def resume():                           # 恢復動畫
    global ballRunning
    ballRunning = False
    animate()   
                                
def animate():                          # 球體移動
    global ballRunning
    while not ballRunning:
        canvas.after(sleepTime)         
        canvas.update()                 # 更新
        canvas.delete("ball")             
        for ball in ballList:           # 更新所有球
            redisplayBall(ball)
    
def redisplayBall(ball):                # 重新顯示球
    if ball.x > width or ball.x < 0:
        ball.dx = -ball.dx            
    if ball.y > height or ball.y < 0:
        ball.dy = -ball.dy   
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                       ball.x + ball.radius, ball.y + ball.radius,
                       fill = ball.color, tags = "ball")
     
tk = Tk()
tk.title("ch19_29")                     
ballList = []                           # 建立球的串列
width, height = 400, 260
canvas = Canvas(tk, width=width, height=height)
canvas.pack()
        
frame = Frame(tk)                       # 建立下方功能紐
frame.pack()
btnStop = Button(frame, text = "暫停", command = stop)
btnStop.pack(side = LEFT)
btnResume = Button(frame, text = "恢復",command = resume)
btnResume.pack(side = LEFT)
btnAdd = Button(frame, text = "增加球", command = addBall)
btnAdd.pack(side = LEFT)
btnRemove = Button(frame, text = "減少球", command = removeBall)
btnRemove.pack(side = LEFT)
btnExit = Button(frame, text = "結束", command=tk.destroy)
btnExit.pack(side = LEFT)
        
sleepTime = 50                          # 動畫速度 
ballRunning = False
animate()
        
tk.mainloop() 



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch19\ch19_30.py

# ch19_30.py
from tkinter import * 
import tkinter.messagebox
import random 
        
def reset():
    ''' 重設長條圖 '''
    global i
    i = 0                               # 重設索引
    random.shuffle(mylist)
    newBar()

def go():                               
    ''' 執行排序 '''
    global i
    if i > len(mylist) - 1:
        tkinter.messagebox.showinfo("showinfo", "排序完成")
        return              
# 將mylist[i]插入mylist[0 .. i-1]
    currentValue = mylist[i]
    k = i - 1
# 找尋mylist[i]適當位置
    while k >= 0 and mylist[k] > currentValue:      
        mylist[k + 1] = mylist[k]
        k -= 1            
# 正式執行插入list[k + 1]
    mylist[k + 1] = currentValue

    newBar()                            # 繪製新的長條圖   
    i += 1                              # 增加串列指標
        
def newBar():
    global i, gap
    canvas.delete("line")               # 刪除bar
    canvas.delete("text")               # 刪除bar上方數字
    canvas.create_line(10, ht-gap, wd-10, ht-gap, tag="line")
    barWd = (wd - 20) / len(mylist)
        
    maxC = int(max(mylist))
    for j in range(len(mylist)):
        canvas.create_rectangle(j*barWd+10, (ht-gap)*(1-mylist[j]/(maxC+4)), 
                                (j+1)*barWd+10, ht-gap, tag="line")       
                         
        canvas.create_text(j*barWd+10+barWd/2, (ht-gap)*(1-mylist[j]/(maxC+4))-8, 
                           text=str(mylist[j]), tag = "text")

    if i >= 0:
        canvas.create_rectangle(i*barWd+10, (ht-gap)*(1-mylist[i]/(maxC+4)), 
                                (i + 1)*barWd+10, ht-gap, fill="blue", tag="line")


wd = 400                                # 視窗寬度
ht = 200                                # 視窗高度
gap = 20                                # 長條圖與視窗的間距
i = 0                                   # 這是目前排序指標

tk = Tk()                           
tk.title("ch19_30")                     # 視窗標題        
canvas = Canvas(tk, width = wd, height = ht)
canvas.pack()
        
frame = Frame(tk)
frame.pack()
        
btnStep = Button(frame, text = "執行", command = go)
btnStep.pack(side = LEFT)
btnReset = Button(frame, text = "重置", command = reset)
btnReset.pack(side = LEFT)
btnReset = Button(frame, text = "結束", command = tk.destroy)
btnReset.pack(side = LEFT)

mylist = [ x for x in range(1, 20) ]
reset()
newBar()
       
tk.mainloop()



print("------------------------------------------------------------")  # 60個




