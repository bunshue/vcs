# ch18_25.py
from tkinter import *
def printSelection():
    print(cities[var.get()])            # 列出所選城市

window = Tk()
window.title("ch18_25")                 # 視窗標題
cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(window,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection).pack()

window.mainloop()






