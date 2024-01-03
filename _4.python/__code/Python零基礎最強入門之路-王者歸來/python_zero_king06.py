import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

num1 = [1, 3, 5]
num2 = [2, 4, 6]
num3 = num1 + num2           # 字串為主的串列相加
print(num3)

print("------------------------------------------------------------")  # 60個

cars = ['toyota', 'nissan', 'honda']
nums = [1, 3, 5]
carslist = cars * 3           # 串列乘以數字
print(carslist)
numslist = nums * 5           # 串列乘以數字
print(numslist)   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_13.py

# ch6_13.py
James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
Love = ['Kevin Love',20, 18, 30, 22, 15]    # 定義Love串列
game3 = James[4] + Love[4]
LKgame = James[0] + ' 和 ' +  Love[0] + '第四場總得分 = ' 
print(LKgame, game3)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_14.py

# ch6_14.py
warriors = ['Curry', 'Durant', 'Iquodala', 'Bell', 'Thompson']
print("2018年初NBA勇士隊主將陣容", warriors)
del warriors[3]                 # 不明原因離隊
print("2018年末NBA勇士隊主將陣容", warriors)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_15.py

# ch6_15.py
nums1 = [1, 3, 5]
print("刪除nums1串列索引1元素前   = ",nums1)
del nums1[1]
print("刪除nums1串列索引1元素後   = ",nums1)
nums2 = [1, 2, 3, 4, 5, 6]
print("刪除nums2串列索引[0:2]前   = ",nums2)
del nums2[0:2]
print("刪除nums2串列索引[0:2]後   = ",nums2)
nums3 = [1, 2, 3, 4, 5, 6]
print("刪除nums3串列索引[0:6:2]前 = ",nums3)
del nums3[0:6:2]
print("刪除nums3串列索引[0:6:2]後 = ",nums3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_16.py

# ch6_16.py
cars = ['Toyota', 'Nissan', 'Honda']
print("cars串列長度是 = %d" %  len(cars))
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print("cars串列長度是 = %d" % len(cars))
else:
    print("cars串列內沒有元素資料")
nums = []
print("nums串列長度是 = %d" % len(nums))
if len(nums) != 0:
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_17.py

# ch6_17.py
strN = "DeepStone"
strU = strN.upper( )           # 改成大寫
strL = strN.lower( )           # 改成小寫
strT = strN.title( )           # 改成第一個字母大寫其他小寫
print("大寫輸出:",strU,"\n小寫輸出:",strL,"\n第一字母大寫:",strT)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_18.py

# ch6_18.py
strN = " DeepStone "
strL = strN.lstrip( )       # 刪除字串左邊多餘空白
strR = strN.rstrip( )       # 刪除字串右邊多餘空白
strB = strN.lstrip( )       # 先刪除字串左邊多餘空白
strB = strB.rstrip( )       # 再刪除字串右邊多餘空白
strO = strN.strip( )        # 一次刪除頭尾端多餘空白
print("/%s/" % strN)
print("/%s/" % strL)
print("/%s/" % strR)
print("/%s/" % strB)
print("/%s/" % strO)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_19.py

# ch6_19.py
cars = ['bmw', 'benz', 'audi']     
carF = "我開的第一部車是 " + cars[1].title( )
carN = "我現在開的車子是 " + cars[0].upper( )
print(carF)
print(carN)

print("------------------------------------------------------------")  # 60個

cars = ['Honda','Toyota','Ford']     
print("目前串列內容 = ",cars)
print("在索引1位置插入Nissan")
cars.insert(1,'Nissan')
print("新的串列內容 = ",cars)
print("在索引0位置插入BMW")
cars.insert(0,'BMW')
print("最新串列內容 = ",cars)

print("------------------------------------------------------------")  # 60個

cars = ['Honda','Toyota','Ford','BMW']     
print("目前串列內容 = ",cars)
print("使用pop( )刪除串列元素")
popped_car = cars.pop( )          # 刪除串列末端值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)          # 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_car)
print("新的串列內容 = ",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_23.py

# ch6_23.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
print("使用remove( )刪除串列元素")
expensive = 'bmw'
cars.remove(expensive)            # 刪除第一次出現的元素bmw
print("所刪除的內容是: " + expensive.upper( ) + " 因為太貴了" )
print("新的串列內容",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_24.py

# ch6_24.py
cars = ['Honda','bmw','Toyota','Ford','bmw']     
print("目前串列內容 = ",cars)
# 直接列印cars[::-1]顛倒排序,不更改串列內容
print("列印使用[::-1]顛倒排序\n", cars[::-1])
# 更改串列內容
print("使用reverse( )顛倒排序串列元素")
cars.reverse( )            # 顛倒排序串列
print("新的串列內容 = ",cars)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_25.py

# ch6_25.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由小排到大")
cars.sort( )            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由小排到大")
nums.sort( )            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_26.py

# ch6_26.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由大排到小")
cars.sort(reverse=True)            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由大排到小")
nums.sort(reverse=True)            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_27.py

# ch6_27.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列car內容 = ",cars)
print("使用sorted( )由小排到大")
cars_sorted = sorted(cars)            
print("排序串列結果 = ",cars_sorted)
print("原先串列car內容 = ",cars)
nums = [5, 3, 9, 2]     
print("目前串列num內容 = ",nums)
print("使用sorted( )由小排到大")
nums_sorted = sorted(nums)            
print("排序串列結果 = ",nums_sorted)
print("原先串列num內容 = ",nums)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_28.py

# ch6_28.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列car內容 = ",cars)
print("使用sorted( )由大排到小")
cars_sorted = sorted(cars,reverse=True)            
print("排序串列結果    = ",cars_sorted)
print("原先串列car內容 = ",cars)
nums = [5, 3, 9, 2]     
print("目前串列num內容 = ",nums)
print("使用sorted( )由大排到小")
nums_sorted = sorted(nums,reverse=True)            
print("排序串列結果    = ",nums_sorted)
print("原先串列num內容 = ",nums)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_29.py

# ch6_29.py
cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
i = cars.index(search_str)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_str, i))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_val, j))


