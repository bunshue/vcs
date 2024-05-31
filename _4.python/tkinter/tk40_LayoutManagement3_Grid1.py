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
title = "這是主視窗"
window.title(title)

for j in range(0, 16):
    for i in range(0, 16):
        #print(i)
        label_n = tk.Label(window, text = str(i) + ',' + str(j))
        label_n.grid(row = j, column = i)

w = 15
h = 5

text1 = tk.Text(window, width = w, height = h)  #原始數據錄入框
text1.grid(row = 0, column = 0)
#text1.grid(row = 0, column = 0, rowspan = 1, columnspan = 3)

button0 = tk.Button(window, text = "55", width = w, height = h)
button0.grid(row = 2, column = 2)
#button0.grid(row = 2, column = 2, rowspan = 1, columnspan = 3)

'''
若不指名 rowspan / columnspan, 則所佔為1格
會依據控件的大小 將所在格撐大成設定的格數

'''

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

window.mainloop()


print("------------------------------------------------------------")  # 60個


'''
Grid 測試
'''
import tkinter as tk

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

#window.geometry('{}x{}'.format(460, 350))

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



'''
Grid 測試 Button + Canvas
'''
import tkinter as tk

# Display a rectangle
def displayRect():
    canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

# Display an oval
def displayOval():
    canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "oval")

# Display an arc
def displayArc():
    canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", tags = "arc")

# Display a polygon
def displayPolygon():
    canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")

# Display a line
def displayLine():
    canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line")
    canvas.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue", tags = "line")

# Display a string
def displayString():
    canvas.create_text(60, 40, text = "Hi, I am a string", font = "Times 10 bold underline", tags = "string")

# Clear drawings
def clearCanvas():
    canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

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
title = "Grid 測試 Button"
window.title(title)

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame1 = tk.Frame(window)
frame1.pack()

message = tk.Message(frame1, text = "這個訊息所佔的位置為3R2C")
message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
tk.Label(frame1, text = "姓 : ").grid(row = 1, column = 3)
tk.Entry(frame1).grid(row = 1, column = 4, padx = 5, pady = 5)
tk.Label(frame1, text = "名 : ").grid(row = 2, column = 3)
tk.Entry(frame1).grid(row = 2, column = 4)
tk.Button(frame1, text = "取得姓名").grid(row = 3, padx = 5, pady = 5, column = 4, sticky = tk.E)

canvas = tk.Canvas(window, width = 400, height = 400, bg = "white")
canvas.pack()

#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame2 = tk.Frame(window)
frame2.pack()

btRectangle = tk.Button(frame2, text = "Rectangle", command = displayRect)
btOval = tk.Button(frame2, text = "Oval", command = displayOval)
btArc = tk.Button(frame2, text = "Arc", command = displayArc)
btPolygon = tk.Button(frame2, text = "Polygon", command = displayPolygon)
btLine = tk.Button(frame2, text = "Line", command = displayLine)
btString = tk.Button(frame2, text = "String", command = displayString)
btClear = tk.Button(frame2, text = "Clear", command = clearCanvas)
btRectangle.grid(row = 1, column = 1)
btOval.grid(row = 1, column = 2)
btArc.grid(row = 1, column = 3)
btPolygon.grid(row = 1, column = 4)
btLine.grid(row = 1, column = 5)
btString.grid(row = 1, column = 6)
btClear.grid(row = 1, column = 7)



#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame3 = tk.Frame(window)
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

'''
frame3.columnconfigure(0, weight = 1)
frame3.columnconfigure(1, weight = 2)
#column 0 為基礎寬度，column 1 為column0的兩倍寬
'''
'''
frame3.columnconfigure((0, 2, 3), weight = 1)
frame3.columnconfigure(1, weight = 2)
frame3主視窗的，column 0 , 2, 3為基礎寬度，column 1 為其他column的兩倍寬
'''

button20 = tk.Button(frame3, text = "第2排第0個")
button20.grid(row = 2, column = 0, ipadx = 10, ipady = 10)
button21 = tk.Button(frame3, text = "第2排第1個")
button21.grid(row = 2, column = 1, ipadx = 10, ipady = 10)
button22 = tk.Button(frame3, text = "第2排第2個")
button22.grid(row = 2, column = 2, ipadx = 10, ipady = 10)

'''
參數Sticky填充元件大小
sticky 可以輸入N ,S, E, W或是 混搭例如:EW，NS，NSEW，代表靠N(北方) 、S(南方)、E(東方)、W(西方)，NS(北南延伸)，EW(東西延伸)，NSEW(全方位延伸)
'''

button30 = tk.Button(frame3, text = "第3排第0個")
button30.grid(row = 3, column = 0, ipadx = 10, ipady = 10, sticky = "EW")
button31 = tk.Button(frame3, text = "第3排第1個")
button31.grid(row = 3, column = 1, ipadx = 10, ipady = 10, sticky = "EW")
button32 = tk.Button(frame3, text = "第3排第2個")
button32.grid(row = 3, column = 2, ipadx = 10, ipady = 10, sticky = "EW")



#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame4 = tk.Frame(window)
frame4.pack()

width = 100
height = 100

canvas1 = tk.Canvas(frame4, width = width, height = height)
canvas1.create_line(10, 10, width - 10, height - 10)
canvas1.create_line(width - 10, 10, 10, height - 10)
canvas1.grid(row = 3, column = 1)

canvas2 = tk.Canvas(frame4, width = width, height = height)
canvas2.create_rectangle(10, 10, width - 10, height - 10)
canvas2.grid(row = 3, column = 2)

canvas3 = tk.Canvas(frame4, width = width, height = height)
canvas3.create_oval(10, 10, width - 10, height - 10)
canvas3.grid(row = 3, column = 3)

canvas4 = tk.Canvas(frame4, width = width, height = height)
canvas4.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145)
canvas4.grid(row = 3, column = 4)

canvas5 = tk.Canvas(frame4, width = width, height = height)
canvas5.create_rectangle(10, 10, width - 10, height - 10, fill = "red")
canvas5.grid(row = 3, column = 5)

canvas6 = tk.Canvas(frame4, width = width, height = height)
canvas6.create_oval(10, 10, width - 10, height - 10, fill = "red")
canvas6.grid(row = 3, column = 6)

canvas7 = tk.Canvas(frame4, width = width, height = height)
canvas7.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145, fill = "red")
canvas7.grid(row = 3, column = 7)

window.mainloop()


print("------------------------------------------------------------")  # 60個


"""
Grid 測試 grid
"""

import tkinter as tk

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
window.title("grid 測試")

frame = tk.Frame(window)
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



