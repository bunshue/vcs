# Python 新進測試 13

print("求面積")
class Rectangle():       #定義父類別  
    def __init__(self, width,height):
        self.width = width    #定義共用屬性   
        self.height = height  #定義共用屬性
    def area(self):           #定義共用方法 
        return self.width * self.height
        
class Triangle(Rectangle): #定義子類別  
    def area2(self):       #定義子類別的共用方法 
        return (self.width * self.height)/2
     
triangle = Triangle(5,6) #建立 triangle 物件
print("矩形面積=",triangle.area())    #30
print("三角形面積=",triangle.area2()) #15


print("求面積")

def click1():
    textvar.set("我已經被按過了！")

# 導入套件
import tkinter as tk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 600
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

textvar = tk.StringVar()
button1 = tk.Button(window, textvariable=textvar, command=click1)
textvar.set("按鈕")
button1.pack()

window.mainloop()

print("求面積")

