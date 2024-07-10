"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個


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

'''
print("------------------------------------------------------------")  # 60個

#chap9-01b
import requests
import json
import pandas as pd

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



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
