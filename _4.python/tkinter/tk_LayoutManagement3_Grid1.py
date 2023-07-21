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

