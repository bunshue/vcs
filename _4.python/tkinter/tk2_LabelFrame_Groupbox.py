"""
LabelFrame 就是 Groupbox

"""

import tkinter as tk

print('------------------------------------------------------------')	#60個

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print('------------------------------------------------------------')	#60個

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
print('------------------------------------------------------------')	#60個

def printInfo2():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)


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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print('------------------------------------------------------------')	#60個


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print('------------------------------------------------------------')	#60個


window.mainloop()

print('------------------------------------------------------------')	#60個


window = tk.Tk()
window.geometry("600x800")
window.title('LabelFrame 2')


def fnRed():
    frame1.config(bg='red')

def fnGreen():
    frame1.config(bg='green')  

def fnBlue():
    frame1.config(bg='blue')
    
print('顏色切換')

frame1=tk.Frame(window,width=200,height=100,relief='raised',borderwidth=3,bg='white')
frame1.pack(pady=5)

#建立1個 LabelFrame 在 window 下
labelFrame1=tk.LabelFrame(window,text='顏色')
labelFrame1.pack(pady=20,fill='x')

#建立3個 button 在 LabelFrame 下
button1=tk.Button(labelFrame1,text='紅色',width=8,command=fnRed).pack(side='left',padx=5)
button2=tk.Button(labelFrame1,text='綠色',width=8,command=fnGreen).pack(side='left',padx=5)
button3=tk.Button(labelFrame1,text='藍色',width=8,command=fnBlue).pack(side='left',padx=5)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個






window.mainloop()


print('------------------------------------------------------------')	#60個


window = tk.Tk()
window.title('LabelFrame')
window.geometry('400x400')

labelFrame1=tk.LabelFrame(window,text='設定：',relief='raised',borderwidth=2)
labelFrame1.pack(pady=5)

tk.Label(labelFrame1,text='編碼器：').grid(row=0,column=0,pady=3)

spinboxFourcc=tk.Spinbox(labelFrame1,value=('XVID','DIVX','MJPG','I420'),width=10)
spinboxFourcc.grid(row=0,column=1,pady=3,sticky='w')

tk.Label(labelFrame1,text='檔名：').grid(row=2,column=0,pady=3)

entry1 = tk.Entry(labelFrame1, width=20)
entry1.grid(row=2,column=1,pady=3,sticky='w')

tk.Label(labelFrame1,text='AAAAA').grid(row=3,column=0,columnspan=2)

button1=tk.Button(labelFrame1, text='BBBBB')
button1.grid(row=4,column=0,columnspan=1)

button2=tk.Button(labelFrame1, text='CCCCC')
button2.grid(row=4,column=1,columnspan=1)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.title('LabelFrame')
window.geometry('400x400')

def fnCal():
    r = userR.get()
    u=unid.get()
    if (kind.get() == '圓周長'):  		#若選取圓周長
        a=3.14*2*r
        print('圓周長為 {:.2f} {}'.format(a,u))
    else:
        a=3.14*r*r
        print('圓面積為 {:.2f} 平方{}'.format(a,u))
  
print('圓形計算')

lfrmR=tk.LabelFrame(window,text='輸入半徑：')
lfrmR.pack(pady=10)
userR=tk.IntVar()
userR.set(10)
entR= tk.Entry(lfrmR,textvariable=userR).pack(pady=3)
labelMsg=tk.Label(lfrmR, text = '請輸入半徑(整數)然後選擇項目').pack(pady=10)

lfrmKind=tk.LabelFrame(window,text='計算類別')
lfrmKind.pack(side='left',pady=10,padx=10,fill='x',expand=1)
kinds=['圓周長','圓面積']
kind=tk.StringVar()
for k in kinds:
    tk.Radiobutton(lfrmKind,text=k,variable=kind,value=k,command=fnCal).pack(pady=3)
kind.set('圓周長')

lfrmUnid=tk.LabelFrame(window,text='單位')
lfrmUnid.pack(side='left',pady=10,padx=10,fill='x',expand=1)
unids=['公分','英吋']
unid=tk.StringVar()
for u in unids:
    tk.Radiobutton(lfrmUnid,text=u,variable=unid,value=u,command=fnCal).pack(pady=3)
unid.set(unids[0])

window.mainloop()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



