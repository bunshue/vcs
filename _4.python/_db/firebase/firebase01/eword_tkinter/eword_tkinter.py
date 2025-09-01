def CkeckKey(no):
    key_id=""
    if datas != None:
        for key,value in datas.items():
            if no==key: # 讀取鍵名稱
                key_id = key
                break  
    return key_id   
    
def input_data():  
#    global datas,labelcword, entrycword 
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
        
def First(): 
    global page
    HideAllFrame()
    page=0
    disp_data()
 
def Prev():  
    global page
    if page>0:
        page -=1
        disp_data()     
       
def Next(): 
    global page
    if page<pagesize:
        page +=1
        disp_data()
    
def Bottom():
    global page
    page=pagesize    
    disp_data() 

def disp_data():
    datas=fb.get(url, None)
    if datas != None:
        dc_sort = sorted(datas.items(),key = operator.itemgetter(0))              
        sep1=tk.Label(frameShow, text="\t\t",fg="white",width="20",font=("新細明體",10))       
        label1 = tk.Label(frameShow, text="單字",padx=20,fg="white",bg="black",width=20,font=("新細明體",10))
        label2 = tk.Label(frameShow, text="中文翻譯",fg="white",bg="black",width=50,font=("新細明體",10))
        sep1.grid(row=0,column=0,sticky="w")  # 加第一列空白，讓版面美觀些   
        label1.grid(row=1,column=0,sticky="w")
        label2.grid(row=1,column=1,sticky="w")
        
        n=0   # 資料從索引 0 開始
        row=2 # 資料從第二列開始
        start=page * pagesize + row
        for item in dc_sort:
            # 顯示目前 page頁的資料
            if n >= start and n < start + pagesize:
                key=item[0]    
                label1 = tk.Label(frameShow, text="\t\t"+item[0]+"\t\t",fg="blue",width=20,font=("新細明體",10))
                label2 = tk.Label(frameShow, text=item[1][key],fg="blue",width=50,font=("新細明體",10))
                label1.grid(row=row,column=0,sticky="w")
                label2.grid(row=row,column=1,sticky="w")
                row+=1
            n+=1
        
def search_data():
#    global datas,vareword, varcword
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
    global datas,varewordedit, varcwordedit
    eword=varewordedit.get()
    cword=varcwordedit.get()
    key_id = CkeckKey(eword) 
    if cword != "":      # 判斷單字是否存在
        word={eword:cword}
        datas[key_id]=word 
        fb.put(url + '/', data=word, name=key_id)
        disp_data()
        varewordedit.set("")
        varcwordedit.set("")
        edit_data()
        msgedit.set("")
    return  

def DoKeyEdit():
    global datas,varewordedit, varcwordedit
    eword=varewordedit.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        varcwordedit.set(datas[key_id][key_id])
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
        varcwordedit.set(datas[key_id][key_id])
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
    global datas,varewordDelete, varcwordDelete
    eword=varewordDelete.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        msgDelete.set("原來中文翻譯：{}".format(datas[key_id][key_id]))
        btnDoDelete.pack()
    else:
        msgDelete.set("{} 單字未建立!".format(eword))
    return 

def DoKeyDelete():
    global datas,varewordDelete, varcwordDelete
    eword=varewordDelete.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 判斷單字是否存在
        msgDelete.set("原來中文翻譯：{}".format(datas[key_id][key_id]))
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
    global datas,varewordDelete, varcwordDelete
    eword=varewordDelete.get()
    key_id = CkeckKey(eword) 
    if key_id != "":      # 單字存在
        fb.delete(url + '/' + key_id,None)
        datas.pop(key_id)
        msgDelete.set("")
        disp_data()
        varewordDelete.set("")
        delete_data()
        msgDelete.set("")
    return  
            
def exit(): # 結束
    win.destroy()    

def DoInput(): 
    global datas,varewordInput, varcwordInput
    eword=varewordInput.get()
    cword=varcwordInput.get()
    key_id = CkeckKey(eword)   
    if key_id != "":      # 判斷鍵是否存在
        msginput.set("\n{} 單字已存在!".format(datas.get(key_id)))
    elif eword=="":
        msginput.set("\n未輸入英文單字!")
    elif cword=="":
        msginput.set("\n未輸入中文翻譯!")
    else:
        word={eword:cword}
        fb.put(url, data=word,name=eword)
        if datas == None: datas = dict()
        datas[eword]=word
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
        msgSearch.set("\n中文翻譯：{} ".format(datas[key_id][key_id]))
    else:
        msgSearch.set("\n{} 單字未建立!".format(eword))
    return  

