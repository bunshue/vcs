
import tkinter as tk


print("------------------------------------------------------------")  # 60個

print('綁定鍵盤滑鼠事件 Label')

print("------------------------------------------------------------")  # 60個

def fnEnter(event):
    labelTest['bg']='lightblue'

def fnLeave(event):
    labelTest.config(text='試試看',bg='gray')
    
def fnMotion(event):
    labelTest['text']='游標移動'

def fnClick(event):
    global mx,my	#宣告mx,my為全域變數
    mx=event.x	#紀錄按下時滑鼠游標的x坐標
    my=event.y	#紀錄按下時滑鼠游標的y坐標
    
def fnB1Motion(event):
    global mx,my	#宣告mx,my為全域變數
    labelX=labelTest.winfo_rootx()-window.winfo_rootx()	#計算labelTest在視窗的x坐標
    labelY=labelTest.winfo_rooty()-window.winfo_rooty()	#計算labelTest在視窗的y坐標
    labelTest['text']='拖曳中...'
    labelTest.place(x=labelX+(event.x-mx),y=labelY+(event.y-my))	#重設labelTest位置
    
window = tk.Tk()
window.geometry("600x800")
window.title('滑鼠事件測試')

mx=0
my=0
labelTest=tk.Label(window,text='試試看',width=8,height=2,relief='groove',bg='gray')
labelTest.place(x=80,y=100)
labelTest.bind('<Enter>',fnEnter) #<Enter>事件綁定fnEnter事件處理函式
labelTest.bind('<Leave>',fnLeave) #<Leave>事件綁定fnLeave事件處理函式
labelTest.bind('<Motion>',fnMotion) #<Motion>事件綁定fnMotion事件處理函式
labelTest.bind('<Button-1>',fnClick) #<Button-1>事件綁定fnClick事件處理函式
labelTest.bind('<B1-Motion>',fnB1Motion) #<B1-Motion>事件綁定fnB1Motion事件處理函式

window.mainloop()