print("------------------------------------------------------------")  # 60個

James = ['Lebron James',23, 19, 22, 31, 18] # 定義James串列
games = len(James)                          # 求元素數量
score_Max = max(James[1:games])             # 最高得分
i = James.index(score_Max)                  # 場次
print(James[0], "在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

cars = ['toyota', 'nissan', 'honda']
search_str = 'nissan'
num1 = cars.count(search_str)
print("所搜尋元素 %s 出現 %d 次" % (search_str, num1))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素 %s 出現 %d 次" % (search_val, num2))


print("------------------------------------------------------------")  # 60個

char = '-'
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))
char ='***'
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))
char = '\n'             # 換行字元
lst = ['Silicon', 'Stone', 'Education']
print(char.join(lst))

print("------------------------------------------------------------")  # 60個

James = [['Lebron James','SF','12/30/84'],23,19,22,31,18] # 定義James串列
games = len(James)                                        # 求元素數量
score_Max = max(James[1:games])                           # 最高得分
i = James.index(score_Max)                                # 場次
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名     : ", name)
print("位置     : ", position)
print("出生日期 : ", born)
print("在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.append(cars2)
print("執行append( )後串列cars1內容 = ", cars1)
print("執行append( )後串列cars2內容 = ", cars2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_34.py

# ch6_34.py
cars1 = ['toyota', 'nissan', 'honda']
cars2 = ['ford', 'audi']
print("原先cars1串列內容 = ", cars1)
print("原先cars2串列內容 = ", cars2)
cars1.extend(cars2)
print("執行extend( )後串列cars1內容 = ", cars1)
print("執行extend( )後串列cars2內容 = ", cars2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_35.py

# ch6_35.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_36.py

# ch6_36.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)
                   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_37.py

# ch6_37.py
mysports = ['basketball', 'baseball']
friendsports = mysports
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

mysports = ['basketball', 'baseball']
friendsports = mysports[:]
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)
mysports.append('football')
friendsports.append('soccer')
print(" -- 新增運動項目後 -- ")
print("列出mysports位址     = ", id(mysports))
print("列出friendsports位址 = ", id(friendsports))
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個

string = "Python"
# 正值索引
print(" string[0] = ", string[0],
      "\n string[1] = ", string[1],
      "\n string[2] = ", string[2],
      "\n string[3] = ", string[3],
      "\n string[4] = ", string[4],
      "\n string[5] = ", string[5])
# 負值索引
print(" string[-1] = ", string[-1],
      "\n string[-2] = ", string[-2],
      "\n string[-3] = ", string[-3],
      "\n string[-4] = ", string[-4],
      "\n string[-5] = ", string[-5],
      "\n string[-6] = ", string[-6])
# 多重指定觀念
s1, s2, s3, s4, s5, s6 = string
print("多重指定觀念的輸出測試 = ",s1,s2,s3,s4,s5,s6)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_40.py

# ch6_40.py
string = "Deep Learning"                # 定義字串
print("列印string第1-3元素     = ", string[0:3])
print("列印string第2-4元素     = ", string[1:4])
print("列印string第2,4,6元素   = ", string[1:6:2])
print("列印string第1到最後元素 = ", string[1:])
print("列印string前3元素       = ", string[0:3])
print("列印string後3元素       = ", string[-3:])

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41.py

# ch6_41.py
string = "Deep Learning"                # 定義字串
strlen = len(string)
print("字串長度", strlen)
maxstr = max(string)
print("字串最大的unicode碼值和字元", ord(maxstr), maxstr)
minstr = min(string)
print("字串最小的unicode碼值和字元", ord(minstr), minstr)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41_1.py

# ch6_41_1.py
str1 = "Silicon Stone Education"
str2 = "DeepStone"
str3 = "深石數位"

sList1 = str1.split()                       # 字串轉成串列
sList2 = str2.split()                       # 字串轉成串列
sList3 = str3.split()                       # 字串轉成串列
print(str1, " 串列內容是 ", sList1)         # 列印串列
print(str1, " 串列字數是 ", len(sList1))    # 列印字數
print(str2, " 串列內容是 ", sList2)         # 列印串列
print(str2, " 串列字數是 ", len(sList2))    # 列印字數
print(str3, " 串列內容是 ", sList3)         # 列印串列
print(str3, " 串列字數是 ", len(sList3))    # 列印字數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_41_2.py

# ch6_41_2.py
msg = '''CIA Mark told CIA Linda that the secret USB
had given to CIA Peter'''
print("字串開頭是CIA: ", msg.startswith("CIA"))
print("字串結尾是CIA: ", msg.endswith("CIA"))
print("CIA出現的次數: ",msg.count("CIA"))

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = 20
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))
r = x                               # r的值將變為10
print("x = %d, y = %d, z = %d, r = %d" % (x, y, z, r))
print("x位址 = %d, y位址 = %d, z位址 = %d, r位址 = %d"
      % (id(x), id(y), id(z), id(r)))

