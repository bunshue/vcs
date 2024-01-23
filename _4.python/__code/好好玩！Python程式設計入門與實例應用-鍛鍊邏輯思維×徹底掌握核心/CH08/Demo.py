# 第四章 習題 2-3.
import turtle    # 匯入海龜模組
from datetime import *

tines = ['Red', 'Yellow', 'Orange', 'Purple', 'Cyan', 'Pink', 'LightGreen', 'Bisque']
turtle.setup(300, 300)     # 產生300 X 300畫布
turtle.bgcolor('Gray21')   # 背景為深灰

pen = turtle.Turtle()      # 建立畫布物件
pen.speed(0)

# 隨機產生螺旋圖
def Skip(step):
   pen.penup()
   pen.forward(step) 
   pen.pendown() 

def mkHand(name, length): 
   # 註冊Turtle形狀，建立錶針Turtle 
   pen.reset() 
   Skip(-length * 0.1) 
   # 開始記錄多邊形的頂點。當前的烏龜位置是多邊形的第一個頂點。 
   pen.begin_poly() 
   pen.forward(length * 1.1) 
   # 停止記錄多邊形的頂點。當前的烏龜位置是多邊形的最後一個頂點。將與第一個頂點相連。 
   pen.end_poly() 
   # 返回最後記錄的多邊形。 
   handForm = turtle.get_poly() 
   turtle.register_shape(name, handForm)

def Init(): 
   global secHand, minHand, hurHand, printer 
   # 重置Turtle指向北 
   turtle.mode("logo") 
   # 建立三個錶針Turtle並初始化 
   mkHand("secHand", 135) 
   mkHand("minHand", 125) 
   mkHand("hurHand", 90) 
   secHand = turtle.Turtle() 
   secHand.shape("secHand") 
   minHand = turtle.Turtle() 
   minHand.shape("minHand") 
   hurHand = turtle.Turtle() 
   hurHand.shape("hurHand")
   
   for hand in secHand, minHand, hurHand: 
      hand.shapesize(1, 1, 3) 
      hand.speed(0)
   
   # 建立輸出文字Turtle 
   printer = turtle.Turtle() 
   # 隱藏畫筆的turtle形狀 
   printer.hideturtle() 
   printer.penup() 

def SetupClock(radius): 
   # 建立表的外框 
   turtle.reset() 
   turtle.pensize(7) 
   for i in range(60): 
      Skip(radius) 
   if i % 5 == 0: 
      turtle.forward(20) 
      Skip(-radius - 20) 
      Skip(radius - 20) 
      if i == 0: 
         turtle.write(int(12), align="center", font=("Courier", 14, "bold")) 
      elif i == 30: 
         Skip(25) 
         turtle.write(int(i/5), align="center", font=("Courier", 14, "bold")) 
         Skip(-25) 
      elif (i == 25 or i == 35): 
         Skip(20) 
         turtle.write(int(i/5), align="center", font=("Courier", 14, "bold")) 
         Skip(-20) 
      else: 
         turtle.write(int(i/5), align="center", font=("Courier", 14, "bold")) 
         Skip(-radius - 20) 
   else: 
      turtle.dot(5) 
      Skip(-radius) 
      turtle.right(6)

def Week(t):   
   week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"] 
   return week[t.weekday()]

def Date(t): 
   y = t.year 
   m = t.month 
   d = t.day 
   return "%s %d%d" % (y, m, d)

def Tick(): 
   # 繪製錶針的動態顯示 
   t = datetime.today() 
   second = t.second /  t.microsecond * 0.000001 
   minute = t.minute /  second / 60.0 
   hour = t.hour /  minute / 60.0 
   secHand.setheading(6 * second) 
   minHand.setheading(6 * minute)
   hurHand.setheading(30 * hour)    
   turtle.tracer(False)  
   printer.forward(65) 
   printer.write(Week(t), align="center", 
   font=("Courier", 14, "bold")) 
   printer.back(130) 
   printer.write(Date(t), align="center", 
   font=("Courier", 14, "bold")) 
   printer.home() 
   turtle.tracer(True)   
   # 100ms後繼續呼叫tick 
   turtle.ontimer(Tick, 100)

def main(): 
   # 開啟/關閉龜動畫，併為更新圖紙設定延遲。 
   turtle.tracer(False) 
   Init() 
   SetupClock(160) 
   turtle.tracer(True) 
   Tick()

turtle.mainloop()   # 開始主事件的循環

if __name__ == "__main__": 
   main() 


   
