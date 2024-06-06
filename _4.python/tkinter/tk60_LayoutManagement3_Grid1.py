"""
Grid 測試
"""

import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Grid 測試"
window.title(title)

w = 5
h = 2

for j in range(0, 5):
    for i in range(0, 16):
        label_n = tk.Label(window, text = str(i) + ',' + str(j))
        label_n.grid(row = j, column = i)

for j in range(0+5, 5+5):
    for i in range(0, 16):
        text_n = tk.Text(window, width = w, height = h)
        text_n.grid(row = j, column = i)

for j in range(0+5+5, 5+5+5):
    for i in range(0, 16):
        button_n = tk.Button(window, width = w, height = h, text = str(i) + ',' + str(j))
        button_n.grid(row = j, column = i)


text1 = tk.Text(window, width = w, height = h)  #原始數據錄入框
text1.grid(row = 1, column = 1)
#text1.grid(row = 1, column = 1, rowspan = 1, columnspan = 3)

button0 = tk.Button(window, text = "55", width = w, height = h)
button0.grid(row = 2, column = 2)
#button0.grid(row = 2, column = 2, rowspan = 1, columnspan = 3)

"""
若不指名 rowspan / columnspan, 則所佔為1格
會依據控件的大小 將所在格撐大成設定的格數
"""

"""
for j in range(4, 14, 3):
    for i in range(4, 14, 3):
        entry = tk.Entry(window, width = 10) #寬度為5個字
        if(i == 4):
            entry.grid(row = j, column = i) #預設, 占用1欄
        elif(i == 7):
            entry.grid(row = j, column = i, columnspan = 1) #占用1欄
        elif(i == 10):
            entry.grid(row = j, column = i, columnspan = 2) #占用2欄
        else:
            entry.grid(row = j, column = i, columnspan = 3) #占用3欄
"""
window.mainloop()

sys.exit()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Grid 測試"
window.title(title)

# create all of the main containers
top_frame = tk.Frame(window, bg = 'cyan', width = 450, height = 50, pady = 3)
center = tk.Frame(window, bg = 'gray2', width = 50, height = 40, padx = 3, pady = 3)

#layout all of the main containers
window.grid_rowconfigure(1, weight = 2)
window.grid_columnconfigure(0, weight = 1)

top_frame.grid(row = 0, sticky = "ew")
center.grid(row = 1, sticky = "nsew")

# create the widgets for the top frame
model_label = tk.Label(top_frame, text = 'Model Dimensions')
width_label = tk.Label(top_frame, text = 'Width:')
length_label = tk.Label(top_frame, text = 'Length:')
entry_W = tk.Entry(top_frame, background = 'pink')
entry_L = tk.Entry(top_frame, background = 'orange')

# layout the widgets in the top frame
model_label.grid(row = 0, columnspan = 3)
width_label.grid(row = 1, column = 0)
length_label.grid(row = 1, column = 2)
entry_W.grid(row = 1, column = 1)
entry_L.grid(row = 1, column = 3)

# create the center widgets
center.grid_rowconfigure(0, weight = 1)
center.grid_columnconfigure(1, weight = 1)

ctr_left = tk.Frame(center, bg = 'blue', width = 100, height = 190)
ctr_mid = tk.Frame(center, bg = 'yellow', width = 250, height = 190, padx = 3, pady = 3)
ctr_right = tk.Frame(center, bg = 'green', width = 100, height = 190, padx = 3, pady = 3)

