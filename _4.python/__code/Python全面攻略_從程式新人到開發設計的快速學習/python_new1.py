


#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch01\add.py

print (100 + 50)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch01\hello.py

print ('Hello World !')    # 輸出字串內容
print (100 + 50)           # 輸出計算結果

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\assign.py

x = 10	     # 指定常值10給x變數
y = x		 # 指定x變數值給y變數
x = y + 5	 # 指定運算式y+5的結果給x變數
print(x, y)  # 輸出x和y的變數值,分別為15 10



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\auto.py

b = False     # 布林型別
i = 5         # 整數型別
f = 1.2       # 浮點數型別
print(b + i)  # 顥示5,因b=False會自動轉型為0，使為0+5
print(i + f)  # 顯示6.2,因i=5會自動轉型為5.0,使為5.0+1.2
print(b * i)  # 顥示0,因b=False會自動轉型為0，使為0*5
print(i * f)  # 顯示6.0,因i=5會自動轉型為5.0,使為5.0*1.2

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\boolean.py

tf1 = (10 > 5)   # (10>5)是結果為True的條件式,tf1變數屬布林資料型別
print(tf1)       # 輸出tf1變數的內容為布林值True
tf2 = (10 < 5)   # (10<5)是結果為False的條件式,tf2變數屬布林資料型別
print(tf2)       # 輸出tf2變數的內容為布林值False

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\cast.py

i1 = int(3.64)      # 浮點數轉型為整數3,再指定給變數i1
i2 = round(3.64)    # 浮點數四捨五入後轉型為整數4,再指定給變數i2
f = float(100)      # 整數轉型為浮點數100.0,再指定給變數f
print(i1, i2, f)    # 顯示 3 100.0
s = str(12.3)       # 數值轉型為字串'12.3',再指定給變數s
print(s, type(s))   # 顯示 12.3 <class 'str'>
b = bool('123')     # 非0數值資料轉型為布林資料True,再指定給變數b
print(b, type(b))   # 顯示 True <class 'bool'>

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\cast2.py

s1 = '100'				# 文數字字串
s2 = '3.14' 				# 文數字字串
i1 = int(s1)				# 文數字'100'轉型為整數100,指定給i1變數
f1 = float(s2) 	# 文數字'3.14'轉型為浮點數3.14,指定給f1變數
print(i1, f1)				# 顯示 100 3.14
print(type(i1), type(f1))  # 顯示 <class 'int'> <class 'float'>
i2 = int(float(s2)) # 文數字'3.14'先轉型為浮點數3.14,再轉型為變數3
f2 = float(s1) 	 # 文數字'100'轉型為浮點數100.0,指定給f2變數
print(i2, f2)				 # 顯示 3 100.0
print(type(i2), type(f2))  # 顯示 <class 'int'> <class 'float'>
n1 = eval(s1)         # 文數字'100'轉型為整數100,指定給n1變數
n2 = eval(s2) 			 # 文數字'3.14'轉型為浮點數3.14,指定給n2變數
print(n1, n2)				 # 顯示 100 3.14
print(type(n1), type(n2)) # 顯示 <class 'int'> <class 'float'>

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\float.py

print(543.21)     #顯示浮點數常值 543.21
print(5.4321e2)   #顯示浮點數常值 543.21
print(5.4321e6)   #顯示浮點數常值 5432100.0
print(5.4321e-3)  #顯示浮點數常值 0.0054321

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\format01.py

name = '李金星'          # 宣告字串變數name，初值設為'李金星'
score = 73               # 宣告整數變數score，初值設為73

msg = '{}的成績是{}分'.format(name, score)
                                   	
# msg字串內容為 '李金星的成績是73分'

print(msg)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\format02.py

name = '李金星'          # 宣告字串變數name，初值設為'李金星'
score = 73               # 宣告整數變數score，初值設為73

msg = '{0}的成績是{1}分'.format(name, score)
                                   	
# msg字串內容為 '李金星的成績是73分'

print(msg)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\format03.py

# 宣告整數變數price為100，整數變數qty為30
price = 100
qty = 30
# 印出資料後游標往下移一行
print('單價：{0}     數量：{1}'.format(price, qty))
print('打八折後,總金額：{0}'.format(price * qty * 0.8))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\input01.py

name = input('輸入姓名 : ')
score = input('輸入分數 : ')
print('{0}的成績是{1}分'.format(name, score))
# 輸出結果為「李金星的成績是73」

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\input02.py

