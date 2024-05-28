
print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\grid.py

import tkinter as tk
win=tk.Tk()
win.geometry('200x200')
win.title('grid配置')
win.rowconfigure(0,weight=1)
win.rowconfigure(1,weight=1)
win.rowconfigure(2,weight=1)
win.columnconfigure(0,weight=1)
win.columnconfigure(1,weight=1)
win.columnconfigure(2,weight=1)
lbl1=tk.Label(win, text = '北',font=('標楷體', 40))
lbl2=tk.Label(win, text = '東',font=('標楷體', 40),bg='yellow')
lbl3=tk.Label(win, text = '西',font=('標楷體', 40),bg='lightgreen')
lbl4=tk.Label(win, text = '中',font=('標楷體', 40),bg='pink')
lbl5=tk.Label(win, text = '南',font=('標楷體', 40),bg='lightblue')
lbl1.grid(row=0,column=0,columnspan=2,sticky='nswe')
lbl2.grid(row=0,column=2,rowspan=2,sticky='nswe')
lbl3.grid(row=1,column=0,rowspan=2,sticky='nswe')
lbl4.grid(row=1,column=1,sticky='nswe')
lbl5.grid(row=2,column=1,columnspan=2,sticky='nswe')
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\label.py

import tkinter as tk
win=tk.Tk()
win.geometry('300x200')
win.title('Label標籤')
win.configure(bg='white') 
tk.Label(win, text = 'Label標籤', fg='blue',bg='lightblue',bitmap='gray25',\
         compound='left',font=('標楷體', 24, 'bold')).pack()
msg=('使用Label標籤元件可在視窗上提供各種文字訊息，例如顯示程式執行'
     '過程的提示訊息，或是程式的執行結果。Label元件只能顯示文字資料，'
     '無法接受使用者輸入資料。')
tk.Label(win, text = msg, width=28,wraplength=240,justify='left',\
         pady=10,font=('細明體', 14)).pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\pack.py

import tkinter as tk
win=tk.Tk()
win.geometry('300x200')
win.title('pack配置')
win.configure(bg='white')
lbl1=tk.Label(win, text = '元件版面配置',font=('微軟正黑體', 16),fg='white',bg='blue')
lbl2=tk.Label(win, text = '方法',font=('標楷體', 12))
lbl3=tk.Label(win, text = 'pack()方法',font=('標楷體', 12),bg='lightgreen')
lbl4=tk.Label(win, text = 'grid()方法',font=('標楷體', 12),bg='pink')
lbl5=tk.Label(win, text = 'place()方法',font=('標楷體', 12),bg='lightblue')
lbl1.pack(fill='x')
lbl2.pack(side='left', fill='y')
lbl3.pack(pady=5, fill='both', expand=True)
lbl4.pack(pady=5, fill='both', expand=True)
lbl5.pack(pady=5, fill='both', expand=True)
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch07\place.py

import tkinter as tk
win=tk.Tk()
win.geometry('300x200')
win.configure(bg='white') 
win.title('place配置')
lbl1=tk.Label(win, text = "五色鳥 Muller's Barbet", font=('微軟正黑體', 18),\
              fg='white',bg='black')
lbl2=tk.Label(win, text = '啄木鳥目', font=('標楷體', 16),fg='blue',bg='lightblue')
lbl3=tk.Label(win, text = '五色鳥科', font=('標楷體', 14),fg='green',bg='lightgreen')
msg='分布海平面到2800公尺，全身為鮮艷的翠綠色，在闊葉林中有良好的保護色。'
lbl4=tk.Label(win, text = msg,font=('細明體', 12),wraplength=170)
lbl1.place(x=10,y=5,width=280,height=40)
lbl2.place(x=10,y=50,width=90,height=50)
lbl3.place(x=10,y=105,width=90,height=50)
lbl4.place(x=110,y=50,width=180,height=105)
win.mainloop()


print("------------------------------------------------------------")  # 60個



