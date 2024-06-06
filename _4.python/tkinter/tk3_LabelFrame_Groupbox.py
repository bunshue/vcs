'''
LabelFrame 就是 Groupbox.py

'''

import tkinter as tk

# 建立主視窗
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
title = "Groupbox測試"
window.title(title)

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# GroupBox測試
tk.Label(text = 'GroupBox測試').pack()

#GroupBox之大小, 若小於內附控件大小, 則會撐大
w = 10
h = 10
group = tk.LabelFrame(window, text = "Group", padx = w, pady = h)

#GroupBox之位置, 相較於目前表單位置
x_st = 0
y_st = 0
group.pack(padx = x_st, pady = y_st)

#GroupBox內 放幾個控件
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


window.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo2():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

window = tk.Tk()
window.geometry("600x400")

# 以下建立標籤框架與和曲方塊
labFrame = tk.LabelFrame(window,text="選擇最喜歡的運動")
sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = tk.BooleanVar()            # 布林變數物件
    tk.Checkbutton(labFrame,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=tk.W)
labFrame.pack(ipadx=5,ipady=5,pady=10)      # 包裝定位標籤框架

button1 = tk.Button(window,text="確定",width=10,command=printInfo2)
button1.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