name = input('輸入姓名 : ')         	# 輸入字串「李金星」指定給name變數
score = eval(input('輸入分數 : '))	# 輸入字串「73」,先轉型為數值,
                                   	# 再指定給score數值變數
print('%s的成績是%d分' %(name, score))
# 輸出結果為「李金星的成績是73分」

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\int.py

print(11)     	# 以十進制顯示整數常值11
print(0b1011) 	# 以二進制顯示整數常值11
print(0o13) 		# 以八進制顯示整數常值11
print(0xB)			# 以十六進制顯示整數常值11

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print01.py

print('fruit',2020)                  	# 顯示字串和整數常值
print('香蕉','鳯梨','芭樂',sep='&')	# 分隔字元設為'&'
print('項目','功能',sep='\t')        	# 分隔字元設為'\t'
price=620
print('Visual C# 全面攻略',price,'元')	# 顯示price變數
print('請輸入：',end='')         		# 結尾字元串設為空字串

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print02.py

print('%s風景區在%s境內' %('日月潭','南投縣'));
wt=3
price=25
print('%s%d斤，共%d元' %('香蕉', wt, wt*price));

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print03.py

print('%d' %1234)  		# 顯示整數,未設寬度
print('%8d' %1234) 	# 顯示整數,寬度有剩補空格,靠右對齊
print('%8d' %-1234)     # 顯示整數,寬度有剩補空格,靠右對齊
print('%3d' %-1234)     # 顯示整數,寬度不足設定無效

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print04.py

print('%f' %123.456)	# 顯示數值「123.456000」,小數預設6位
print('%f' %-123.456)	# 顯示數值「-123.456000」,小數預設6位
print('%.2f' %123.456)	# 顯示數值「123.46」,小數2位,第3位四捨五入
print('%8.2f' %-12.3456)# 顯示「ΔΔ-12.35」,總寬度8位,小數2位
print('%3.1f' %123.456)	# 顯示「123.5」,寬度不足設定無效,小數位數1位
print('%8.0f' %-123.456)# 顯示數值「ΔΔΔ-1235」,小數第1位四捨五入
print('%8.0f' %123.456)	# 顯示數值「ΔΔΔ1235」,小數第1位四捨五入
print('%g' %12345.6789)	# 顯示數值「12345.7」,總寬度預設7位
print('%g' %1.23456789)	# 顯示數值「1.23457」,總寬度預設7位
print('%g' %12.3)		# 顯示數值「12.3」, 寬度低於預設,直接顯示
print('%g' %123456.789)	# 顯示數值「123457」,最後1位為小數點不顯示
print('%g' %1234567.89)	# 顯示數值「1.23457e+06」,整數7位以上,
                             	# 改用科學記號顯示,指數位數佔2位(不含+-號)
print('%10.3G' %1234.5)	# 顯示「ΔΔ1.23E+03」,寬度10位,E及小數3位


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print05.py

print('%c' %'M')            # 顯示字元「M」
print('%4c' %'M')           # 顯示字元「ΔΔΔM」,靠右對齊,寬度有剩補空格
print('%c' %65)             # 顯示字元「A」,65的ASCII碼為「A」
print('%s' %'ABCDE')        # 顯示字串「ABCDE」
print('%8s' %'ABCDE')       # 顯示字串「ΔΔΔABCDE」
print('%3s' %'ABCDE')       # 顯示字串「ABCDE」,總寬度不足設定無效
print('%6.2s' %'ABCDE')     # 顯示字串「ΔΔΔΔAB」,寬度設為6,顯示2字元


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print06.py

print('%+8d' %12345)        # 顯示「ΔΔ+12345」,靠右對齊,正數值前加「+」號
print('%+8d' %-12345)       # 顯示「ΔΔ-12345」,靠右對齊,負數值前加「-」號
print('%-8d' %12345)        # 顯示「12345ΔΔΔ」,靠左對齊,正數值前不加號
print('%-8d' %-12345)       # 顯示「-12345ΔΔ」,靠左對齊,負數值前加「-」號
print('%+8.2f' %12.345)     # 顯示「ΔΔ+12.35」,靠右對齊,正數值加「+」號
print('%-8.2f' %12.345)     # 顯示「12.35ΔΔΔ」,靠左對齊,正數值不加號
print('%-8.2f' %-12.345)    # 顯示「-12.35ΔΔ」,靠左對齊,負數值加「-」號
print('%-8s' %'ABCDE')      # 顯示字串「ABCDEΔΔΔ」,靠左對齊,寬度有剩補空格
print('%-6.2s' %'ABCDE')    # 顯示字串「ABΔΔΔΔ」,寬度設為6,顯示2個字元

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print07.py