import tkinter as tk
win=tk.Tk()
win.geometry('300x200+80+50')
win.title('我的第一個視窗應用程式')
win.resizable(True, False)
win.iconbitmap('first.ico')
win.maxsize(500,200)
win.minsize(100,200)
win.configure(bg='yellow')
win.mainloop()



print("------------------------------------------------------------")  # 60個

#calculator.py

import tkinter as tk
def fnKey(str):
    global exp		#宣告exp為全域變數
    exp+=str        #運算式為原運算式加新輸入的字串
    lblExp.config(text=exp)  #重設lblExp的文字為新運算式

def fnCls():
    global exp
    exp=''	#運算式設為空字串
    lblExp.config(text=exp)
    
def fnCal():
    global exp
    exp=str(eval(exp))	#用eval方法計算運算式並轉型為字串
    lblExp.config(text=exp)    

win = tk.Tk()
win.title('簡易計算機')
win.geometry('180x140')
lblExp=tk.Label(win,text='',width=18,relief='raised',bg='yellow')
lblExp.grid(row=0,column=0,columnspan=4)
tk.Button(win,text='7',width=3,command=lambda:fnKey('7')).grid(row=1,column=0)
tk.Button(win,text='8',width=3,command=lambda:fnKey('8')).grid(row=1,column=1)
tk.Button(win,text='9',width=3,command=lambda:fnKey('9')).grid(row=1,column=2)
tk.Button(win,text='/',width=3,command=lambda:fnKey('/')).grid(row=1,column=3)
tk.Button(win,text='4',width=3,command=lambda:fnKey('4')).grid(row=2,column=0)
tk.Button(win,text='5',width=3,command=lambda:fnKey('5')).grid(row=2,column=1)
tk.Button(win,text='6',width=3,command=lambda:fnKey('6')).grid(row=2,column=2)
tk.Button(win,text='*',width=3,command=lambda:fnKey('*')).grid(row=2,column=3)
tk.Button(win,text='1',width=3,command=lambda:fnKey('1')).grid(row=3,column=0)
tk.Button(win,text='2',width=3,command=lambda:fnKey('2')).grid(row=3,column=1)
tk.Button(win,text='3',width=3,command=lambda:fnKey('3')).grid(row=3,column=2)
tk.Button(win,text='-',width=3,command=lambda:fnKey('-')).grid(row=3,column=3)
tk.Button(win,text='0',width=3,command=lambda:fnKey('0')).grid(row=4,column=0)
tk.Button(win,text='C',width=3,command=fnCls).grid(row=4,column=1)
tk.Button(win,text="=",width=3,command=fnCal).grid(row=4,column=2)
tk.Button(win,text="+",width=3,command=lambda:fnKey('+')).grid(row=4,column=3)
exp=''   #預設運算式為空字串
win.mainloop()


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch09\drag.py

import tkinter as tk

def fnEnter(event):
    lblTest['bg']='lightblue'

def fnLeave(event):
    lblTest.config(text='試試看',bg='gray')
    
def fnMotion(event):
    lblTest['text']='游標移動'

def fnClick(event):
    global mx,my	#宣告mx,my為全域變數
    mx=event.x	#紀錄按下時滑鼠游標的x坐標
    my=event.y	#紀錄按下時滑鼠游標的y坐標
    
def fnB1Motion(event):
    global mx,my	#宣告mx,my為全域變數
    lblX=lblTest.winfo_rootx()-win.winfo_rootx()	#計算lblTest在視窗的x坐標
    lblY=lblTest.winfo_rooty()-win.winfo_rooty()	#計算lblTest在視窗的y坐標
    lblTest['text']='拖曳中...'
    lblTest.place(x=lblX+(event.x-mx),y=lblY+(event.y-my))	#重設lblTest位置
    
win = tk.Tk()
win.title('滑鼠事件測試')
win.geometry('240x240')
mx=0
my=0
lblTest=tk.Label(win,text='試試看',width=8,height=2,relief='groove',bg='gray')
lblTest.place(x=80,y=100)
lblTest.bind('<Enter>',fnEnter) #<Enter>事件綁定fnEnter事件處理函式
lblTest.bind('<Leave>',fnLeave) #<Leave>事件綁定fnLeave事件處理函式
lblTest.bind('<Motion>',fnMotion) #<Motion>事件綁定fnMotion事件處理函式
lblTest.bind('<Button-1>',fnClick) #<Button-1>事件綁定fnClick事件處理函式
lblTest.bind('<B1-Motion>',fnB1Motion) #<B1-Motion>事件綁定fnB1Motion事件處理函式
win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch09\login.py

