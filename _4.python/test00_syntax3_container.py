# 各種python專用的語法 字典




import sys

print('------------------------------------------------------------')	#60個

print('字典的操作')
      
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
del fruits['西瓜']
print("新fruits字典內容:", fruits)

print('------------------------------------------------------------')	#60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
fruits.clear( )
print("新fruits字典內容:", fruits)
print("fruits字典元素數量     = ", len(fruits))

print('------------------------------------------------------------')	#60個

season = {}           # 建立空字典
print("空季節字典", season)
season['Summer'] = '夏天'
season['Winter'] = '冬天'
print("新季節字典", season)

print('------------------------------------------------------------')	#60個

blood = {'A':'誠實','B':'開朗','O':'自信','AB':'聰明少有野心'}
print(type(blood))
print(blood)

print('------------------------------------------------------------')	#60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
for name, team in players.items( ):
    print("姓名: ", name)
    print("隊名: ", team, end='\n\n')

print('------------------------------------------------------------')	#60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
for name in players.keys( ):
    print("姓名: ", name)

print('------------------------------------------------------------')	#60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
for name in sorted(players.keys( )):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print('------------------------------------------------------------')	#60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
for name in sorted(players.keys( ),reverse=True):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print('------------------------------------------------------------')	#60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
for team in players.values( ):
    print(team)

print('------------------------------------------------------------')	#60個

# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items( ):
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

season = {'水瓶座':'1月20日 - 2月18日, 須警惕小人',
          '雙魚座':'2月19日 - 3月20日, 凌亂中找立足',
          '白羊座':'3月21日 - 4月19日, 運勢比較低迷',
          '金牛座':'4月20日 - 5月20日, 財運較佳',
          '雙子座':'5月21日 - 6月21日, 運勢好可錦上添花',
          '巨蟹座':'6月22日 - 7月22日, 不可鬆懈大意',
          '獅子座':'7月23日 - 8月22日, 會有成就感',
          '處女座':'8月23日 - 9月22日, 會有挫折感',
          '天秤座':'9月23日 - 10月23日, 運勢給力',
          '天蠍座':'10月24日 - 11月22日, 中規中矩',
          '射手座':'11月23日 - 12月21日, 可羨煞眾人',
          '魔羯座':'12月22日 - 1月19日, 需保有謙虛',
          }

#wd = input("請輸入欲查詢的星座 : ")
wd = '雙魚座'

if wd in season:
    print(wd, " 本月運勢 : ", season[wd])
else:
    print("星座輸入錯誤")

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