print('1234567890!\a')       # 出現音效聲,游標位置在'!'字元後面
print('12345\b67890!')       # 顯示字串「123467890!」,刪除字元'5'
print('1234567890!\n')       # 顯示字串「123467890!」,游標跳到下一行行首
print('123\r4567890!')       # 游標跳到行首,刪除'123',顯示字串「4567890!」
print('123\t45\\67')         # 顯示字串「123ΔΔΔΔΔ45\67」
print('123\"45\"67')         # 顯示字串「123"45"67」
print('123\'4\'567')         # 顯示字串「123'4'567」
print('ASCII碼41(Hex):\x41') # 顯示字串「ASCII碼41(Hex):A」



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\print08.py

name = '李金星'          # 宣告字串變數name，初值設為'李金星'
score = 73               # 宣告整數變數score，初值設為73
print('{0}的成績是{1}'.format(name, score))
                                   	
# 輸出結果為「李金星的成績是73」


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\sale.py

name = input('輸入品名：')
num = int(input('輸入數量：'))
price = float(input('輸入單價：'))
print()
print('品名\t\t數量\t單價\t金額')
print('=========================================')
print('%-14s%-9d%-9.1f%-9.1f' %(name,num,price,num*price))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\statement01.py

x=10; y=20; z=30
sum = x + \
      y + \
      z
print(sum)          # 顯示10,20,30的和,結果為60

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\statement02.py

x=10; y=20; z=30
sum = (x +          # 用()括起來的內容視為同一個敘述
       y +          
       z)        	   # 這個敘述有三行
print(sum)          # 顯示60

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\str.py

print('H')           # 顯示字元常值 H
print("5.432")       # 顯示字串常值 5.432
print('我愛Python')  # 顯示字串常值 我愛Python
print('"Hi!" says Joe.')  # 顯示字串常值 "Hi!" says Joe.
print("Tom's dog.")    # 顯示字串常值 Tom's dog.

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\strAdd.py

st1 = 'qwer'        # 宣告st1變數，並指定字串常值 qwer為變數值
st2 = '1234'       # 宣告st2變數，並指定文數字 1234為字串變數值
st3 = st1 + st2		  # 將st1與st2兩字串相串連的結果指定給st3字串變數
print(st3)          # 輸出st3變數值，結果為 qwer1234

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch02\swap.py

a = 100	     	
b = 20			   
print(a, b)  	        # 輸出a和b的變數值,分別為100,20
print(id(a), id(b))     # 顯示a和b變數所在的記憶體位址
a, b = b, a             # a,b兩變數的記憶體位址交換
print(a, b)  	        # 輸出a和b的變數值,分別為20,100
print(id(a), id(b))     # 顯示a和b變數所在的記憶體位址

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch03\example.py

# -*- coding: utf-8 -*-
i = int(input("請輸入2020年1月1日是星期幾？"))
print("Sun.\tMon.\tTue.\tWed.\tThu.\tFri.\tSat.")
print("\t" * i, end='')
for x in range(1, 31 + 1):
    print(f"{x}\t", end='')
    if(i < 6):
        i += 1
    else:
        print()
        i = 0

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch03\loop.py

# -*- coding: utf-8 -*-
x = int(input("請輸入小於12的正整數："))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(f"{i * j}\t", end="")
    print()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch03\ph.py

# -*- coding: utf-8 -*-
i = float(input("請輸入PH值："))
if (i < -1 or i > 15):
    print("輸入值異常！！")
else:
    if(i == 7):
        print("中性！！")
    elif (i < 7):
        print("酸性！！")
    else:
        print("鹼性！！")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch03\while.py

# -*- coding: utf-8 -*-
i = 10
while(i > 0):
    print(f"count:{i}")
    i = i - 1
print("時間到")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch04\checkin.py

# -*- coding: utf-8 -*-
tel = []
indata = []
outdata = []
while True:
    s1 = input("請輸入電話號碼：")
    if (s1 in tel):
        idx = tel.index(s1)
        tel.remove(s1)
        lst = indata.pop(idx)
        t1 = input("請輸入離開時間：")
        lst.append(t1)
        lst.append(s1)
        outdata.append(lst)
    else:
        tel.append(s1)
        lst = []
        lst.append(input("請輸入進入時間："))
        lst.append(input("請輸入體温："))
        indata.append(lst)
    ch = input("是否繼續登錄(y/n)？")
    if (ch in "nN"):
        break