import tkinter as tk

def fnID(e):
    code=e.keycode		#取得字元的鍵盤碼
    if(code==8 or code==46):	#若是退位或刪除鍵就離開函式
        return
    if(e.keysym=='Return'): 	#若是 Enter 鍵
        entPW.focus_set()		#設entPW成為作用元件
        return  
    id=userID.get()			#取得帳號字串
    if(e.char.islower()==False):   #若輸入字元不是小寫字元
        userID.set(id.replace(e.char,''))  #重設帳號字串將輸入字元以空字串取代
        tk.messagebox.showerror('注意','請輸入小寫字母！')

def fnPW(e):
    sym=e.keysym		#取得字元的按鍵名稱
    if(sym=='BackSpace' or sym=='Delete'): 	#若是退位或刪除鍵就離開函式
        return
    pw=userPW.get()
    if(e.char.isdigit()==False):	#若輸入字元不是數字
        userPW.set(pw.replace(e.char,''))  #重設密碼字串將輸入字元以空字串取代
        tk.messagebox.showerror('注意','請輸入數字！')

def fnCheck():
    id=userID.get()
    pw=userPW.get()
    if (id == 'love' and pw == '1314'):#若帳號和密碼字串都正確
        tk.messagebox.showinfo('歡迎','帳號和密碼正確！')
        win.destroy()
    else:
        tk.messagebox.showerror('注意','帳號或是密碼不正確！')
        userID.set('')	#清空帳號字串
        userPW.set('')	#清空密碼字串
        entID.focus_set()	#設entID成為作用元件
    
win = tk.Tk()
win.title('登入')
win.geometry('220x180')
tk.Label(win, text = '請輸入帳號：(小寫字母)').pack(anchor='w',pady=5)
userID=tk.StringVar()
entID= tk.Entry(win,textvariable=userID)
entID.pack(pady=5)
entID.bind('<KeyRelease>',fnID)	# KeyRelease事件綁定fnID事件處理函式
entID.focus_set()
tk.Label(win, text = '請輸入密碼：(數字)').pack(anchor='w',pady=5)
userPW=tk.StringVar()
entPW= tk.Entry(win,textvariable=userPW)
entPW.pack(pady=5)
entPW.bind('<KeyRelease>',fnPW) 	# KeyRelease事件綁定fnPW事件處理函式
btnLogin = tk.Button(win, text='登入', command=fnCheck).pack(pady=15)
win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch09\night_market.py

import tkinter as tk

def fnArea(e):
    global iArea,iNM		#宣告iArea,iNM為全域變數
    i=lstArea.curselection()    #取得地區選項索引的元組
    iArea=i[0]  #設iArea值為第一個元組值
    lstNM.delete(0,'end')   #清除所有夜市項目
    for x in range(len(nm[iArea])): #依序加入對應地區的夜市到清單
        lstNM.insert('end',nm[iArea][x])

def fnNM(e):
    global iArea,iNM		#宣告iArea,iNM為全域變數
    i=lstNM.curselection()    #取得夜市選項索引的元組
    iNM=i[0]  #設iNM值為第一個元組值
    lblMsg.config(text=msg[iArea][iNM]) #重設標籤的文字內容
    
win = tk.Tk()
win.title('台灣夜市簡介')
win.geometry('300x180')
tk.Label(win,text='台灣夜市之旅',font=('微軟正黑體',16)).pack()
lfrmNM=tk.LabelFrame(win,text='夜市名稱',relief='raised',borderwidth=2)
lfrmNM.pack(side='left',anchor='n',padx=5,pady=3)
areas=['北台灣','中台灣','南台灣','東台灣'] #宣告地區串列
lstArea=tk.Listbox(lfrmNM,height=4)
for a in areas: #將地區串列值依序插入清單中
    lstArea.insert('end',a)
