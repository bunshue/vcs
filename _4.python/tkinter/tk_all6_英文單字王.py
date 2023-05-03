def First():  # 首頁
    global page
    page=0
    disp_data()
 
def Prev():  #上一頁
    global page
    if page>0:
        page -=1
        disp_data()     
       
def Next(): #下一頁
    global page
    if page<pagesize:
        page +=1
        disp_data()
    
def Bottom(): #最後頁
    global page
    page=pagesize    
    disp_data() 

def disp_data():
    if datas != None:          
        sep1=tk.Label(frameShow, text="\t",fg="white",width="20",font=("新細明體",10))       
        label1 = tk.Label(frameShow, text="單字".ljust(30),fg="white",bg="black",width=30,font=("新細明體",10))
        label2 = tk.Label(frameShow, text="中文翻譯".ljust(175),fg="white",bg="black",width=80,font=("新細明體",10))
        sep1.grid(row=0,column=0,sticky="w")  # 加第一列空白，讓版面美觀些   
        label1.grid(row=1,column=0,sticky="w")
        label2.grid(row=1,column=1,sticky="w")
        
        n=0   # 資料從索引 0 開始
        row=2 # 資料從第二列開始
        start=page * pagesize + row
        for eword,cword in datas.items():
            # 顯示目前 page頁的資料
            if n >= start and n < start + pagesize: 
                label1 = tk.Label(frameShow, text="\t"+'{0:30}'.format(eword),fg="blue",font=("新細明體",10))
                label2 = tk.Label(frameShow, text='{0:30}'.format(cword),fg="blue",font=("新細明體",10))
                label1.grid(row=row,column=0,sticky="w")
                label2.grid(row=row,column=1,sticky="w")
                row+=1
            n+=1



# 導入套件
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
title = "英文單字王"
window.title(title)

import math

page,pagesize=0,10
datas=dict()

filename = 'C:/______test_files2/eword.txt'
with open(filename,'r', encoding = 'UTF-8-sig') as f:
    for line in f:
        eword,cword = line.rstrip('\n').split(',')
        datas[eword]=cword
print("轉換完畢!") 

datasize=len(datas) #資料筆數
totpage=math.ceil(datasize/pagesize) #總頁數

# 單字顯示區
frameShow = tk.Frame(window)  
frameShow.pack()
labelwords = tk.Label(window, text="")
labelwords.pack() 

frameCommand = tk.Frame(window)  # 翻頁按鈕容器
frameCommand.pack()  
btnFirst = tk.Button(frameCommand, text="第一頁", width=8,command=First)
btnPrev = tk.Button(frameCommand, text="上一頁", width=8,command=Prev)
btnNext = tk.Button(frameCommand, text="下一頁", width=8,command=Next)
btnBottom = tk.Button(frameCommand, text="最末頁", width=8,command=Bottom)
btnFirst.grid(row=0, column=0, padx=5, pady=5)
btnPrev.grid(row=0, column=1, padx=5, pady=5)
btnNext.grid(row=0, column=2, padx=5, pady=5)        
btnBottom.grid(row=0, column=3, padx=5, pady=5)   

First()

window.mainloop()