if (len(outdata) > 0):
    print(" ---出--入--人--員--記--錄---")
    print("進入時間-體 温-離開時間-電話號碼")
    for item in outdata:
        print(f" {item[0]}  {item[1]}  {item[2]}   {item[3]}")
if (len(indata) > 0):
    print("--館-內-人-員-記-錄---")
    print("進入時間-體 温-電話號碼")
    for i in range (len(indata)):
        print(f" {indata[i][0]}  {indata[i][1]}  {tel[i]}")
        


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch04\dBtest.py

# -*- coding: utf-8 -*-
name = ["東","西","南","北","中"]
data = [43.0, 45.4, 44.8, 47.4, 46.4, 47.5, 
      43.3, 44.1, 45.1, 37.2, 31.7, 37.6, 
      33.3, 31.9, 39.9, 38.2, 32.6, 38.5, 
      41.2, 40.2, 41.0, 32.7, 37.8, 34.7, 
      40.0, 37.9, 38.1, 42.0, 45.5, 41.2, 
      32.2, 39.9, 46.4, 44.5, 46.0, 47.9, 
      37.5, 31.4, 32.6, 42.6, 33.5, 45.4, 
      49.0, 42.7, 39.7]
value = []
i = 0
for x in range(5):
    value.append([])
    for y in range(3):
        lst = data[i : i + 3]
        i = i + 3
        high = max(lst)
        if (high >= 40):
            value[x].append(high)
for x in range(5):
    days = len(value[x])
    if (days == 0):
        print(f"{name[x]}區噪音值正常")
    else:
        for y in value[x]:
            print(y)
        print(f"{name[x]}區噪音值超標{days}天，平均值={sum(value[x])/days}")    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch05\id.py

# -*- coding: utf-8 -*-
dict1 = {}
for i in range(3):
    data = []
    site = input("請輸入平台名稱：")
    data.append(input("請輸入帳號："))
    data.append(input("請輸入密碼："))
    dict1[site] = data
site = input("請輸入要查詢的平台名稱：")
data = dict1.get(site, False)
if data == False:
    print("無此資料!")
else:
    print(f"{site}的帳號：{data[0]}；密碼：{data[1]}")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch05\lotto.py

# -*- coding: utf-8 -*-
from random import randint
rand = set()

while (len(rand) < 7):
    rand.add(randint(1,49))
print ("本期樂透彩號碼：")
for idx,num in enumerate(rand, 1):
    print (f"({idx})={num}", end='  ')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch05\score.py

# -*- coding: utf-8 -*-

data = (("張三", 86, 60),("李四", 93, 55),("王五", 72, 66), ("劉六", 89, 84))

print ("編號    姓名      學科    術科    總分")
for idx, dt in enumerate(data):
    print (f"{idx + 1}\t{dt[0]}\t{dt[1]}\t{dt[2]}\t{dt[1] + dt[2]}")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch06\call.py

# -*- coding: utf-8 -*-
import func

lst1 = [62, 47, 36, 53, 100]
print (f"原始資料={lst1}")
print ("方法一調整後的數值")
for x in range(len(lst1)):
    print(func.func1(lst1[x]), end = '  ')
    
print ()
print ("方法二調整後的數值")
for x in range(len(lst1)):
    print(func.func2(lst1[x]), end = '  ')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch06\checkYear.py

# -*- coding: utf-8 -*-

def checkYear(y):
    if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
        print(f"{y}年是閏年")
    else:
        print(f"{y}年是平年")

year = int(input("請輸入年份:"))
checkYear(year)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch06\compute.py

# -*- coding: utf-8 -*-

def compute(r):
    return (4 / 3 * 3.1416 * r * r * r)

radius = int(input("請輸入球半徑(公分) :"))
volume = compute(radius)
print(f"球半徑 = {radius}公分  球體積 = {volume}立方公分")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch06\func.py

# -*- coding: utf-8 -*-
from math import sqrt

def func1(x):
    r = sqrt(x) * 10
    return(int(r + 0.5))

def func2(x):
    r = x / 2 + 50
    return(round(r))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch06\global.py

# -*- coding: utf-8 -*-