lstArea.pack()
iArea=0 #預設地區選項的索引值為0
lstArea.bind('<<ListboxSelect>>',fnArea)    #選項改變的事件綁定fnArea函式
nm =[['基隆廟口','士林夜市','華西街夜市'],['逢甲夜市','一中街夜市'],
     ['文化路夜市','花園夜市','六合夜市'],['羅東夜市','東大門夜市']]
lstNM=tk.Listbox(lfrmNM,height=3)
lstNM.pack()
for x in range(len(nm[0])): #將北台灣的夜市串列值依序插入清單中
    lstNM.insert('end',nm[0][x])
lstNM.selection_set(0)  #預設選取第一個夜市
iNM=0 #預設夜市選項的索引值為0
lstNM.bind('<<ListboxSelect>>',fnNM)    #選項改變的事件綁定fnNM函式
lfrmMsg=tk.LabelFrame(win,text='夜市簡介',relief='raised',borderwidth=2)
lfrmMsg.pack(side='left',anchor='n',padx=5,pady=3)
msg=[['基隆夜市的廟口小吃遠近馳名\n\n營業時間：17:00-03:00',
      '集合大江南北小吃觀光客必到夜市\n\n營業時間：11:00-02:00',
      '最著名的夜市吸引國內外觀光客\n\n營業時間：16:00-24:00'],
     ['「價位便宜，應有盡有」是特色\n\n營業時間：12:00-02:00',
      '小吃攤、飲食店、流行服飾店林立\n\n營業時間：11:00–22:10'],
     ['文化路夜市聚集千家以上的攤販\n\n營業時間：17:00-06:00',
      '花園夜市規模大，交通便利\n\n營業時間：18:00-24:00(四、六、日)',
      '各地特產、小吃等一應俱全\n\n營業時間：17:00-02:00'],
     ['羅東夜市有豐富的當地小吃\n\n營業時間：17:00-01:00',
      '占地遼闊吃喝玩樂逛不完\n\n營業時間:18:00-00:00']]
lblMsg=tk.Label(lfrmMsg,text=msg[0][0],font=(12),wraplength=120,justify='left')
lblMsg.pack(anchor='n')
win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch09\order.py

import tkinter as tk

def fnOK():
    global order,total		#宣告order,tota為全域變數
    f=selFood.get()  #取得使用者選擇的菜單
    n=selNum.get()   #取得使用者選擇的數量
    i=foods.index(f) #取得菜單在foods串列的索引值
    m=money[i]*n     #計算本次點餐的小計
    total+=m         #計算點餐的總計
    order+='{} {} 碗 {}元\n'.format(foods[i],n,m) #加入本次點餐的資訊
    lblOrder.config(text='{}總計： {} 元'.format(order,total))
    
win = tk.Tk()
win.title('台中肉圓點餐系統')
win.geometry('300x160')
foods = ['肉圓','冬粉湯','魚丸湯']  #菜單項目串列
money=[40,30,30]                  #單價串列
selFood = tk.StringVar()
selFood.set('肉圓')
opnFood=tk.OptionMenu(win, selFood, *foods)
opnFood.config(width=10,font=('微軟正黑體',14))
opnFood.grid(row=0,column=0,pady=5)
selNum = tk.IntVar()
selNum.set(1)
opnNum=tk.OptionMenu(win, selNum, 1,2,3,4,5)
opnNum.config(width=8,font=('微軟正黑體',14))
opnNum.grid(row=0,column=1)
lblOrder=tk.Label(win,text='')
lblOrder.grid(row=1,column=0,columnspan=2,sticky='w')
btnOK=tk.Button(win, text='確定', command=fnOK)
btnOK.grid(row=1,column=1,sticky='n')
order=''    #點餐的文字訊息
total=0     #點餐的總計
win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch09\palette.py

import tkinter as tk

