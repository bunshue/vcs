def input_data():  
#    global labelcword, entrycword 
    HideAllFrame()
    frameInput.pack()    
    frameInputCheck.pack() 
    entryewordInput.focus()

def HideAllFrame(): 
    frameInput.pack_forget()
    frameInputCheck.pack_forget()
    frameSearch.pack_forget()
    frameSearchChech.pack_forget()
    frameEdit.pack_forget()
    frameEditCheck.pack_forget()
    frameDelete.pack_forget()
    frameDeleteCheck.pack_forget()    
        
def First():  # 首頁
    global page
    HideAllFrame()
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
    print('TBD')
        
def search_data():
#    global vareword, varcword
    HideAllFrame()
    frameSearch.pack()    
    frameSearchChech.pack()
    entryewordSearch.focus()
        
def edit_data():
    HideAllFrame()
    frameEdit.pack()
    frameEditCheck.pack() 
    labelewordedit.config(state="normal")
    entryewordedit.config(state="normal")
    buttonEditInput.config(state="normal")
    labelcwordedit.config(state="disabled")
    entrycwordedit.config(state="disabled")
    btnDoedit.pack_forget()
    entryewordedit.focus()

def DoEdit():
    global varewordedit, varcwordedit
    eword=varewordedit.get()
    cword=varcwordedit.get()
    key_id = CkeckKey(eword) 
    if cword != "":      # 判斷單字是否存在
        word={eword:cword}
        disp_data()
        varewordedit.set("")
        varcwordedit.set("")
        edit_data()
        msgedit.set("")
    return  

def DoKeyEdit():
    global varewordedit, varcwordedit
    eword=varewordedit.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        msgedit.set("")
        labelcwordedit.config(state="disabled")
        entryewordedit.config(state="disabled")
        labelcwordedit.config(state="normal")
        entrycwordedit.config(state="normal")
        buttonEditInput.config(state="normal")
        btnDoedit.pack()
    else:
        varcwordedit.set("")
        msgedit.set("{} 單字未建立!".format(eword))
    return

def keyEdit(event):
    eword=varewordedit.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        msgedit.set("")
        labelcwordedit.config(state="disabled")
        entryewordedit.config(state="disabled")
        labelcwordedit.config(state="normal")
        entrycwordedit.config(state="normal")
        buttonEditInput.config(state="normal")
        btnDoedit.pack()
    else:
        varcwordedit.set("")
        msgedit.set("{} 單字未建立!".format(eword))
    return
            
def keyDelete(event):
    global varewordDelete, varcwordDelete
    eword=varewordDelete.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        btnDoDelete.pack()
    else:
        msgDelete.set("{} 單字未建立!".format(eword))
    return 

def DoKeyDelete():
    global varewordDelete, varcwordDelete
    eword=varewordDelete.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        btnDoDelete.pack()
    else:
        msgDelete.set("{} 單字未建立!".format(eword))
    return          

def delete_data():
    HideAllFrame()
    frameDelete.pack()
    frameDeleteCheck.pack()
    labelewordDelete.config(state="normal")
    entryewordDelete.config(state="normal")
    buttonDeleteInput.config(state="normal")
    btnDoDelete.pack_forget()
    entryewordDelete.focus()

def DoDelete():
    global varewordDelete, varcwordDelete
    eword=varewordDelete.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 單字存在
        msgDelete.set("")
        disp_data()
        varewordDelete.set("")
        delete_data()
        msgDelete.set("")
    return  
            
def exit(): # 結束
    window.destroy()    

def DoInput(): 
    global varewordInput, varcwordInput
    eword=varewordInput.get()
    cword=varcwordInput.get()
    key_id = CkeckKey(eword)   
    if key_id != "":      # 判斷鍵是否存在
        print('aaaaaaa')
    elif eword=="":
        msginput.set("\n未輸入英文單字!")
    elif cword=="":
        msginput.set("\n未輸入中文翻譯!")
    else:
        word={eword:cword}
        disp_data()
        entryewordInput.focus()
        varewordInput.set("")
        varcwordInput.set("")
        msginput.set("")
    return
        
def DoSearch(): 
    eword=varewordSearch.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        print('aaaaa')
    else:
        msgSearch.set("\n{} 單字未建立!".format(eword))
    return  


# 導入套件
import tkinter as tk
import math
import operator

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

page,pagesize=0,10
datasize=10 #資料筆數
totpage=math.ceil(datasize/pagesize) #總頁數

labeltitle = tk.Label(window, text="\n", fg="red",font=("新細明體",12))
labeltitle.pack()

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

# 單字顯示區
frameShow = tk.Frame(window)  
frameShow.pack()
varwords = tk.StringVar()
labelwords = tk.Label(window, textvariable=varwords,fg="blue",font=("新細明體",10))
labelwords.pack() 

   
frameSepArea = tk.Frame(window)  # 空白列
frameSepArea.pack()
labelSep= tk.Label(frameSepArea, text="\n<<< 資料編輯 >>>\n",fg="brown",font=("新細明體",12))
labelSep.pack()  
   
