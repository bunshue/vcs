# ch19_30.py
from tkinter import * 
import tkinter.messagebox
import random 
        
def reset():
    ''' 重設長條圖 '''
    global i
    i = 0                               # 重設索引
    random.shuffle(mylist)
    newBar()

def go():                               
    ''' 執行排序 '''
    global i
    if i > len(mylist) - 1:
        tkinter.messagebox.showinfo("showinfo", "排序完成")
        return              
# 將mylist[i]插入mylist[0 .. i-1]
    currentValue = mylist[i]
    k = i - 1
# 找尋mylist[i]適當位置
    while k >= 0 and mylist[k] > currentValue:      
        mylist[k + 1] = mylist[k]
        k -= 1            
# 正式執行插入list[k + 1]
    mylist[k + 1] = currentValue

    newBar()                            # 繪製新的長條圖   
    i += 1                              # 增加串列指標
        
def newBar():
    global i, gap
    canvas.delete("line")               # 刪除bar
    canvas.delete("text")               # 刪除bar上方數字
    canvas.create_line(10, ht-gap, wd-10, ht-gap, tag="line")
    barWd = (wd - 20) / len(mylist)
        
    maxC = int(max(mylist))
    for j in range(len(mylist)):
        canvas.create_rectangle(j*barWd+10, (ht-gap)*(1-mylist[j]/(maxC+4)), 
                                (j+1)*barWd+10, ht-gap, tag="line")       
                         
        canvas.create_text(j*barWd+10+barWd/2, (ht-gap)*(1-mylist[j]/(maxC+4))-8, 
                           text=str(mylist[j]), tag = "text")

    if i >= 0:
        canvas.create_rectangle(i*barWd+10, (ht-gap)*(1-mylist[i]/(maxC+4)), 
                                (i + 1)*barWd+10, ht-gap, fill="blue", tag="line")


wd = 400                                # 視窗寬度
ht = 200                                # 視窗高度
gap = 20                                # 長條圖與視窗的間距
i = 0                                   # 這是目前排序指標

tk = Tk()                           
tk.title("ch19_30")                     # 視窗標題        
canvas = Canvas(tk, width = wd, height = ht)
canvas.pack()
        
frame = Frame(tk)
frame.pack()
        
btnStep = Button(frame, text = "執行", command = go)
btnStep.pack(side = LEFT)
btnReset = Button(frame, text = "重置", command = reset)
btnReset.pack(side = LEFT)
btnReset = Button(frame, text = "結束", command = tk.destroy)
btnReset.pack(side = LEFT)

mylist = [ x for x in range(1, 20) ]
reset()
newBar()
       
tk.mainloop()