ctr_left.grid(row = 0, column = 0, sticky = "ns")
ctr_mid.grid(row = 0, column = 1, sticky = "nsew")
ctr_right.grid(row = 0, column = 2, sticky = "ns")

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
Grid 測試 Button + Canvas
"""

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "Grid 測試"
window.title(title)

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame1 = tk.Frame(window, bg = 'yellow')
frame1.pack()

message = tk.Message(frame1, text = "這個訊息所佔的位置為3R2C")
message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
tk.Label(frame1, text = "姓 : ").grid(row = 1, column = 3)
tk.Entry(frame1).grid(row = 1, column = 4, padx = 5, pady = 5)
tk.Label(frame1, text = "名 : ").grid(row = 2, column = 3)
tk.Entry(frame1).grid(row = 2, column = 4)
tk.Button(frame1, text = "取得姓名").grid(row = 3, padx = 5, pady = 5, column = 4, sticky = tk.E)


#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame2 = tk.Frame(window, bg = 'pink')
frame2.pack()



#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame3 = tk.Frame(window, bg = 'cyan')
frame3.pack()

button00 = tk.Button(frame3, text = "第0排第0個", width = 20)
button00.grid(row = 0, column = 0, padx = 5, pady = 5)
button01 = tk.Button(frame3, text = "第0排第1個", width = 20)
button01.grid(row = 0, column = 1, padx = 5, pady = 5)
button02 = tk.Button(frame3, text = "第0排第2個", width = 20)
button02.grid(row = 0, column = 2, padx = 5, pady = 5)
button10 = tk.Button(frame3, text = "第1排第0個", width = 20)
button10.grid(row = 1, column = 0, padx = 5, pady = 5)
button11 = tk.Button(frame3, text = "第1排第1個", width = 20)
button11.grid(row = 1, column = 1, padx = 5, pady = 5)
button12 = tk.Button(frame3, text = "第1排第2個", width = 20)
button12.grid(row = 1, column = 2, padx = 5, pady = 5)

"""
frame3.columnconfigure(0, weight = 1)
frame3.columnconfigure(1, weight = 2)
#column 0 為基礎寬度，column 1 為column0的兩倍寬
"""
"""
frame3.columnconfigure((0, 2, 3), weight = 1)
frame3.columnconfigure(1, weight = 2)
frame3主視窗的，column 0 , 2, 3為基礎寬度，column 1 為其他column的兩倍寬
"""

button20 = tk.Button(frame3, text = "第2排第0個")
button20.grid(row = 2, column = 0, ipadx = 10, ipady = 10)
button21 = tk.Button(frame3, text = "第2排第1個")
button21.grid(row = 2, column = 1, ipadx = 10, ipady = 10)
button22 = tk.Button(frame3, text = "第2排第2個")
button22.grid(row = 2, column = 2, ipadx = 10, ipady = 10)

"""
參數Sticky填充元件大小
sticky 可以輸入N ,S, E, W或是 混搭例如:EW，NS，NSEW，代表靠N(北方) 、S(南方)、E(東方)、W(西方)，NS(北南延伸)，EW(東西延伸)，NSEW(全方位延伸)
"""

button30 = tk.Button(frame3, text = "第3排第0個")
button30.grid(row = 3, column = 0, ipadx = 10, ipady = 10, sticky = "EW")
button31 = tk.Button(frame3, text = "第3排第1個")
button31.grid(row = 3, column = 1, ipadx = 10, ipady = 10, sticky = "EW")
button32 = tk.Button(frame3, text = "第3排第2個")
button32.grid(row = 3, column = 2, ipadx = 10, ipady = 10, sticky = "EW")



window.mainloop()


print("------------------------------------------------------------")  # 60個


"""
Grid 測試 grid
"""


def get_data():
    print('取得資料')
    data1 = entry_1_0.get()
    data2 = entry_1_1.get()
    data3 = entry_1_2.get()
    data4 = int(spinbox_3_0.get())
    data5 = entry_3_1.get()
    data6 = float(spinbox_3_2.get())
    print(data1, data2, data3, data4, data5, data6)
    
def set_data():
    print('設定資料')
    

def clear_data():
    print('清除資料')
    entry_1_0.delete(0, tk.END)
    entry_1_1.delete(0, tk.END)
    entry_1_2.delete(0, tk.END)
    spinbox_3_0.delete(0, tk.END)
    spinbox_3_0.insert(0, "1")
    entry_3_1.delete(0, tk.END)
    spinbox_3_2.delete(0, tk.END)
    spinbox_3_2.insert(0, "0.0")

window = tk.Tk()
window.title("Grid 測試")

frame = tk.Frame(window, bg = 'magenta')
frame.pack(padx = 20, pady = 10)

print('第 0 row, Label')
label_0_0 = tk.Label(frame, text = "Label 0 0")
label_0_0.grid(row = 0, column = 0)
label_0_1 = tk.Label(frame, text = "Label 0 1")
label_0_1.grid(row = 0, column = 1)
label_0_2 = tk.Label(frame, text = "Label 0 2")
label_0_2.grid(row = 0, column = 2)

print('第 1 row, Entry')
entry_1_0 = tk.Entry(frame)
entry_1_0.grid(row = 1, column = 0)
entry_1_1 = tk.Entry(frame)
entry_1_1.grid(row = 1, column = 1)
entry_1_2 = tk.Entry(frame)
entry_1_2.grid(row = 1, column = 2)

print('第 2 row, Label')
label_2_0 = tk.Label(frame, text = "Label 2 0")
label_2_0.grid(row = 2, column = 0)
label_2_1 = tk.Label(frame, text = "Label 2 1")
label_2_1.grid(row = 2, column = 1)
label_2_2 = tk.Label(frame, text = "Label 2 2")
label_2_2.grid(row = 2, column = 2)

print('第 3 row, Spinbox Entry Spinbox')
spinbox_3_0 = tk.Spinbox(frame, from_ = 1, to = 100)
spinbox_3_0.grid(row = 3, column = 0)

entry_3_1 = tk.Entry(frame)
entry_3_1.grid(row = 3, column = 1)

spinbox_3_2 = tk.Spinbox(frame, from_ = 0.0, to = 500, increment = 0.5)
spinbox_3_2.grid(row = 3, column = 2)

print('第 4 row, Button')
button_4_0 = tk.Button(frame, text = "Button 4 0")
button_4_0.grid(row = 4, column = 0, pady = 5)

button_4_1 = tk.Button(frame, text = "Button 4 1")
button_4_1.grid(row = 4, column = 1, pady = 5)

button_4_2 = tk.Button(frame, text = "Button 4 2")
button_4_2.grid(row = 4, column = 2, pady = 5)

print('第 5 row, Button')
button_5_0 = tk.Button(frame, text = "取得資料", command = get_data)
button_5_0.grid(row = 5, column = 0, pady = 5)

button_5_1 = tk.Button(frame, text = "設定資料", command = set_data)
button_5_1.grid(row = 5, column = 1, pady = 5)

button_5_2 = tk.Button(frame, text = "清除資料", command = clear_data)
button_5_2.grid(row = 5, column = 2, pady = 5)

button_row6 = tk.Button(frame, text = "橫跨的大Button")
button_row6.grid(row = 6, column = 0, columnspan = 3, sticky = "news", padx = 20, pady = 5)
button_row7 = tk.Button(frame, text = "橫跨的大Button")
button_row7.grid(row = 7, column = 0, columnspan = 3, sticky = "news", padx = 20, pady = 5)

window.mainloop()



print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個






#grid 大全

print("grid")

print("grid版面佈局")

taipei=tk.Button(window, width=30, text="台北景點")
taipei.grid(column=0,row=0)
kaohsiung=tk.Button(window, width=30, text="高雄景點")
kaohsiung.grid(column=0,row=1)
ilan=tk.Button(window, width=30, text="宜蘭景點")
ilan.grid(column=1,row=0)
tainan=tk.Button(window, width=30, text="台南景點")
tainan.grid(column=1,row=1)
	

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("100x100")
window.title("grid佈局")

one=tk.Button(window, width=20, text="January")
one.grid(column=0,row=0)
two=tk.Button(window, width=20, text="Februry")
two.grid(column=1,row=0)
three=tk.Button(window, width=20, text="March")
three.grid(column=2,row=0)
one=tk.Button(window, width=20, text="April")
one.grid(column=0,row=1)
two=tk.Button(window, width=20, text="May")
two.grid(column=1,row=1)
three=tk.Button(window, width=20, text="June")
three.grid(column=2,row=1)
one=tk.Button(window, width=20, text="July")
one.grid(column=0,row=2)
two=tk.Button(window, width=20, text="August")
two.grid(column=1,row=2)
three=tk.Button(window, width=20, text="September")
three.grid(column=2,row=2)
one=tk.Button(window, width=20, text="October")
one.grid(column=0,row=3)
two=tk.Button(window, width=20, text="November")
two.grid(column=1,row=3)
three=tk.Button(window, width=20, text="December")
three.grid(column=2,row=3)

window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()

def add():                                  # 加法運算
    n3.set(n1.get()+n2.get())
    
n1 = tk.IntVar()                   
n2 = tk.IntVar()
n3 = tk.IntVar()

e1 = tk.Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = tk.Label(window,width=3,text='+')      # 加號
e2 = tk.Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = tk.Button(window,width=5,text='=',command=add)   # =按鈕
e3 = tk.Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btn.grid(row=1,column=1,pady=5)             # 定位=按鈕
e3.grid(row=2,column=1)                     # 定位儲存結果

window.mainloop()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


print("------------------------------------------------------------")  # 60個


window = tk.Tk()

lab1 = tk.Label(window,text="Peter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="John",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="Notron",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab4 = tk.Label(window,text="Kevin",
              bg="lightgreen",      # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab5 = tk.Label(window,text="Tommy",
              bg="lightblue",       # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab6 = tk.Label(window,text="Mary",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab7 = tk.Label(window,text="Tracy",
              bg="lightblue",       # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab8 = tk.Label(window,text="Mike",
              bg="lightyellow",     # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab9 = tk.Label(window,text="Vicent",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15

lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=0,column=1)           # 格狀包裝
lab3.grid(row=0,column=2)           # 格狀包裝
lab4.grid(row=1,column=0)           # 格狀包裝
lab5.grid(row=1,column=1)           # 格狀包裝
lab6.grid(row=1,column=2)           # 格狀包裝
lab7.grid(row=2,column=0)           # 格狀包裝
lab8.grid(row=2,column=1)           # 格狀包裝
lab9.grid(row=2,column=2)           # 格狀包裝

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="標籤1",relief="raised")
lab2 = tk.Label(window,text="標籤2",relief="raised")
lab3 = tk.Label(window,text="標籤3",relief="raised")
lab4 = tk.Label(window,text="標籤4",relief="raised")
lab5 = tk.Label(window,text="標籤5",relief="raised")
lab6 = tk.Label(window,text="標籤6",relief="raised")
lab7 = tk.Label(window,text="標籤7",relief="raised")
lab8 = tk.Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1)
lab3.grid(row=0,column=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=1)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="標籤1",relief="raised")
lab2 = tk.Label(window,text="標籤2",relief="raised")
lab4 = tk.Label(window,text="標籤4",relief="raised")
lab5 = tk.Label(window,text="標籤5",relief="raised")
lab6 = tk.Label(window,text="標籤6",relief="raised")
lab7 = tk.Label(window,text="標籤7",relief="raised")
lab8 = tk.Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,columnspan=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=1)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="標籤1",relief="raised")
lab2 = tk.Label(window,text="標籤2",relief="raised")
lab3 = tk.Label(window,text="標籤3",relief="raised")
lab4 = tk.Label(window,text="標籤4",relief="raised")
lab5 = tk.Label(window,text="標籤5",relief="raised")
lab7 = tk.Label(window,text="標籤7",relief="raised")
lab8 = tk.Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,rowspan=2)
lab3.grid(row=0,column=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def add():                                  # 加法運算
    n3.set(n1.get()+n2.get())
    
window = tk.Tk()

n1 = tk.IntVar()                   
n2 = tk.IntVar()
n3 = tk.IntVar()

e1 = tk.Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = tk.Label(window,width=3,text='+')      # 加號
e2 = tk.Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = tk.Button(window,width=5,text='=',command=add)   # =按鈕
e3 = tk.Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btn.grid(row=1,column=1,pady=5)             # 定位=按鈕
e3.grid(row=2,column=1)                     # 定位儲存結果

window.mainloop()

print("------------------------------------------------------------")  # 60個
          

window = tk.Tk()
window.geometry("400x100")
window.title("grid版面佈局的示範")

plus=tk.Button(window, width=20, text="加法範例")
plus.grid(column=0,row=0)
minus=tk.Button(window, width=20, text="減法範例")
minus.grid(column=0,row=1)
multiply=tk.Button(window, width=20, text="乘法範例")
multiply.grid(column=1,row=0)
divide=tk.Button(window, width=20, text="除法範例")
divide.grid(column=1,row=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("400x100")
window.title("grid版面佈局的示範")

plus=tk.Button(window, width=20, text="加法範例")
plus.grid(column=0,row=0)
minus=tk.Button(window, width=20, text="減法範例")
minus.grid(column=0,row=1)
multiply=tk.Button(window, width=20, text="乘法範例")
multiply.grid(column=0,row=2)
divide=tk.Button(window, width=20, text="除法範例")
divide.grid(column=0,row=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
pLabel1= tk.Label(window, text="難度計算過程", fg="black", bg="silver", font=("新細明體",12),padx=20,pady=10 )


text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(window, textvariable=text1, width=15, justify=tk.CENTER)
ent1.grid(row=0, column=0, padx=5, pady=5)
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(window, textvariable=text2, width=15, justify=tk.CENTER)
ent2.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N)
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(window, textvariable=text3, width=15, justify=tk.CENTER)
ent3.grid(row=1, column=1, padx=5, pady=5)
"""

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# Frame測試
tk.Label(text = 'Frame測試').pack()
frame1 = tk.Frame(window)
frame1.pack()