frameCommand2 = tk.Frame(window)  # 按鈕容器
frameCommand2.pack()    
button1 = tk.Button(frameCommand2, text="查  詢", width=8,command=search_data)
button2 = tk.Button(frameCommand2, text="輸  入", width=8,command=input_data)
button3 = tk.Button(frameCommand2, text="修  改", width=8,command=edit_data)
button4 = tk.Button(frameCommand2, text="刪  除", width=8,command=delete_data)
button5 = tk.Button(frameCommand2, text="結  束", width=8,command=exit)
button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=0, column=3, padx=5, pady=5)
button4.grid(row=0, column=4, padx=5, pady=5)
button5.grid(row=0, column=5, padx=5, pady=5)
window.protocol("WM_DELETE_WINDOW", exit)

# 單字輸入區
msginput = tk.StringVar()
msginput.set("\n")
frameInput = tk.Frame(window)  
varewordInput = tk.StringVar()
labelewordInput = tk.Label(frameInput, text="請輸入英文單字",fg="blue",font=("新細明體",10))
entryewordInput=tk.Entry(frameInput,textvariable=varewordInput)
labelewordInput.grid(row=0, column=0, padx=5, pady=5)
entryewordInput.grid(row=0, column=1, padx=5, pady=5)
varcwordInput = tk.StringVar()
labelcwordInput = tk.Label(frameInput, text="請輸入中文翻譯",fg="blue",font=("新細明體",10))
entrycwordInput=tk.Entry(frameInput,textvariable=varcwordInput)
labelcwordInput.grid(row=1, column=0, padx=5, pady=5)
entrycwordInput.grid(row=1, column=1, padx=5, pady=5)

frameInputCheck = tk.Frame(window)  # 單字輸入確認區
btnDoInput = tk.Button(frameInputCheck, text="確定輸入", width=8,command=DoInput)
btnDoInput.pack()  
labelmsgInput = tk.Label(frameInputCheck, textvariable=msginput,fg="red",font=("新細明體",10))
labelmsgInput.pack()

# 單字查詢區
msgSearch = tk.StringVar()
msgSearch.set("\n")
frameSearch = tk.Frame(window)  
varewordSearch = tk.StringVar()
labelewordSearch = tk.Label(frameSearch, text="請輸入要查詢的英文單字",fg="blue",font=("新細明體",10))
entryewordSearch=tk.Entry(frameSearch,textvariable=varewordSearch)
labelewordSearch.grid(row=0, column=0, padx=5, pady=5)
entryewordSearch.grid(row=0, column=1, padx=5, pady=5)

frameSearchChech = tk.Frame(window)  # 查詢輸入確認區
btnDoSearch = tk.Button(frameSearchChech, text="確定", width=8,command=DoSearch)
btnDoSearch.pack()  
labelmsgSearch = tk.Label(frameSearchChech, textvariable=msgSearch,fg="red",font=("新細明體",10))
labelmsgSearch.pack()

# 單字修改區
msgedit = tk.StringVar()
msgedit.set("\n")
frameEdit = tk.Frame(window) 
varewordedit = tk.StringVar()
labelewordedit = tk.Label(frameEdit, text="請輸入要修改的英文單字(Enter 結束輸入)",fg="blue",font=("新細明體",10))
entryewordedit=tk.Entry(frameEdit,textvariable=varewordedit)
buttonEditInput = tk.Button(frameEdit, text="輸入完成", width=8,command=DoKeyEdit)
labelewordedit.grid(row=0, column=0, padx=5, pady=5)
entryewordedit.grid(row=0, column=1, padx=5, pady=5)
buttonEditInput.grid(row=0, column=2, padx=5, pady=5)
varcwordedit = tk.StringVar()
labelcwordedit = tk.Label(frameEdit, text="請輸入中文翻譯",fg="blue",font=("新細明體",10))
entrycwordedit=tk.Entry(frameEdit,textvariable=varcwordedit)
labelcwordedit.grid(row=1, column=0, padx=5, pady=5)
entrycwordedit.grid(row=1, column=1, padx=5, pady=5)

frameEditCheck = tk.Frame(window)  # 單字修改確認區
btnDoedit = tk.Button(frameEditCheck, text="確定修改", width=8,command=DoEdit)
btnDoedit.pack()  
labelmsgedit = tk.Label(frameEditCheck, textvariable=msgedit,fg="red",font=("新細明體",10))
labelmsgedit.pack()
entryewordedit.bind('<Return>', keyEdit) # 按 Enter鍵的處理

# 單字刪除區
msgDelete = tk.StringVar()
msgDelete.set("\n")
frameDelete= tk.Frame(window)  
varewordDelete = tk.StringVar()
labelewordDelete = tk.Label(frameDelete, text="請輸入要刪除的英文單字(Enter 結束輸入)",fg="blue",font=("新細明體",10))
entryewordDelete=tk.Entry(frameDelete,textvariable=varewordDelete)
buttonDeleteInput = tk.Button(frameDelete, text="輸入完成", width=8,command=DoKeyDelete)
labelewordDelete.grid(row=0, column=0, padx=5, pady=5)
entryewordDelete.grid(row=0, column=1, padx=5, pady=5)
buttonDeleteInput.grid(row=0, column=2, padx=5, pady=5)
frameDeleteCheck = tk.Frame(window)  # 刪除確認區
btnDoDelete = tk.Button(frameDeleteCheck, text="確定刪除", width=8,command=DoDelete)
btnDoDelete.pack()  
labelmsgDelete = tk.Label(frameDeleteCheck, textvariable=msgDelete,fg="red",font=("新細明體",10))
labelmsgDelete.pack()
entryewordDelete.bind('<Return>', keyDelete) # 按 Enter鍵的處理

First()
window.mainloop()
