# 各種python專用的語法 字典

adict = {'book':10, 'pen':3, 'earser':6, 'ruler':2}
for key, value in adict.items():
    if value < 5:
      print("({},{})".format(key, value))


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

name = input("輸入學生姓名：")
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
name = input("輸入要查詢的血型:")
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
    time.sleep(0.3)


#讀取檔案字典範例

print("將 字典 寫入檔案")
filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/sssssss3.txt'

scores=dict()

scores[1] = 30
scores[2] = 50
scores[3] = 80
scores[4] = 90
scores[5] = 100

with open(filename,'w') as fp:
    fp.write(str(scores))
    
print("寫入檔案 : " + filename)