print("------------------------------------------------------------")  # 60個

x = 10
y = 10
z = 15
r = z - 5
boolean_value = x is y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

boolean_value = x is not y
print("x位址 = %d, y位址 = %d" % (id(x), id(y)))
print("x = %d, y = %d, " % (x, y), boolean_value)

boolean_value = x is not z
print("x位址 = %d, z位址 = %d" % (id(x), id(z)))
print("x = %d, z = %d, " % (x, z), boolean_value)

boolean_value = x is not r
print("x位址 = %d, r位址 = %d" % (id(x), id(r)))
print("x = %d, r = %d, " % (x, r), boolean_value)

print("------------------------------------------------------------")  # 60個

mysports = ['basketball', 'baseball']
sports1 = mysports          # 拷貝位址
sports2 = mysports[:]       # 拷貝新串列
print("我喜歡的運動 = ", mysports, "位址是 = ", id(mysports))
print("運動 1       = ", sports1,  "位址是 = ", id(sports1))
print("運動 2       = ", sports2,  "位址是 = ", id(sports2))
boolean_value = mysports is sports1
print("我喜歡的運動 is 運動 1     = ", boolean_value)

boolean_value = mysports is sports2
print("我喜歡的運動 is 運動 2     = ", boolean_value)

boolean_value = mysports is not sports1
print("我喜歡的運動 is not 運動 1 = ", boolean_value)

boolean_value = mysports is not sports2
print("我喜歡的運動 is not 運動 2 = ", boolean_value)

print("------------------------------------------------------------")  # 60個

drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)        # 數值初始是0
print(enumerate_drinks)                     # 傳回enumerate物件所在記憶體
print("下列是輸出enumerate物件類型")
print(type(enumerate_drinks))               # 列出物件類型

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch6\ch6_48.py

# ch6_48.py
drinks = ["coffee", "tea", "wine"]
enumerate_drinks = enumerate(drinks)                # 數值初始是0
print("轉成串列輸出, 初始值是 0 = ", list(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start = 10)    # 數值初始是10
print("轉成串列輸出, 初始值是10 = ", list(enumerate_drinks))










          



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
