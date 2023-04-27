# 各種python專用的語法 字典

adict = {'book':10, 'pen':3, 'earser':6, 'ruler':2}
print('打印字典的內容1')
for key, value in adict.items():
    if value < 5:
      print("({},{})".format(key, value))
print('打印字典的內容2')
print(adict)


#字典(dictionary)的資料型態
mydict = {'a':3, 'b':2, 'c':5}
print(mydict['a'])
mydict['d'] = 7
print(mydict)

# 星座轉換字典
zodiacSigns_convent = {
    '1':'Aries',
    '2':'Taurus',
    '3':'Gemini',
    '4':'Cancer',
    '5':'Leo',
    '6':'Virgo',
    '7':'Libra',
    '8':'Scorpio',
    '9':'Sagittarius',
    '10':'Capricorn',
    '11':'Aquarius',
    '12':'Pisces'
}
index = 7
print(zodiacSigns_convent[str(index)])

print("字典測試 1")

dict1 ={
    "david":85,
    "lion":93,
    "mouse":67
    }

#name = input("輸入學生姓名：")
name = 'david'
if name in dict1:  
    print(name + "的成績為 " + str(dict1[name]))
else:  
    score = input("輸入學生分數：")
    dict1[name] = score
    print("字典內容：" + str(dict1))
    
    
print("字典測試 2")
#item
dict1={"金牌":26, "銀牌":34, "銅牌":30}
item1 = list(dict1.items())
for name, num in item1:
    print("得到的 %s 數目為 %d 面" % (name, num))


print("字典測試 3")
#key-value
dict1={"金牌":26, "銀牌":34, "銅牌":30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))


print("字典測試 4")
dict1 = {"A":"內向穩重", "B":"外向樂觀", "O":"堅強自信", "AB":"聰明自然"}
#name = input("輸入要查詢的血型:")
name = 'O'
blood = dict1.get(name)
if blood == None:  
    print("沒有「" + name + "」血型！")
else:  
    print(name + " 血型的個性為：" + str(dict1[name]))
    



import time

new_users = [
{'name': 'Richard Ho'},
{'name': 'Tom Wu'},
{'name': 'Judy Chen'},
{'name': 'Lisa Chang'}
]

for user in new_users:
    print('/user', user)
    time.sleep(0.1)


#讀取檔案字典範例

print("將 字典 寫入檔案")
filename = 'C:/______test_files3/sssssss3.txt'

scores=dict()

scores[1] = 30
scores[2] = 50
scores[3] = 80
scores[4] = 90
scores[5] = 100

with open(filename,'w') as fp:
    fp.write(str(scores))
    
print("寫入檔案 : " + filename)

print('dict使用範例')

class_101 = dict() #記錄學生座號及姓名
chi_score = dict() #記錄國文成績
eng_score = dict() #記錄英文成績
mat_score = dict() #記錄數學成績

subjects = ["國文", "英文", "數學"]
scores  = [chi_score, eng_score, mat_score]

class_101[1] = 'apple'
class_101[2] = 'banana'
class_101[4] = 'cat'
class_101[8] = 'dog'
print(class_101)

print('輸入國文成績')
subject_no = 0
no = 1
scores[subject_no][no] = 80
no = 2
scores[subject_no][no] = 85
no = 4
scores[subject_no][no] = 78
no = 8
scores[subject_no][no] = 88

print('顯示國文成績')
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print('輸入英文成績')
subject_no = 1
no = 1
scores[subject_no][no] = 84
no = 2
scores[subject_no][no] = 79
no = 4
scores[subject_no][no] = 92
no = 8
scores[subject_no][no] = 82

print('顯示英文成績')
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print('輸入數學成績')
subject_no = 2
no = 1
scores[subject_no][no] = 85
no = 2
scores[subject_no][no] = 91
no = 4
scores[subject_no][no] = 84
no = 8
scores[subject_no][no] = 77

print('顯示數學成績')
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print('顯示總成績')
for no in class_101.keys():
    print("{:<5}:".format(class_101[no]), end="")
    sum = 0
    for subject_no in range(0,3):
        sum = sum + scores[subject_no][no]
        print("{}:{:>3} ".format(subjects[subject_no], scores[subject_no][no]), end="")
    print("總分:{:>3}, 平均:{:.2f}".format(sum, float(sum)/len(scores)))


print('dict使用範例')


'''
Dictionary(字典)

Dictionary是無序、沒有索引值且沒有重複的成員的容器，Pair的語法是key: value，一個key對應一個value，key不一定要是字串，但必須是唯一的。
'''

Number = {"five": 5, "ten": 10, "three": 3}
print(Number)		#打印dictionary

#語法是dict[key]，利用key來存取數量。dict[key] = value就可以改變數量。

print(Number["five"])	#5
Number["five"] = 50	#50
print(Number)		#打印dictionary

#增加dictionary
#只要給新的key就會產生新的資料。
Number["eight"] = 8
print(Number)		#打印dictionary




#移除dictionary
#使用pop(key)移除該key值的資料。
Number.pop("eight")
print(Number)		#打印dictionary


#取得所有資料
#使用keys()取得所有key值，回傳是所有key的List。
#取得所有數字
#使用values()取得所有value值，回傳是所有value的List。
#取得所有資料
#使用item()取得所有資料組，回傳是由(key, value)所組成的List。

print(Number.keys())
print(Number.values())
print(Number.items())