def fnBg(e):
    red=r.get()	#用get()方法讀取刻度值
    green=g.get()
    blue=b.get()
    color='#{:02x}{:02x}{:02x}'.format(red,green,blue)
    frmColor.config(bg=color)
    
win = tk.Tk()
win.title('調色盤')
win.geometry('250x200')
frmColor=tk.Frame(win,width=100,height=180,relief='raised',borderwidth=3,bg='white')
frmColor.pack(side='left',padx=10)
frmRGB=tk.Frame(win,width=200,height=200)
frmRGB.pack(side='left')
r=tk.IntVar()
sclR=tk.Scale(frmRGB,label='紅：',orient='horizontal',variable=r,from_=0,to=255,command=fnBg)
r.set(255)	#用set()方法設定刻度值
sclR.pack()
g=tk.IntVar()
sclG=tk.Scale(frmRGB,label='綠：',orient='horizontal',variable=g,from_=0,to=255,command=fnBg)
sclG.pack()
g.set(255)
b=tk.IntVar()
sclB=tk.Scale(frmRGB,label='藍：',orient='horizontal',variable=b,from_=0,to=255,command=fnBg)
sclB.pack()
b.set(255)
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch09\test.py

import tkinter as tk
import random as rnd

def fnTest():
    global ans		#宣告ans為全域變數來記錄答案
    n=int(spnNum.get()) #取得使用者選擇的位數
    num=[[1,9],[10,99],[100,999]]   #用二維串列儲存各位數的亂數範圍
    r1=rnd.randint(num[n-1][0],num[n-1][1])
    r2=rnd.randint(num[n-1][0],num[n-1][1])
    if(r2>r1):	#若r2>r1就兩者互換
        r1,r2=r2,r1
    if(spnOpt.get()=='加法'):	#若選擇'加法'
        opt='+'
        ans=r1+r2
    else:
        opt='-'
        ans=r1-r2        
    lblTest.config(text='{} {} {} ='.format(r1,opt,r2))
    entAns.focus_set()
    btnTest.config(state='disable')
    btnAns.config(state='normal')
    
def fnAns():
    global ans
    userAns=int(entAns.get())
    if(userAns==ans):
        msg.set('太棒了！答案正確！')
    else:
        msg.set('答錯了！答案是：{}'.format(ans))
    btnTest.config(state='normal')
    btnAns.config(state='disable')
    
win = tk.Tk()
win.title('加減法測驗')
win.geometry('300x160')
frmTest=tk.Frame(win,relief='raised',borderwidth=2)
frmTest.pack(side='left',padx=5,pady=3)
lblTest=tk.Label(frmTest,text=' ',font=('微軟正黑體',20))
lblTest.pack(pady=5)
ans=tk.IntVar()
entAns=tk.Entry(frmTest,textvariable=ans)
entAns.pack(pady=5)
msg=tk.StringVar()
msg.set('設定後按 <出題> 鈕開始測驗')
lblMsg=tk.Label(frmTest,textvariable=msg)
lblMsg.pack(pady=5)
frmSet=tk.Frame(win,relief='raised',borderwidth=2)
frmSet.pack(side='left',padx=5,pady=3)
tk.Label(frmSet,text='運算：').pack(anchor='w')
lstOpt=['加法','減法']
spnOpt=tk.Spinbox(frmSet,values=lstOpt)
spnOpt.pack(anchor='w')
tk.Label(frmSet,text='位數：').pack(anchor='w')
spnNum=tk.Spinbox(frmSet,from_=1,to=3)
spnNum.pack(anchor='w')
btnTest=tk.Button(frmSet, text='出題', command=fnTest)
btnTest.pack(side='left',pady=3)
btnAns=tk.Button(frmSet, text='核對', command=fnAns,state='disable')
btnAns.pack(side='right',pady=3)
ans=0
win.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch08\album.py

import tkinter as tk
def fnSet(img):
    lblPhoto.config(image=img)
    