### 主程式從這裡開始 ###    

import tkinter as tk
from firebase import firebase
import operator,math

url = 'https://chiouapp01-a6172.firebaseio.com/English_tkinter'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get(url, None)

win=tk.Tk()
win.geometry("800x600")
win.title("英文單字王")

page,pagesize=0,10
datasize=len(datas) #資料筆數
totpage=math.ceil(datasize/pagesize) #總頁數

labeltitle = tk.Label(win, text="\n", fg="red",font=("新細明體",12))
labeltitle.pack()

frameCommand = tk.Frame(win)  # 翻頁按鈕容器
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
frameShow = tk.Frame(win)  
frameShow.pack()
varwords = tk.StringVar()
labelwords = tk.Label(win, textvariable=varwords,fg="blue",font=("新細明體",10))
labelwords.pack() 

   
frameSepArea = tk.Frame(win)  # 空白列
frameSepArea.pack()
labelSep= tk.Label(frameSepArea, text="\n<<< 資料編輯 >>>\n",fg="brown",font=("新細明體",12))
labelSep.pack()  
   
frameCommand2 = tk.Frame(win)  # 按鈕容器
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
win.protocol("WM_DELETE_WINDOW", exit)

# 單字輸入區
msginput = tk.StringVar()
msginput.set("\n")
frameInput = tk.Frame(win)  
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

frameInputCheck = tk.Frame(win)  # 單字輸入確認區
btnDoInput = tk.Button(frameInputCheck, text="確定輸入", width=8,command=DoInput)
btnDoInput.pack()  
labelmsgInput = tk.Label(frameInputCheck, textvariable=msginput,fg="red",font=("新細明體",10))
labelmsgInput.pack()

# 單字查詢區
msgSearch = tk.StringVar()
msgSearch.set("\n")
frameSearch = tk.Frame(win)  
varewordSearch = tk.StringVar()
labelewordSearch = tk.Label(frameSearch, text="請輸入要查詢的英文單字",fg="blue",font=("新細明體",10))
entryewordSearch=tk.Entry(frameSearch,textvariable=varewordSearch)
labelewordSearch.grid(row=0, column=0, padx=5, pady=5)
entryewordSearch.grid(row=0, column=1, padx=5, pady=5)

frameSearchChech = tk.Frame(win)  # 查詢輸入確認區
btnDoSearch = tk.Button(frameSearchChech, text="確定", width=8,command=DoSearch)
btnDoSearch.pack()  
labelmsgSearch = tk.Label(frameSearchChech, textvariable=msgSearch,fg="red",font=("新細明體",10))
labelmsgSearch.pack()

# 單字修改區
msgedit = tk.StringVar()
msgedit.set("\n")
frameEdit = tk.Frame(win) 
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

frameEditCheck = tk.Frame(win)  # 單字修改確認區
btnDoedit = tk.Button(frameEditCheck, text="確定修改", width=8,command=DoEdit)
btnDoedit.pack()  
labelmsgedit = tk.Label(frameEditCheck, textvariable=msgedit,fg="red",font=("新細明體",10))
labelmsgedit.pack()
entryewordedit.bind('<Return>', keyEdit) # 按 Enter鍵的處理

# 單字刪除區
msgDelete = tk.StringVar()
msgDelete.set("\n")
frameDelete= tk.Frame(win)  
varewordDelete = tk.StringVar()
labelewordDelete = tk.Label(frameDelete, text="請輸入要刪除的英文單字(Enter 結束輸入)",fg="blue",font=("新細明體",10))
entryewordDelete=tk.Entry(frameDelete,textvariable=varewordDelete)
buttonDeleteInput = tk.Button(frameDelete, text="輸入完成", width=8,command=DoKeyDelete)
labelewordDelete.grid(row=0, column=0, padx=5, pady=5)
entryewordDelete.grid(row=0, column=1, padx=5, pady=5)
buttonDeleteInput.grid(row=0, column=2, padx=5, pady=5)
frameDeleteCheck = tk.Frame(win)  # 刪除確認區
btnDoDelete = tk.Button(frameDeleteCheck, text="確定刪除", width=8,command=DoDelete)
btnDoDelete.pack()  
labelmsgDelete = tk.Label(frameDeleteCheck, textvariable=msgDelete,fg="red",font=("新細明體",10))
labelmsgDelete.pack()
entryewordDelete.bind('<Return>', keyDelete) # 按 Enter鍵的處理

First()
win.mainloop()