def order(str, num):
    global no
    print (f"菜單編號：{no}  品名：{str} 數量：{num}")
    no += 1

no = 1

while (True):
    s = input("請輸入品名：")
    n = input("請輸入數量：")
    order(s, n)
    i = input("是否繼續輸入？(y/n)")
    if(i in "nN"):
        break
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch06\method.py

# -*- coding: utf-8 -*-
from random import randint

def getRan(i, lstA):
    while (i > 0):
        lstA.append(randint(40, 100))
        i -= 1
    
lst1 = []
i = int(input("請輸入數量："))
getRan(i, lst1)
print(lst1)
print(i)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch06\recursive.py

# -*- coding: utf-8 -*-
def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))
    
i = int(input("請輸入欲顯示到第幾個費波南希係數："))
for x in range(1, i + 1):
    print(f"\t{fib(x)}", end = "")


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



#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\bar1.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='DFKai-SB'

plt.bar(['北部','中部','南部','東部'],[800000,580000,640000,420000])

plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\bar2.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='mingliu'

plt.bar(['北部','中部','南部','東部'],[800000,580000,640000,420000],
width=0.6, color='cm')

plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\bar3.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='mingliu'

areas=['北部','中部','南部','東部']
data1=[800000,580000,640000,420000]
data2=[750000,460000,680000,340000]
plt.bar(areas,data1,label='上半年')
plt.bar(areas,data2,label='下半年',bottom=data1)

plt.legend()
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\bar4.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='mingliu'

areas=['北部','中部','南部','東部']
width=0.4
x1=[x-width/2 for x in range(len(areas))]
x2=[x+width/2 for x in range(len(areas))]
data1=[800000,580000,640000,420000]
data2=[750000,460000,680000,340000]
plt.bar(x1,data1,width,label='上半年')
plt.bar(x2,data2,width,label='下半年')
plt.xticks(range(len(areas)),labels=areas)

plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\pie1.py

import matplotlib.pyplot as plt

plt.pie([40,45,15])

plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\pie2.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='DFKai-SB'

plt.pie([40,45,15],labels=['現金','股票','債券'],autopct='%2.1f%%')
plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\pie3.py

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='DFKai-SB'

datas=[40, 45, 15]
lbls=['現金', '股票', '債券']
exps=[0.2, 0, 0]
clrs=['pink','lightblue','yellow']
plt.pie(datas, labels=lbls, colors=clrs, explode=exps, autopct='%2.1f%%',startangle=0, shadow=True)

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\plot1.py

import matplotlib.pyplot as plt

plt.plot(['A','B','C','D'],[76,85,64,92])
plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\plot2.py

import matplotlib.pyplot as plt

plt.plot(['A','B','C','D'],[76,85,64,92], color='red', ls='--', marker='*', lw=3, ms=20,)
#plt.plot(['A','B','C','D'],[76,85,64,92],'r--*',lw=3,ms=20)#簡寫
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\plot3.py

import matplotlib.pyplot as plt

plt.plot(['A','B','C','D'],[76,85,64,92],label='Math')
plt.legend()    # 使用legend()方法顯示圖例

plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\plot4.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='mingliu'	#指定為明體字

plt.rcParams['font.sans-serif']='mingliu'
plt.plot(['A','B','C','D'],[76,85,64,92])
plt.title('班級成績比較表',fontsize=12)
plt.xlabel('班級')
plt.ylabel('分數')

plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\plot5.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='DFKai-SB'

plt.plot(['A','B','C','D'],[76,85,64,92],label='數學')
plt.plot(['A','B','C','D'],[100,75,84,54],'--',label='英語')
plt.plot([86,90,48,88],'-.',label='電腦')		#X軸資料相同時可省略

plt.legend()    # 使用legend()方法顯示圖例
plt.show()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch10\rndDice.py

import matplotlib.pyplot as plt
import random as rnd

plt.rcParams['font.sans-serif']='mingliu'
dices=['1點','2點','3點','4點','5點','6點']
data=[]
times=[]
for i in range(1000):
    data.append(rnd.randint(1,6))

for i in range(1,7):
    times.append(data.count(i))
    
plt.pie(times,labels=dices,autopct='%2.1f%%',explode=[0.1,0.1,0.1,0.1,0.1,0.1],shadow=True)
plt.title('擲骰子機率圖',fontsize=18)
plt.show()


print("------------------------------------------------------------")  # 60個

