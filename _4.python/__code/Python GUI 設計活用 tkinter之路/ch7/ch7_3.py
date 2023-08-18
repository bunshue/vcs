# ch7_3.py
from tkinter import *
def printSelection():
    print(cities[var.get()])            # 列出所選城市

root = Tk()
root.title("ch7_3")                     # 視窗標題
cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(root,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(root,
                text=city,
                variable=var,value=val, 
                command=printSelection).pack()

root.mainloop()