win = tk.Tk()
win.title('相簿')
win.geometry('250x230')
imgPhoto1=tk.PhotoImage(file='sheep1.png')
imgPhoto2=tk.PhotoImage(file='cat.png')
imgPhoto3=tk.PhotoImage(file='sheep2.png')
imgPhoto1_s=imgPhoto1.subsample(4,4)
imgPhoto2_s=imgPhoto2.subsample(4,4)
imgPhoto3_s=imgPhoto3.subsample(4,4)
lblPhoto=tk.Label(win,image=imgPhoto1)
lblPhoto.pack()
lfrmSet=tk.LabelFrame(win,text='選擇照片',relief='raised',borderwidth=2)
lfrmSet.pack()
btn1=tk.Button(lfrmSet,image=imgPhoto1_s,command=lambda:fnSet(imgPhoto1))
btn1.pack(side='left',padx=5)
btn2=tk.Button(lfrmSet,image=imgPhoto2_s,command=lambda:fnSet(imgPhoto2))
btn2.pack(side='left',padx=5)
btn3=tk.Button(lfrmSet,image=imgPhoto3_s,command=lambda:fnSet(imgPhoto3))
btn3.pack(side='left',padx=5)
win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch08\bmi.py

import tkinter as tk

def fnBmi():
    height = userH.get()	#用get方法取得身高
    weight = userW.get()
    bmi = round(weight / pow(height, 2), 2)
    msg=''
    if bmi < 18.5:
        msg='體重過輕！'
    elif bmi >= 24:
        msg='體重過重！'
    else :
        msg='體重剛好！'    
    tk.messagebox.askokcancel('注意','你的BMI指數為：{} {}'.format(bmi, msg))
    
win = tk.Tk()
win.title('BMI計算')
win.geometry('240x200')
win.configure(bg='white')
lblTitle = tk.Label(win, text='BMI 計算',font=('微軟正黑體', 16),fg='white',bg='blue')
lblTitle.pack(pady=10,fill='x')
tk.Label(win, text='身高(公尺，請輸入浮點數)').pack(pady=5,anchor='w')
userH=tk.DoubleVar()		#宣告userH為浮點數物件
entH = tk.Entry(win,textvariable=userH).pack()  #textvariable參數值為userH
tk.Label(win, text='體重(公斤，請輸入整數)').pack(pady=5,anchor='w')
userW=tk.IntVar()		#宣告userW為整數物件
entW = tk.Entry(win,textvariable=userW).pack()  #textvariable參數值為userW
btnCal = tk.Button(win, text=' 計算 ', command=fnBmi).pack(pady=5)
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch08\circle.py

import tkinter as tk

def fnCal():
    r = userR.get()
    u=unid.get()
    if (kind.get() == '圓周長'):  		#若選取圓周長
        a=3.14*2*r
        tk.messagebox.showinfo('圓周長','圓周長為 {:.2f} {}'.format(a,u))
    else:
        a=3.14*r*r
        tk.messagebox.showinfo('圓面積','圓面積為 {:.2f} 平方{}'.format(a,u))
  
win = tk.Tk()
win.title('圓形計算')
win.geometry('300x200')
lfrmR=tk.LabelFrame(win,text='輸入半徑：')
lfrmR.pack(pady=10)
userR=tk.IntVar()
userR.set(10)
entR= tk.Entry(lfrmR,textvariable=userR).pack(pady=3)
lblMsg=tk.Label(lfrmR, text = '請輸入半徑(整數)然後選擇項目').pack(pady=10)

lfrmKind=tk.LabelFrame(win,text='計算類別')
lfrmKind.pack(side='left',pady=10,padx=10,fill='x',expand=1)
kinds=['圓周長','圓面積']
kind=tk.StringVar()
for k in kinds:
    tk.Radiobutton(lfrmKind,text=k,variable=kind,value=k,command=fnCal).pack(pady=3)
kind.set('圓周長')

lfrmUnid=tk.LabelFrame(win,text='單位')
lfrmUnid.pack(side='left',pady=10,padx=10,fill='x',expand=1)
unids=['公分','英吋']
unid=tk.StringVar()
for u in unids:
    tk.Radiobutton(lfrmUnid,text=u,variable=unid,value=u,command=fnCal).pack(pady=3)