label1 = tk.Label(frame1, text = "標籤一：")
entry1 = tk.Entry(frame1)
label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)

frame2 = tk.Frame(window)
frame2.pack()

button1 = tk.Button(frame2, text = "確定")
button2 = tk.Button(frame2, text = "取消")
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

print("------------------------------------------------------------")  # 60個

# window
window = tk.Tk()
window.geometry('500x500')

# widgets 
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'green', width = 10)
label3 = ttk.Label(window, text = 'Label 3', background = 'blue', width = 10)

# layout 
# label1.pack()
# label2.pack()

# grid 
window.columnconfigure((0,2), weight = 1, uniform = 'a')    #column 為  0 1 2
window.rowconfigure((0,2), weight = 1, uniform = 'a')       #row 為  0 1 2

"""
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0, sticky = 'nsew')
label3.grid(row = 0, column = 1)
"""

label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)
label3.grid(row = 0, column = 2)

window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝
tk.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""

label = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件


lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝


button1 = tk.Button(window, text='push1')
button2 = tk.Button(window, text='push2')
button3 = tk.Button(window, text='push3')

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=1)


"""



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#account - password

window = tk.Tk()

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)              # 文字方塊1
e2 = tk.Entry(window,show='*')     # 文字方塊2
e1.grid(row=0,column=1)         # 定位文字方塊1
e2.grid(row=1,column=1)         # 定位文字方塊2

window.mainloop()

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = tk.Tk()

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
btn1.grid(row=2,column=0)
btn2 = tk.Button(window,text="Quit",command=window.quit)
btn2.grid(row=2,column=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = tk.Tk()

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=tk.W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=tk.W,pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = tk.Tk()

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=tk.W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=tk.W,pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
    e1.delete(0,tk.END)                # 刪除文字方塊1
    e2.delete(0,tk.END)                # 刪除文字方塊2
          
window = tk.Tk()

lab1 = tk.Label(window,text="Account ").grid(row=0)
lab2 = tk.Label(window,text="Password").grid(row=1)

e1 = tk.Entry(window)                  # 文字方塊1
e2 = tk.Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = tk.Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=tk.W,pady=10)  
btn2 = tk.Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=tk.W,pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個



window = tk.Tk()
window.title(' GUI介面- Checkbutton 核取方塊')

def check(): #回應核取方塊變數狀態
   print('選取的炸物有:', var1.get(), var2.get()
         ,var3.get())

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
lb1=tk.Label(window, text = '請勾選要買的品項：', font = ft1)
lb1.grid(row = 0, column = 0)
item1 = '炸雞排'
var1 = tk.StringVar()
chk = tk.Checkbutton(window, text = item1, font = ft1,
    variable = var1, onvalue = item1, offvalue = '')
chk.grid(row = 1, column = 0)
item2 = '高麗菜'
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text = item2, font = ft1,
    variable = var2, onvalue = item2, offvalue = '')
chk2.grid(row = 2, column = 0)
item3 = '炸花枝'
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text = item3, font = ft1,
    variable = var3, onvalue = item3, offvalue = '')
chk3.grid(row = 3, column = 0)

btnQuit = tk.Button(window, text = '離開', font = ft2,
    command = window.destroy)
btnQuit.grid(row = 2, column = 1, pady = 4)
btnShow = tk.Button(window, text = '購買明細', font = ft2,
    command = check)
btnShow.grid(row = 2, column = 2, pady = 4)

window.mainloop()

print("------------------------------------------------------------")  # 60個




window=tk.Tk()
window.geometry("500x500")
window.title('grid配置')
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)

label1=tk.Label(window, text = '北',font=('標楷體', 40))
label2=tk.Label(window, text = '東',font=('標楷體', 40),bg='yellow')
label3=tk.Label(window, text = '西',font=('標楷體', 40),bg='lightgreen')
label4=tk.Label(window, text = '中',font=('標楷體', 40),bg='pink')
label5=tk.Label(window, text = '南',font=('標楷體', 40),bg='lightblue')
label1.grid(row=0,column=0,columnspan=2,sticky='nswe')
label2.grid(row=0,column=2,rowspan=2,sticky='nswe')
label3.grid(row=1,column=0,rowspan=2,sticky='nswe')
label4.grid(row=1,column=1,sticky='nswe')
label5.grid(row=2,column=1,columnspan=2,sticky='nswe')

window.mainloop()

print("------------------------------------------------------------")  # 60個


window = Tk()
window.geometry("600x400")

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label6.grid(row=1,column=1)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,columnspan=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label6.grid(row=1,column=1)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,rowspan=2)
label3.grid(row=0,column=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,rowspan=2,columnspan=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=0,column=2,padx=5,pady=5)
label4.grid(row=0,column=3,padx=5,pady=5)
label5.grid(row=1,column=0,padx=5)
label6.grid(row=1,column=1,padx=5)
label7.grid(row=1,column=2,padx=5)
label8.grid(row=1,column=3,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",relief="raised")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國",relief="raised")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

label1 = Label(window,text="歡迎來到美國",relief="raised")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國",relief="raised")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()



print("------------------------------------------------------------")  # 60個

window = Tk()
window.geometry("600x400")

Colors = ["red","orange","yellow","green","blue","purple"]

r = 0                               # row編號
for color in Colors:
    Label(window,text=color,relief="groove",width=20).grid(row=r,column=0)
    Label(window,bg=color,relief="ridge",width=20).grid(row=r,column=1)
    r += 1

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

label1 = Label(window,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5)

label2 = Label(window,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(window,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

label1 = Label(window,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5,stick=W)

label2 = Label(window,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(window,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

label1 = Label(window,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5,stick=W+E)

label2 = Label(window,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(window,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

window.mainloop()


print('------------------------------------------------------------')	#60個


window = Tk()
window.geometry("600x400")

lab  = Label(window,text="",bg="yellow",width=20)
button7 = Button(window,text="7",width=3)
button8 = Button(window,text="8",width=3)
button9 = Button(window,text="9",width=3)
buttonM = Button(window,text="*",width=3)                # 乘法符號
button4 = Button(window,text="4",width=3)
button5 = Button(window,text="5",width=3)
button6 = Button(window,text="6",width=3)
buttonS = Button(window,text="-",width=3)                # 減法符號
button1 = Button(window,text="1",width=3)
button2 = Button(window,text="2",width=3)
button3 = Button(window,text="3",width=3)
buttonP = Button(window,text="+",width=3)                # 加法符號
button0 = Button(window,text="0",width=8)
buttonD = Button(window,text=".",width=3)                # 小數點符號
buttonE = Button(window,text="=",width=3)                # 等號符號

lab.grid(row=0,column=0,columnspan=4)
button7.grid(row=1,column=0,padx=5)
button8.grid(row=1,column=1,padx=5)
button9.grid(row=1,column=2,padx=5)
buttonM.grid(row=1,column=3,padx=5)                    # 乘法符號
button4.grid(row=2,column=0,padx=5)
button5.grid(row=2,column=1,padx=5)
button6.grid(row=2,column=2,padx=5)
buttonS.grid(row=2,column=3,padx=5)                    # 減法符號
button1.grid(row=3,column=0,padx=5)
button2.grid(row=3,column=1,padx=5)
button3.grid(row=3,column=2,padx=5)
buttonP.grid(row=3,column=3,padx=5)                    # 加法符號
button0.grid(row=4,column=0,padx=5,columnspan=2)
buttonD.grid(row=4,column=2,padx=5)                    # 小數點符號
buttonE.grid(row=4,column=3,padx=5)                    # 等號符號

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

nameL = Label(window,text="Name ")        # name標籤
nameL.grid(row=0)
addressL = Label(window,text="Address")   # address標籤
addressL.grid(row=1)

nameE = Entry(window)                     # 文字方塊name
addressE = Entry(window)                  # 文字方塊address
nameE.grid(row=0,column=1)              # 定位文字方塊name
addressE.grid(row=1,column=1)           # 定位文字方塊address

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

accountL = Label(window,text="Account")   # account標籤
accountL.grid(row=0)
pwdL = Label(window,text="Password")      # pwd標籤
pwdL.grid(row=1)

accountE = Entry(window)                  # 文字方塊account
pwdE = Entry(window,show="*")             # 文字方塊pwd
accountE.grid(row=0,column=1)           # 定位文字方塊account
pwdE.grid(row=1,column=1)               # 定位文字方塊pwd

window.mainloop()


print('------------------------------------------------------------')	#60個


window = Tk()
window.geometry("600x400")

var1 = IntVar()                      
cbtnNFL = Checkbutton(window,text="美式足球",variable=var1)
cbtnNFL.grid(row=1,sticky=W)

var2 = IntVar()
cbtnMLB = Checkbutton(window,text="棒球",variable=var2)
cbtnMLB.grid(row=2,sticky=W)

var3 = IntVar()
cbtnNBA = Checkbutton(window,text="籃球",variable=var3)
cbtnNBA.grid(row=3,sticky=W)   

window.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo1():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

window = Tk()
window.geometry("600x400")

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(window,text=sports[i], variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
button1 = Button(window,text="選取",width=10,command=printInfo1)
button1.grid(row=i+2)

window.mainloop()

print('------------------------------------------------------------')	#60個

# 以下是callback方法
def selAll():                               # 選取全部字串
    entry.select_range(0,END)
def deSel():                                # 取消選取
    entry.select_clear()
def clr():                                  # 刪除文字
    entry.delete(0,END)
def readonly():                             # 設定Entry狀態
    if var.get() == True:
        entry.config(state=DISABLED)        # 設為DISABLED
    else:
        entry.config(state=NORMAL)          # 設為NORMAL

window = Tk()
window.geometry("600x400")

# 以下row=0建立Entry
entry = Entry(window)
entry.grid(row=0,column=0,columnspan=4,
           padx=5,pady=5,sticky=W)
# 以下row=1建立Button
buttonSel = Button(window,text="選取",command=selAll)
buttonSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)
buttonDesel = Button(window,text="取消選取",command=deSel)
buttonDesel.grid(row=1,column=1,padx=5,pady=5,sticky=W)
buttonClr = Button(window,text="刪除",command=clr)
buttonClr.grid(row=1,column=2,padx=5,pady=5,sticky=W)
buttonQuit = Button(window,text="結束",command=window.destroy)
buttonQuit.grid(row=1,column=3,padx=5,pady=5,sticky=W)
# 以下row=2建立Checkboxes
var = BooleanVar()
var.set(False)
chkReadonly = Checkbutton(window,text="唯讀",variable=var,command=readonly)
chkReadonly.grid(row=2,column=0)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.geometry("600x400")

style = Style()                 # 改用Style
style.theme_use("alt")          # 改用alt支援Style

fm1 = Frame(window,width=150,height=80,relief="flat")
fm1.grid(row=0,column=0,padx=5,pady=5)

fm2 = Frame(window,width=150,height=80,relief="groove")
fm2.grid(row=0,column=1,padx=5,pady=5)

fm3 = Frame(window,width=150,height=80,relief="raised")
fm3.grid(row=0,column=2,padx=5,pady=5)

fm4 = Frame(window,width=150,height=80,relief="ridge")
fm4.grid(row=1,column=0,padx=5,pady=5)

fm5 = Frame(window,width=150,height=80,relief="solid")
fm5.grid(row=1,column=1,padx=5,pady=5)

fm6 = Frame(window,width=150,height=80,relief="sunken")
fm6.grid(row=1,column=2,padx=5,pady=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



