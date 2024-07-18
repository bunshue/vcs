"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

'''
#chap8-01
#Cars基礎類別
class Cars():
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    self.__factory=factory  #廠牌屬性(保護)
    self.__model=model  #型號屬性(保護)
    self.color=color  #顏色屬性(可改)
    self.seat=seat  #座位屬性(可改)    
    self.__displacement=displacement #排氣量或電功率屬性(保護)
  #屬性(Attribute)
  #函式唯讀
  #傳回製造商出廠資料
  def manufacture(self):
    if self.__model.find("電能")>=0:  
      return self.__factory+"-"+self.__model+"-"+str(self.__displacement)+"HP"
    else:
      return self.__factory+"-"+self.__model+"-"+str(self.__displacement)+"CC" 
  #傳回排氣量或電功率(保護)
  def displacement(self):
    return self.__displacement 
  #傳回燃料稅(因為汽油、柴油、電能車計算方式不同，交由各子類別自行定義函式)
  def fueltax(self):
    pass
  #傳回牌照稅(因為主要的汽油、柴油都是以排氣量計算，只有電能車不同，另外覆寫即可)  
  def licensetax(self):
    if self.__displacement<=500:
      return 1620
    elif self.__displacement<=600:
      return 2160
    elif self.__displacement<=1200:
      return 4320     
    elif self.__displacement<=1800:
      return 7120
    elif self.__displacement<=2400:
      return 11230    
    elif self.__displacement<=3000:
      return 15210 
    elif self.__displacement<=3600:
      return 28220   
    elif self.__displacement<=4200:
      return 28220    
    elif self.__displacement<=4800:
      return 46170
    else:
      return 46170 
  #傳回全部稅金    
  def totaltax(self):
    return self.fueltax()+self.licensetax()  
  #方法(Method)   
  #輸出汽車屬性                                        
  def info(self):
    if self.__model.find("電能")>=0:    
      print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.seat)+"人座"+str(self.__displacement)+"HP")
    else:   
      print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.seat)+"人座"+str(self.__displacement)+"CC")
#汽油車衍生類別
class GasolineCars(Cars):
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    super().__init__(factory, '汽油'+model, color, seat, displacement)
  #屬性(Attribute)
  #傳回燃料稅
  def fueltax(self):
    if self.displacement()<=500:
      return 2160
    elif self.displacement()<=600:
      return 2880
    elif self.displacement()<=1200:
      return 4320     
    elif self.displacement()<=1800:
      return 4800
    elif self.displacement()<=2400:
      return 6180    
    elif self.displacement()<=3000:
      return 7200 
    elif self.displacement()<=3600:
      return 8640    
    elif self.displacement()<=4200:
      return 9810     
    elif self.displacement()<=4800:
      return 11220 
    else:
      return 12180  
#柴油車衍生類別
class DieselCars(Cars):
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    super().__init__(factory, '柴油'+model, color, seat, displacement)
  #屬性(Attribute)
  #傳回燃料稅
  def fueltax(self):
    if self.displacement()<=1800:
      return 2880
    elif self.displacement()<=2400:
      return 3708   
    elif self.displacement()<=3000:
      return 4320
    elif self.displacement()<=3600:
      return 5184    
    elif self.displacement()<=4200:
      return 5886     
    elif self.displacement()<=4800:
      return 6732
    else:
      return 7308
#電能車衍生類別
class ElectricCars(Cars):
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    super().__init__(factory, '電能'+model, color, seat, displacement)
  #屬性(Attribute)
  #傳回牌照稅
  def licensetax(self):
    return 0
  #傳回燃料稅
  def fueltax(self):
    return 0

def tax(obj):
  print(obj.manufacture(),":",obj.totaltax())

#建構第1輛汽油車物件
print("==Test1==")
a = GasolineCars('CITROEN','BX16TGS','灰', 5, 1580)
print(type(a))
print(a.manufacture())
a.info()
print(a.fueltax())
print(a.licensetax())
print(a.totaltax())
#可以修改屬性
a.color="綠"
a.seat=2
print(a.manufacture())
a.info()
#建構第2輛柴油車物件
print("==Test2==")
b = DieselCars('福特六和','C346-9W','白', 5, 1997)
print(type(b))
print(b.manufacture())
b.info()
print(b.fueltax())
print(b.licensetax())
print(b.totaltax())
#建構第3輛電能車物件
print("==Test3==")
c = ElectricCars('Tesla','Model 3','紅', 5, 346)
print(type(c))
print(c.manufacture())
c.info()
print(c.fueltax())
print(c.licensetax())
print(c.totaltax())
print("==Test4==")
tax(a)
tax(b)
tax(c)

print("------------------------------------------------------------")  # 60個

#chap8-02
#輪胎類別
class Wheels():
  #建構式
  def __init__(self, width, diameter):
    self.width=width  #寬度屬性
    self.diameter=diameter  #直徑屬性
  #自訂義Wheels物件的比較關係(判斷是否相等) 
  #判斷兩個輪胎是否為相同類型根據輪胎寬度、直徑 
  def __eq__(self, other):
    return self.width==other.width and self.diameter==other.diameter
  def eq(self, other):
    return self.width==other.width and self.diameter==other.diameter
  #屬性(Attribute)  
  def dimension(self):
    return ("寬"+str(self.width)+"mm"+" 直徑"+str(self.diameter)+"inch")
  #方法(Method)   
  #輸出輪胎屬性     
  def info(self):
    print("寬"+str(self.width)+"mm"+" 直徑"+str(self.diameter)+"inch")

#機車基礎類別
class Motorcycles():
  #類別方法變數
  counts=0
  #建構式
  def __init__(self, factory, model, color, displacement, wheel):
    self.__factory=factory  #廠牌屬性
    self.__model=model  #型號屬性
    self.color=color  #顏色屬性
    self.__displacement=displacement #排氣量或電功率屬性
    self.wheel=wheel #輪胎屬性
    #改變類別方法變數
    Motorcycles.counts=Motorcycles.counts+1
  #解構式   
  def __del__(self):
    #改變類別方法變數
    Motorcycles.counts=Motorcycles.counts-1    
  #自訂義Motorcycles物件的比較關係(判斷是否相等) 
  #判斷兩台機車是否為相同類型根據廠商、型號、排氣量   
  def __eq__(self, other):
    return self.__factory==other.__factory and self.__model==other.__model and self.__displacement==other.__displacement
  def eq(self, other):
    return self.__factory==other.__factory and self.__model==other.__model and self.__displacement==other.__displacement 
  #類別方法
  @classmethod
  #顯示類別方法變數
  def motocycles_counts(cls):
    return cls.counts    
  #屬性(Attribute)
  #函式唯讀
  #傳回製造商出廠資料    
  def manufacture(self):
    if self.__model.startswith("汽油"):
      return self.__factory+"-"+self.__model+"-"+str(self.__displacement)+"CC"
    else:
      return self.__factory+"-"+self.__model+"-"+str(self.__displacement)+"HP"
  #傳回排氣量或電功率(保護)      
  def displacement(self):
    return self.__displacement  
  #傳回燃料稅(以汽油機車為主，電能車不同，另外覆寫即可)
  def fueltax(self):
    if self.displacement()<=50:
      return 300
    elif self.displacement()<=125:
      return 450
    elif self.displacement()<=250:
      return 600     
    elif self.displacement()<=500:
      return 900
    elif self.displacement()<=600:
      return 1200    
    elif self.displacement()<=1200:
      return 1800 
    else:
      return 2010  
  #傳回牌照稅(因為汽油是以排氣量計算，只有電能車不同，另外覆寫即可)       
  def licensetax(self):
    if self.displacement()<=150:
      return 0
    elif self.displacement()<=250:
      return 800
    elif self.displacement()<=500:
      return 1620     
    elif self.displacement()<=600:
      return 2160
    elif self.displacement()<=1200:
      return 4320    
    elif self.displacement()<=1800:
      return 7120 
    else:
      return 11230 
  #傳回全部稅金         
  def totaltax(self):
    return self.fueltax()+self.licensetax()  
  #方法(Method)   
  #輸出機車屬性                                       
  def info(self):
    if self.__model.startswith("汽油"):
      print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.displacement())+"CC 輪胎"+self.wheel.dimension())    
    else:
      print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.displacement())+"HP 輪胎"+self.wheel.dimension()) 

class GasolineMotorcycles(Motorcycles):
  #建構式
  def __init__(self, factory, model, color, displacement, wheel):
    super().__init__(factory, '汽油'+model, color, displacement, wheel)

class ElectricMotorcycles(Motorcycles):
  #建構式
  def __init__(self, factory, model, color, displacement, wheel):
    super().__init__(factory, '電能'+model, color, displacement, wheel)
  #傳回燃料稅(0元)
  def fueltax(self):
    return 0
  #傳回牌照稅(0元)
  def licensetax(self):
    return 0  

#建立第1台機車
print("==Test1==")
d = GasolineMotorcycles('光陽','SJ25JF','白黑銀',124,Wheels(100,10))
#print(type(d))
print(d.manufacture())
d.info()
print(d.fueltax())
print(d.licensetax())
print(d.totaltax())
#建立第2台機車
print("==Test2==")
e = GasolineMotorcycles('功學社','CT-50','白紅',49,Wheels(100,10))
#print(type(e))
print(e.manufacture())
e.info()
print(e.fueltax())
print(e.licensetax())
print(e.totaltax())
#建立第3台機車
print("==Test3==")
f = ElectricMotorcycles('睿能','GHS6B2','白',8.58,Wheels(100,10))
#print(type(f))
print(f.manufacture())
f.info()
print(f.fueltax())
print(f.licensetax())
print(f.totaltax())
#建立第4台機車
print("==Test4==")
g = GasolineMotorcycles('光陽','SK60AF','深藍',298,Wheels(100,10))
#print(type(g))
print(g.manufacture())
g.info()
print(g.fueltax())
print(g.licensetax())
print(g.totaltax())
#建立第5台機車
print("==Test5==")
h = ElectricMotorcycles('睿能','GHS6B2','紅',8.58,Wheels(100,10))
#print(type(h))
print(h.manufacture())
h.info()
print(h.fueltax())
print(h.licensetax())
print(h.totaltax())
#判斷f與h這兩台機車是否為相同類型
print("==Test6==")
f.info()
h.info()
print(f==h)
#判斷d與e這兩台機車的輪台是否為相同類型
d.wheel.info()
e.wheel.info()
print(d.wheel.eq(e.wheel))
print(d.wheel==e.wheel)
print("==Test7==")
#查看總共新增了幾台機車
print(Motorcycles.counts)
#刪除d車
del d
print(Motorcycles.counts)
#刪除e車
del e
print(Motorcycles.counts)
#刪除f車
del f
print(Motorcycles.counts)
#刪除g車
del g
print(Motorcycles.counts)
#刪除h車
del h
print(Motorcycles.counts)

print("------------------------------------------------------------")  # 60個

#chap8-03
#輪胎類別
class Wheels():
  #建構式
  def __init__(self, width, diameter):
    self.width=width  #寬度屬性
    self.diameter=diameter  #直徑屬性
  #自訂義Wheels物件的比較關係(判斷是否相等) 
  #判斷兩個輪胎是否為相同類型根據輪胎寬度、直徑 
  def __eq__(self, other):
    return self.width==other.width and self.diameter==other.diameter
  def eq(self, other):
    return self.width==other.width and self.diameter==other.diameter
  #屬性(Attribute)  
  def dimension(self):
    return ("寬"+str(self.width)+"mm"+" 直徑"+str(self.diameter)+"inch")
  #方法(Method)   
  #輸出輪胎屬性     
  def info(self):
    print("寬"+str(self.width)+"mm"+" 直徑"+str(self.diameter)+"inch")

#車輛基礎類別
class Vehicles():
  #建構式
  def __init__(self, factory, model, color, displacement):
    self.__factory=factory  #廠牌屬性
    self.__model=model  #型號屬性
    self.color=color  #顏色屬性
    self.__displacement=displacement #排氣量或電功率屬性
  #自訂義車輛物件的比較關係(判斷是否相等) 
  #判斷兩車輛是否為相同類型根據廠商、型號、排氣量   
  def __eq__(self, other):
    return self.__factory==other.__factory and self.__model==other.__model and self.__displacement==other.__displacement
  def eq(self, other):
    return self.__factory==other.__factory and self.__model==other.__model and self.__displacement==other.__displacement  
  #屬性(Attribute)
  #函式唯讀
  #傳回製造商出廠資料    
  def manufacture(self):
    if self.__model.startswith("汽油"):
      return self.__factory+"-"+self.__model+"-"+str(self.__displacement)+"CC"
    else:
      return self.__factory+"-"+self.__model+"-"+str(self.__displacement)+"HP"
  #傳回排氣量或電功率(保護)      
  def displacement(self):
    return self.__displacement  
  #傳回燃料稅(另外覆寫即可)
  def fueltax(self):
    pass
      
  #傳回牌照稅(因為汽油是以排氣量計算，只有電能車不同，另外覆寫即可)       
  def licensetax(self):
    if self.displacement()<=125:
      return 0
    elif self.displacement()<=250:
      return 800
    elif self.displacement()<=500:
      return 1620     
    elif self.__displacement<=600:
      return 2160
    elif self.__displacement<=1200:
      return 4320     
    elif self.__displacement<=1800:
      return 7120
    elif self.__displacement<=2400:
      return 11230    
    elif self.__displacement<=3000:
      return 15210 
    elif self.__displacement<=3600:
      return 28220   
    elif self.__displacement<=4200:
      return 28220    
    elif self.__displacement<=4800:
      return 46170
    else:
      return 46170       
  #傳回全部稅金         
  def totaltax(self):
    return self.fueltax()+self.licensetax()  
  #方法(Method)   
  #輸出車輛屬性                                       
  def info(self):
    if self.__model.startswith("電能"):
      if self.__model.find("機車")>=0:
        print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.displacement())+"HP 輪胎"+self.wheel.dimension())          
      else:  
        print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.seat)+"人座"+str(self.__displacement)+"HP")
    else:
      if self.__model.find("機車")>=0:
        print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.displacement())+"CC 輪胎"+self.wheel.dimension()) 
      else:   
        print(self.__factory+"-"+self.__model+"-"+self.color+"色-"+str(self.seat)+"人座"+str(self.__displacement)+"CC")

#機車基礎類別
class Motorcycles(Vehicles):
  #類別方法變數
  counts=0
  #建構式
  def __init__(self, factory, model, color, displacement, wheel):
    super().__init__(factory, model, color, displacement)
    self.wheel=wheel #輪胎屬性
    #改變類別方法變數
    Motorcycles.counts=Motorcycles.counts+1
  #解構式      
  def __del__(self):
    #改變類別方法變數
    Motorcycles.counts=Motorcycles.counts-1
  #類別方法
  @classmethod
  #顯示類別方法變數
  def motocycles_counts(cls):
    return cls.counts    
  #屬性(Attribute)  
  #方法(Method)     
  def fueltax(self):
    if self.displacement()<=50:
      return 300
    elif self.displacement()<=125:
      return 450
    elif self.displacement()<=250:
      return 600     
    elif self.displacement()<=500:
      return 900
    elif self.displacement()<=600:
      return 1200    
    elif self.displacement()<=1200:
      return 1800 
    else:
      return 2010   

class GasolineMotorcycles(Motorcycles):
  #建構式
  def __init__(self, factory, model, color, displacement, wheel):
    super().__init__(factory, '汽油機車'+model, color, displacement, wheel)

class ElectricMotorcycles(Motorcycles):
  #建構式
  def __init__(self, factory, model, color, displacement, wheel):
    super().__init__(factory, '電能機車'+model, color, displacement, wheel)
  #傳回燃料稅(0元)
  def fueltax(self):
    return 0
  #傳回牌照稅(0元)
  def licensetax(self):
    return 0  

#Cars基礎類別
class Cars(Vehicles):
  #類別方法變數
  counts=0
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    super().__init__(factory, model, color, displacement)    
    self.seat=seat  #座位屬性(可改) 
    #改變類別方法變數
    Cars.counts=Cars.counts+1
  #解構式     
  def __del__(self):
    #改變類別方法變數
    Cars.counts=Cars.counts-1
  #類別方法
  @classmethod
  #顯示類別方法變數
  def cars_counts(cls):
    return cls.counts    
  #屬性(Attribute)  
  #方法(Method)           

#汽油車衍生類別
class GasolineCars(Cars):
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    super().__init__(factory, '汽油汽車'+model, color, seat, displacement)
  #屬性(Attribute)
  #傳回燃料稅
  def fueltax(self):
    if self.displacement()<=500:
      return 2160
    elif self.displacement()<=600:
      return 2880
    elif self.displacement()<=1200:
      return 4320     
    elif self.displacement()<=1800:
      return 4800
    elif self.displacement()<=2400:
      return 6180    
    elif self.displacement()<=3000:
      return 7200 
    elif self.displacement()<=3600:
      return 8640    
    elif self.displacement()<=4200:
      return 9810     
    elif self.displacement()<=4800:
      return 11220 
    else:
      return 12180  
#柴油車衍生類別
class DieselCars(Cars):
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    super().__init__(factory, '柴油汽車'+model, color, seat, displacement)
  #屬性(Attribute)
  #傳回燃料稅
  def fueltax(self):
    if self.displacement()<=1800:
      return 2880
    elif self.displacement()<=2400:
      return 3708   
    elif self.displacement()<=3000:
      return 4320
    elif self.displacement()<=3600:
      return 5184    
    elif self.displacement()<=4200:
      return 5886     
    elif self.displacement()<=4800:
      return 6732
    else:
      return 7308
#電能車衍生類別
class ElectricCars(Cars):
  #建構式
  def __init__(self, factory, model, color, seat, displacement):
    super().__init__(factory, '電能汽車'+model, color, seat, displacement)
  #屬性(Attribute)
  #傳回牌照稅(0元)
  def licensetax(self):
    return 0
  #傳回燃料稅(0元)
  def fueltax(self):
    return 0

def tax(obj):
  print(obj.manufacture(),":",obj.totaltax())

#建構第1輛汽油車物件
print("==Test1==")
a = GasolineCars('CITROEN','BX16TGS','灰', 5, 1580)
#print(type(a))
print(a.manufacture())
a.info()
print(a.fueltax())
print(a.licensetax())
print(a.totaltax())
#可以修改屬性
a.color="綠"
a.seat=2
print(a.manufacture())
a.info()
#建構第2輛柴油車物件
print("==Test2==")
b = DieselCars('福特六和','C346-9W','白', 5, 1997)
#print(type(b))
print(b.manufacture())
b.info()
print(b.fueltax())
print(b.licensetax())
print(b.totaltax())
#建構第3輛電能車物件
print("==Test3==")
c = ElectricCars('Tesla','Model 3','紅', 5, 346)
#print(type(c))
print(c.manufacture())
c.info()
print(c.fueltax())
print(c.licensetax())
print(c.totaltax())
print("==Test4==")
#判斷a與b這兩輛汽車是否為相同類型
a.info()
b.info()
print(a==b)

#建立第1台機車
print("==Test5==")
d = GasolineMotorcycles('光陽','SJ25JF','白黑銀',124,Wheels(100,10))
#print(type(d))
print(d.manufacture())
d.info()
print(d.fueltax())
print(d.licensetax())
print(d.totaltax())
#建立第2台機車
print("==Test6==")
e = GasolineMotorcycles('功學社','CT-50','白紅',49,Wheels(100,10))
#print(type(e))
print(e.manufacture())
e.info()
print(e.fueltax())
print(e.licensetax())
print(e.totaltax())
#建立第3台機車
print("==Test7==")
f = ElectricMotorcycles('睿能','GHS6B2','白',8.58,Wheels(100,10))
#print(type(f))
print(f.manufacture())
f.info()
print(f.fueltax())
print(f.licensetax())
print(f.totaltax())
#建立第4台機車
print("==Test8==")
g = GasolineMotorcycles('光陽','SK60AF','深藍',298,Wheels(100,10))
#print(type(g))
print(g.manufacture())
g.info()
print(g.fueltax())
print(g.licensetax())
print(g.totaltax())
#建立第5台機車
print("==Test9==")
h = ElectricMotorcycles('睿能','GHS6B2','紅',8.58,Wheels(100,10))
#print(type(h))
print(h.manufacture())
h.info()
print(h.fueltax())
print(h.licensetax())
print(h.totaltax())
print("==Test10==")
#判斷f與h這兩台機車是否為相同類型
f.info()
h.info()
print(f==h)
print("==Test11==")
#判斷d與e這兩台機車的輪台是否為相同類型
d.wheel.info()
e.wheel.info()
print(d.wheel.eq(e.wheel))
print(d.wheel==e.wheel)
print("==Test12==")
tax(a)
tax(b)
tax(c) 
tax(d)
tax(e)
tax(f)
tax(g)
tax(h)
print("==Test13==")
#查看總共新增了幾輛汽車
print(Cars.counts)
#刪除a車
del a
print(Cars.counts)
#刪除b車
del b
print(Cars.counts)
#刪除c車
del c
print(Cars.counts)
print("==Test14==")
#查看總共新增了幾台機車
print(Motorcycles.counts)
#刪除d車
del d
print(Motorcycles.counts)
#刪除e車
del e
print(Motorcycles.counts)
#刪除f車
del f
print(Motorcycles.counts)
#刪除g車
del g
print(Motorcycles.counts)
#刪除h車
del h
print(Motorcycles.counts)

print("------------------------------------------------------------")  # 60個

#chap9-01b
import requests
import json

url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'
res = requests.get(url, verify = False)

print(res)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data=res.json() #方法2
print(data)

sys.exit()

#因為有欄位名稱
#只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
#轉換'確定病例數'欄位內容為整數(以利後面加總)
df['確定病例數'] = df['確定病例數'].astype(int)

startdate='2021/07/20'
#startdate=input("請輸日期(yyyy/mm/dd)")
#只保留個案研判日、是否為境外移入、確定病例數 三個欄位
df.drop(['確定病名','縣市','鄉鎮','性別','年齡層'],inplace=True,axis=1)
#設定過濾條件(累積)
indexNames=df[df['個案研判日']>startdate].index
#刪除所有大於指定日期的個案
df.drop(indexNames,inplace=True)
#計算累積確診人數
total=df.sum()['確定病例數']
print("累積確診人數:",total)
#設定過濾條件(今日)
indexNames=df[df['個案研判日']!=startdate].index
#刪除所有不是指定日期的個案
df.drop(indexNames,inplace=True)
#計算境外移入人數
imported=df[df['是否為境外移入']=='是'].sum()['確定病例數']
print("今日境外移入人數:",imported)
#計算本土人數
domestic=df[df['是否為境外移入']=='否'].sum()['確定病例數']
print("今日本土人數:",domestic)
total=imported+domestic
print("今日總人數:",total)
#若要查看有哪些欄位
print((df.keys()))
#也可以透過df.info()查看
df.info()
#也可以直接看前幾列
df.head(3)

print("------------------------------------------------------------")  # 60個

import requests

url ='https://www.dcard.tw/f/stock/p/237123381'
response = requests.get(url)
print(response.text)


print('chap7-02a')
import requests
url ='https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
print(res.text)

#chap7-01b
import requests
url ='http://jigsaw.w3.org/HTTP/connection.html'
response = requests.get(url)
#print(response.text)

#在<HEAD></HEAD>區塊中取得包圍網頁標題的指定字串<TITLE></TITLE>所在的位置
#stripe()去除字串頭尾的'\n'(換行)、'\t'(跳格)、' '(空白)
datapos1=response.text.find("<TITLE>")
datapos2=response.text.find("</TITLE>")
data=response.text[datapos1+7:datapos2]
data=data.strip()
print("網頁的<TITLE> :", data)
#在<BODY></BODY>區塊中取得包圍內容標題的指定字串<H1></H1>所在的位置
datapos1=response.text.find("<H1>")
datapos2=response.text.find("</H1>")
data=response.text[datapos1+4:datapos2]
#將設定斜體的HTML語法<I></I>移除
data=data.replace("<I>","")
data=data.replace("</I>","")
data=data.strip()
print("<網頁的H1的資料(去掉<I>)> :", data)

datapos1=response.text.find("<CODE>")
datapos2=response.text.find("</CODE>")
data=response.text[datapos1+7:datapos2]
data=data.strip()
print("網頁的<CODE> :", data)

print("------------------------------------------------------------")  # 60個

print('chap7-02b')
import requests
from bs4 import BeautifulSoup

url ='https://www.dcard.tw/f/stock/p/237123381'
response = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(response.text, 'html.parser') 
#把排版後的html印出來，因為未排版前有很多網頁語法缺乏換行符號，不易閱讀
#必須借助於Beautiful Shop套件
print(soup.prettify())

print("------------------------------------------------------------")  # 60個

print('chap7-02c')
import requests
from bs4 import BeautifulSoup

url = 'https://www.dcard.tw/f/stock/p/237123381'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" #使用者代理
    }

#response = requests.get(url="https://example.com", headers=headers)
response = requests.get(url, headers=headers)
#指定html.parser作為解析器
soup = BeautifulSoup(response.text, 'html.parser') 
#把排版後的html印出來
#print(soup.prettify())
a_tags = soup.find_all('h1')
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print("\n")

print("------------------------------------------------------------")  # 60個

print('chap7-02d')

import requests
from bs4 import BeautifulSoup

url = 'https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(res.text, 'html.parser') 
#把排版後的html印出來
#print(soup.prettify()) 
a_tags = soup.find_all('h1')
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print("\n")
a_tags = soup.find_all('div',limit=1)
a_tag=a_tags[0]
cc=""
for b in a_tag.contents:
  if str(b).find("gFINpq")>=0:  
    b=str(b).replace('\n','').replace('\r','')
    cc=cc+b
print(cc.strip())

print("------------------------------------------------------------")  # 60個

print('chap7-02e')

import requests
from bs4 import BeautifulSoup

url = 'https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(res.text, 'html.parser') 
#把排版後的html印出來
#print(soup.prettify()) 
a_tags = soup.find_all('h1')
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print()
a_tags = soup.find_all('div',limit=1)
a_tag=a_tags[0]
cc=""
for b in a_tag.contents:
  if str(b).find("gFINpq")>=0:  
    b=str(b)
    cc=cc+b
cc=cc.strip()
data=">>>>>原Po文章\n"
#尋找前四筆，第一個是原Po文章，後三個則為熱門留言
for j in range(4):
  #尋找最附近的<div class>有gFINpq
  datapos1=cc.find("gFINpq")
  #只保留這個字串以後的文字
  cc=cc[datapos1:] 
  while True:
    #尋找最附近的<span
    datapos1=cc.find("<span")
    #只保留<span以後的文字
    cc=cc[datapos1:]
    #尋找最附近的>
    datapos1=cc.find(">")
    #尋找最附近的</span> 
    datapos2=cc.find("</span>")
    #如果<span></span>中間出現了enUbOQ，表示這個步驟該結束了 
    if cc[:datapos2].find("enUbOQ")>=0:
      break   
    #如果<span></span>有資料，就合併在data字串裡 
    if datapos1+1<datapos2:
      #但是<span></span>的資料，如果還有span就不行了
      if cc[datapos1+1:datapos2].find("span")<0:       
        data=data+cc[datapos1+1:datapos2]+"\n" 
    #只保留</span>之後的文字    
    cc=cc[datapos2+7:]
  #後三個是熱門留言
  if j<3:
    data=data+"\n*******熱門留言"+str(j+1)+":\n"  
print(data)

print("------------------------------------------------------------")  # 60個

print('chap7-02f')

import requests
import json

postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data=res.json() #方法2
#查看有哪些欄位
print(data.keys())
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#查看有哪些內容
print(df)

print("------------------------------------------------------------")  # 60個

print('chap7-02g')

import requests
import json

postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data=res.json() #方法2
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#取出title、content內容
print(">>>>>文章標題")
print(df.loc["title",0])
print()
print(">>>>>原Po文章")
print(str(df.loc["content",0]).strip())
print("------------------------------------------------------------")  # 60個

print('chap7-02h')

import requests
import json
from datetime import datetime

postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#取出title、content內容
print(">>>>>文章標題")
print(df[0]["title"])
print()
print(">>>>>原Po文章\n")
print(str(df[0]["content"]).strip())
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid+'/comments?popular=True'
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為有欄位名稱
#只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
#取出前3筆資料
for i in range(3):
  print("*******熱門留言"+str(i)+":")
  print(df.loc[i,"content"])
  #將最後修改文字日期轉換成日期  
  updatedate=datetime.fromisoformat(str(df.loc[i,"updatedAt"]).replace("Z",""))
  #計算現在和最後修改日期的時間差
  datediff=datetime.today()-updatedate
  #顯示幾天前有最新留言
  print(datediff.days,"天前")
  print()
#若要查看有哪些欄位
print((df.keys()))
#也可以透過df.info()查看
df.info()
#也可以直接看前幾列
df.head(3)

print("------------------------------------------------------------")  # 60個

print('chap7-02i')

import requests
import json
from datetime import datetime

postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#取出title、content內容
print(">>>>>文章標題")
print(df[0]["title"])
print()
print(">>>>>原Po文章\n")
print(str(df[0]["content"]).strip())
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid+'/comments'
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為有欄位名稱
#只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
#除了updatedAt, content, likeCount三個欄位以外，全部刪除
#刪除欄依定要指定axis=1 
#inplace=True真實刪除
df.drop(['id', 'anonymous', 'postId', 'createdAt', 'floor',
    'withNickname', 'hiddenByAuthor', 'meta',
    'gender', 'school', 'host', 'reportReason', 'mediaMeta', 'hidden',
    'inReview', 'reportReasonText', 'isSuspiciousAccount', 'isModerator',
    'doorplate', 'edited', 'postAvatar', 'activityAvatar', 'verifiedBadge',
    'memberType', 'enablePrivateMessage', 'department'],inplace=True,axis=1)
#依據likeCout內容排序，以降序排列
df.sort_values(by='likeCount', inplace=True, ascending=False)
#要記得重設index，這樣df.loc[]的結果才會正確
df = df.reset_index(drop=True)
#取出前3筆資料
for i in range(3):
  print("*******熱門留言"+str(i)+":")
  print(df.loc[i,"content"])
  #將最後修改文字日期轉換成日期  
  updatedate=datetime.fromisoformat(str(df.loc[i,"updatedAt"]).replace("Z",""))
  #計算現在和最後修改日期的時間差
  datediff=datetime.today()-updatedate
  #顯示幾天前有最新留言
  print(datediff.days,"天前")
  print()
#若要查看有哪些欄位
print((df.keys()))
#也可以透過df.info()查看
df.info()
#也可以直接看前幾列
df.head(3)

print("------------------------------------------------------------")  # 60個

print('chap7-02j')

import requests
import csv
#from io import StringIO

county="屏東縣"
url = 'https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=keykeykey&sort=ImportDate%20desc&format=csv'
#方法1:下載檔案後儲存，再開啟檔案讀出
#res = requests.get(url)
#open('data.csv','wb').write(res.content)
#df=pd.read_csv('data.csv')
#方法2:直接讀取網站的檔案
df=pd.read_csv(url)
#查看有那些欄位
df.info()
#只保留SiteName、County、AQI、Status四個欄位
df.drop(['SiteId','Longitude','Latitude','PublishTime','SO2_AVG', 'Pollutant', 'SO2', 'CO', 'NO', 'CO_8hr', 'O3', 'O3_8hr', 'PM10', 'PM10_AVG', 'PM2.5', 'PM2.5_AVG', 'NO2', 'NOx', 'WindSpeed', 'WindDirec'],inplace=True,axis=1)
#設定過濾條件
indexNames=df[df['County']!=county].index
#刪除所有不是臺北市的偵測站
df.drop(indexNames,inplace=True)
#重設索引值
df=df.reset_index(drop=True)
#列出該縣市所有偵測站狀態
print(county,"空氣品質狀態")
for i in range(len(df)):
  print(df.loc[i,'SiteName'],'(',df.loc[i,'Status'],")")
indexNames=df[df['Status']=='良好'].index
df.drop(indexNames,inplace=True)
#重設索引值
df=df.reset_index(drop=True)
#列出該縣市所有為達良好之偵測站
print()
print(county,"空氣品質未達良好之偵測站")
for i in range(len(df)):
  print(df.loc[i,'SiteName'],'(',df.loc[i,'Status'],")")

print("------------------------------------------------------------")  # 60個

#chap9-01b
import requests
import json

url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data=res.json() #方法2
#因為有欄位名稱
#只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
#轉換'確定病例數'欄位內容為整數(以利後面加總)
df['確定病例數'] = df['確定病例數'].astype(int)

startdate='2021/07/20'
#startdate=input("請輸日期(yyyy/mm/dd)")
#只保留個案研判日、是否為境外移入、確定病例數 三個欄位
df.drop(['確定病名','縣市','鄉鎮','性別','年齡層'],inplace=True,axis=1)
#設定過濾條件(累積)
indexNames=df[df['個案研判日']>startdate].index
#刪除所有大於指定日期的個案
df.drop(indexNames,inplace=True)
#計算累積確診人數
total=df.sum()['確定病例數']
print("累積確診人數:",total)
#設定過濾條件(今日)
indexNames=df[df['個案研判日']!=startdate].index
#刪除所有不是指定日期的個案
df.drop(indexNames,inplace=True)
#計算境外移入人數
imported=df[df['是否為境外移入']=='是'].sum()['確定病例數']
print("今日境外移入人數:",imported)
#計算本土人數
domestic=df[df['是否為境外移入']=='否'].sum()['確定病例數']
print("今日本土人數:",domestic)
total=imported+domestic
print("今日總人數:",total)
#若要查看有哪些欄位
print((df.keys()))
#也可以透過df.info()查看
df.info()
#也可以直接看前幾列
df.head(3)

print("------------------------------------------------------------")  # 60個

#chap9-01c
import requests
import csv
#from io import StringIO

url = 'https://od.cdc.gov.tw/eic/covid19/covid19_tw_stats.csv'
#方法1:下載檔案後儲存，再開啟檔案讀出
#res = requests.get(url)
#open('data.csv','wb').write(res.content)
#df=pd.read_csv('data.csv')
#方法2:直接讀取網站的檔案
df=pd.read_csv(url)
#查看有那些欄位
df.info()
#只保留確診、死亡、送驗、排除四個欄位
df.drop(['昨日確診','昨日排除','昨日送驗'],inplace=True,axis=1)
print(df)
totaldeath=df.loc[0,'死亡']
print("累積死亡人數",totaldeath)

print("------------------------------------------------------------")  # 60個

#chap9-01d
import requests
import json
import csv
from docx import Document

url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'
res = requests.get(url)
data=res.json()
#因為有欄位名稱
#只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
#轉換'確定病例數'欄位內容為整數(以利後面加總)
df['確定病例數'] = df['確定病例數'].astype(int)
startdate='2021/07/20'
startdate=input("請輸日期(yyyy/mm/dd)")
#只保留個案研判日、是否為境外移入、確定病例數 三個欄位
df.drop(['確定病名','縣市','鄉鎮','性別','年齡層'],inplace=True,axis=1)
#設定過濾條件(累積)
indexNames=df[df['個案研判日']>startdate].index
#刪除所有大於指定日期的個案
df.drop(indexNames,inplace=True)
#計算累積確診人數
total=df.sum()['確定病例數']
print("累積確診人數:",total)
#設定過濾條件(今日)
indexNames=df[df['個案研判日']!=startdate].index
#刪除所有不是指定日期的個案
df.drop(indexNames,inplace=True)
#計算境外移入人數
imported=df[df['是否為境外移入']=='是'].sum()['確定病例數']
print("今日境外移入人數:",imported)
#計算本土人數
domestic=df[df['是否為境外移入']=='否'].sum()['確定病例數']
print("今日本土人數:",domestic)
print("今日總人數:",domestic+imported)

url = 'https://od.cdc.gov.tw/eic/covid19/covid19_tw_stats.csv'
df=pd.read_csv(url)
#只保留確診、死亡、送驗、排除四個欄位
df.drop(['昨日確診','昨日排除','昨日送驗'],inplace=True,axis=1)
totaldeath=df.loc[0,'死亡']
print("累積死亡人數",totaldeath)

#切換至指定的資料夾為工作資料夾
os.chdir('/content/drive/MyDrive/Book')
#開啟指定的Word檔案
my_doc = Document("指揮中心快訊.docx")
#設定要取代的串列list
replacements = {
    '%Date%': startdate,
    '%N1%': str(domestic+imported),
    '%N2%': str(domestic),
    '%N3%': str(imported),
    '%N4%': str(totaldeath),
    '%N5%': str(total)
    }
#尋找要取代的關鍵字
for key in replacements:
  #尋找所有的表格
  for table in my_doc.tables:
    #尋找表格中的列
    for row in table.rows:
      #尋找列中的每個儲存格
      for cell in row.cells:
        #尋找儲存格中的每一個斷落
        for paragraph in cell.paragraphs:
          #如果關鍵字出現在段落中
          if key in paragraph.text:
            #為了避免修改掉原有的樣式，必須用這個方法處理
            inline = paragraph.runs            
            for i in range(len(inline)):
              if key in inline[i].text:
                text = inline[i].text.replace(key, replacements[key])
                inline[i].text = text
#指定儲存的檔案名稱         
fname="指揮中心快訊"+startdate.replace("/","")+".docx"
#儲存檔案
my_doc.save(fname)

"""
請輸日期(yyyy/mm/dd)2021/07/20

累積確診人數: 15450

今日境外移入人數: 6

今日本土人數: 18

今日總人數: 24

累積死亡人數 846
"""

print("------------------------------------------------------------")  # 60個

import matplotlib
print(matplotlib.__version__)

print("------------------------------------------------------------")  # 60個

try:
    # 嘗試打開一個不存在的檔案
    with open("non_existent_file.txt", "r") as f:
        data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    # 如果文件不存在, 捕獲異常
    print("The file was not found")
except IOError:
    # 處理 I/O 錯誤, 例如:讀取錯誤
    print("An I/O error occurred")

print("------------------------------------------------------------")  # 60個

filename = "data15_4.txt"
try:
    with open(filename) as f:  # 預設mode=r開啟檔案
        data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    print(f"找不到 {filename} 檔案")
else:
    print(data)  # 輸出變數data


print("------------------------------------------------------------")  # 60個


set99 = set()
for i in range(2, 9 + 1):
    set99.add(i)

print(type(set99))
print(set99)



print("------------------------------------------------------------")  # 60個

import os
pName = 'C:/pcYah'
if os.path.isdir(pName):           # 檢查資料夾路徑是否存在
    print('%s 資料夾路徑存在' %pName)
else:
    print('%s 資料夾路徑不存在' %pName)
     
fName = 'C:/Windows/win.ini'
if os.path.isfile(fName):         # 檢查檔案路徑是否存在
    print('%s 檔案路徑存在' %fName)
else:
    print('%s 檔案路徑不存在' %fName)

"""

isdir  isfile

if os.path.exists(pName):        # 檢查資料夾路徑是否存在
if os.path.exists(fName):        # 檢查檔案路徑是否存在


"""



#try-catch-finally
n1 = 8
n2 = 0
try:
    d = n1/n2
    print('%d / %d = %d' %(n1, n2, d))
except Exception as e:
    print('錯誤類型 :', end =' ')
    print(e)
finally:
    print('執行 finally: 敘述\n')





print('------------------------------------------------------------')	#60個



lst = [0 for x in range(4)]
try:
    lst[3] = 33
    print('lst[3] =', lst[3])
    lst[8] = 88
    print('lst[8] =', lst[8])
except ZeroDivisionError: 
    print('錯誤類型 : 除數為零')
except IndexError: 
    print('錯誤類型 : 串列註標超出範圍')
except MemoryErroe: 
    print('錯誤類型 : 超出記憶體空間')  
except Exception as e:
    print('錯誤類型 :', e) 

import os
fName = 'score.txt'
if os.path.isfile(fName):
    f = open(fName, 'r')
    print('讀1行')
    str1 = f.readline()
    print(str1)
    print('讀4行')
    str2 = f.readline(4)
    print(str2)
    print('剩下的讀完')
    print(f.read())
    f.close()
else:
    print(None)


print("------------------------------------------------------------")  # 60個

# ord(x) 可以將參數x所代表的Unicode字元，轉換為對應編碼數字
A = ord('A')
B = ord('B')
C = ord('C')

print(A)
print(B)
print(C)

# chr(x) 可以將參數x轉換為所代表的Unicode字元
AA = chr(A)
BB = chr(B)
CC = chr(C)

print(AA)
print(BB)
print(CC)
'''
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個




