
import tkinter as tk


print("------------------------------------------------------------")  # 60個
print('綁定鍵盤滑鼠事件 Listbox')
print("------------------------------------------------------------")  # 60個


# night_market.py

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
    labelMsg.config(text=msg[iArea][iNM]) #重設標籤的文字內容
    
window = tk.Tk()
window.geometry("600x800")
window.title('台灣夜市簡介')

tk.Label(window,text='台灣夜市之旅',font=('微軟正黑體',16)).pack()
lfrmNM=tk.LabelFrame(window,text='夜市名稱',relief='raised',borderwidth=2)
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
lfrmMsg=tk.LabelFrame(window,text='夜市簡介',relief='raised',borderwidth=2)
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
labelMsg=tk.Label(lfrmMsg,text=msg[0][0],font=(12),wraplength=120,justify='left')
labelMsg.pack(anchor='n')

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