unid.set(unids[0])  
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch08\color.py

import tkinter as tk

def fnBlue():
    frmColor.config(bg='blue')

def fnRed():
    frmColor.config(bg='red')

def fnGreen():
    frmColor.config(bg='green')  
    
win = tk.Tk()
win.title('顏色切換')
win.geometry('240x200')
frmColor=tk.Frame(win,width=200,height=100,relief='raised',borderwidth=3,bg='white')
frmColor.pack(pady=5)
lfrmBtns=tk.LabelFrame(win,text='顏色')
lfrmBtns.pack(pady=20,fill='x')
btnBlue=tk.Button(lfrmBtns,text='藍色',width=8,command=fnBlue).pack(side='left',padx=5)
btnRed=tk.Button(lfrmBtns,text='紅色',width=8,command=fnRed).pack(side='left',padx=5)
btnGreen=tk.Button(lfrmBtns,text='綠色',width=8,command=fnGreen).pack(side='left',padx=5)
win.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch08\counter.py

import tkinter as tk
num = 0
def fnAdd():
    global num		#宣告為全域變數
    num += 1		#num加1
    lblNum['text']=str(num)	#重設標籤文字
    if (num>0):		#若num大於0，就設歸零鈕可以使用
        btnClear['state']='normal'
    
def fnClear():
    global num
    num = 0
    lblNum['text']=str(num)
    btnClear['state']='disabled'  #設歸零鈕不能使用
 
win=tk.Tk()
win.geometry('300x200')
win.title('計數器')
win.configure(bg='white')
lblTitle=tk.Label(win, text = '計數器',font=('標楷體', 16),fg='white',bg='blue')
lblNum=tk.Label(win, text = '0',font=('微軟正黑體', 36))
btnAdd=tk.Button(win, text = '加 1',pady=5,padx=10,command=fnAdd)
btnClear=tk.Button(win, text = '歸零',pady=5,padx=10,command=fnClear,state='disabled')
lblTitle.pack(pady=10,fill='x')
lblNum.pack(pady=20,fill='x')
btnAdd.pack(pady=5, side='left',fill='x', expand=True)
btnClear.pack(pady=5, side='left',fill='x', expand=True)
win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch08\end.py

import tkinter as tk

def fnEnd():
    res = tk.messagebox.askokcancel('注意','確定要結束程式嗎？')
    if(res == True):	#若傳回值為 True
        win.destroy()   #結束程式執行
        
win=tk.Tk()
win.geometry('300x150')
win.title('對話方塊')
lblTitle=tk.Label(win, text = '按鈕結束程式',font=('標楷體', 16))
btnEnd=tk.Button(win, text = '結束',pady=5,padx=10,command=fnEnd)
lblTitle.pack(pady=20)
btnEnd.pack(pady=5)
win.mainloop()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch08\survey.py

import tkinter as tk

def fnOk():
    lfrmSpot=tk.LabelFrame(win,text='勾選建議地點(可複選)：')
    lfrmSpot.pack(pady=10)
    for i in range(3):
        check[i]=tk.BooleanVar()	#設check[]元素值為布林值物件
        tk.Checkbutton(lfrmSpot,text=spots[i],variable=check[i]).pack(anchor='w')
def fnMsg():
    if ok.get()==True:
        msg='勾選的地點為：'
        for i in range(3):
            if check[i].get()==True:	#若check[i]元素值為True
                msg += (spots[i]+'、')	#將spots[i]元素值加入msg字串
        tk.messagebox.showinfo('訊息',msg[:len(msg)-1])
    else:
        tk.messagebox.showinfo('訊息','期盼下次你能參加')
    win.destroy()
    
win = tk.Tk()
win.title('旅遊問卷')
win.geometry('220x180')
ok=tk.BooleanVar()
chkOK=tk.Checkbutton(win,text='參加旅遊',variable=ok, command=fnOk).pack()
spots=['九份與金瓜石','日月潭','墾丁國家公園']
check={}
btnSend = tk.Button(win, text=' 送出 ', command=fnMsg).pack(pady=5)
win.mainloop()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


