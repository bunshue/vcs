# 各種python專用的語法 字典

import sys

print('------------------------------------------------------------')	#60個

print('字典的操作')

print('------------------------------------------------------------')	#60個

print('建立空字典')
animal = {}
print("空字典", animal)

animal = {
    'mouse':'老鼠',
    'panda':'貓熊',
    'penguin':'企鵝',
    'lion':'獅子',
}

print('增加字典內容')
animal['tiger'] = '老虎'
animal['zebra'] = '斑馬'
animal['koala'] = '無尾熊'
animal['hippo'] = '河馬'

print('刪除字典內容')
del animal['penguin']

print(type(animal))
print(animal)
print(animal['tiger'])
print(animal.keys())
print(animal.values())
print(animal.items())

print('字典裡內容一一列出')
for key in animal:
    print(key + ": " + animal[key])

for ename, cname in animal.items():
    print("{:15s}{:15s}".format(ename, cname))

for ename in animal.keys():
    print(f"{ename},{animal[ename]}")

print('排序再顯示')
for ename in sorted(animal.keys()):
    print(f"{ename},{animal[ename]}")

print('排序 反相 再顯示')
for ename in sorted(animal.keys(),reverse=True):
    print(f"{ename},{animal[ename]}")

print('顯示values')
for cname in animal.values():
    print(cname)

animal_name = 'lion'
if animal_name in animal:
    print('有此動物 :', animal_name, '=>', animal[animal_name])
else:
    print('查無此動物 :', animal_name)

animal_name = 'dinosour'
if animal_name in animal:
    print('有此動物 :', animal_name, '=>', animal[animal_name])
else:
    print('查無此動物 :', animal_name)


print("目前字典元素數量     = ", len(animal))

animal.clear()

print("目前字典內容:", animal)
print("目前字典元素數量     = ", len(animal))


print('------------------------------------------------------------')	#60個

# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}

print(type(sports))
print(sports)

# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items():
          print("%s 喜歡的運動是: " % name)
# 列印value,這是串列
          for sport in favorite_sport:
              print("   ", sport)

print('------------------------------------------------------------')	#60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}
                 }

print(type(wechat_account))
print(wechat_account)

# 列印字典元素個數
print("wechat_account字典元素個數       ", len(wechat_account))
print("wechat_account['cshung']元素個數 ", len(wechat_account['cshung']))
print("wechat_account['kevin']元素個數  ", len(wechat_account['kevin']))

print('------------------------------------------------------------')	#60個

fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print("Value = ", ret_value1)
ret_value2 = fruits.get('Grape')
print("Value = ", ret_value2)
ret_value3 = fruits.get('Grape', 10)
print("Value = ", ret_value3)

print('------------------------------------------------------------')	#60個

# key在字典內
fruits = {'Apple':20, 'Orange':25}
ret_value = fruits.setdefault('Orange')
print("Value = ", ret_value)
print("fruits字典", fruits)
ret_value = fruits.setdefault('Orange',100)
print("Value = ", ret_value)
print("fruits字典", fruits)



print('------------------------------------------------------------')	#60個

person = {'name':'John'}
print("原先字典內容", person)

# 'age'鍵不存在
age = person.setdefault('age')
print("增加age鍵 ", person)
print("age = ", age)

# 'sex'鍵不存在
sex = person.setdefault('sex', 'Male')
print("增加sex鍵 ", person)
print("sex = ", sex)

print('------------------------------------------------------------')	#60個

song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
mydict = {}                         # 空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
        if ch in ".,?":
            songLower = songLower.replace(ch,'')
print("不再有標點符號的歌曲")    
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()        
print("以下是歌曲串列")
print(songList)                     # 列印歌曲串列

# 將歌曲串列處理成字典 
for wd in songList:                 
        if wd in mydict:            # 檢查此字是否已在字典內
            mydict[wd] += 1         # 累計出現次數
        else:
            mydict[wd] = 1          # 第一次出現的字建立此鍵與值
    
print("以下是最後執行結果")
print(mydict)                       # 列印字典

print('------------------------------------------------------------')	#60個

abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

#msgTest = input("請輸入原始字串 : ")
msgTest = 'catdogelephant'

cipher = []
for i in msgTest:                       # 執行每個字元加密
    v = encry_dict[i]                   # 加密
    cipher.append(v)                    # 加密結果
ciphertext = ''.join(cipher)            # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)

print('------------------------------------------------------------')	#60個

print('摩斯密碼字典')
morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.','D':'-..','E':'.',
              'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
              'K':'-.-', 'L':'.-..','M':'--', 'N':'-.','O':'---',
              'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
              'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
              'Z':'--..'}

print(type(morse_code))

#wd = input("請輸入大寫英文字: ")
wd = 'ABCDEFGHIJK'

for c in wd:
    print(morse_code[c])

print('------------------------------------------------------------')	#60個



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
filename = 'C:/_git/vcs/_1.data/______test_files2/sssssss3.txt'

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










'''
新進








'''



'''
print('用pickle來存取一個字典檔案, 讀寫接用 wb/rb binary')

import pickle

f = open("animal.pickle", 'wb')

pickle.dump(animal, f)

f.close()

f = open("animal.pickle", 'rb')

pickledict = pickle.load(f)
f.close()
print(pickledict)
'''
