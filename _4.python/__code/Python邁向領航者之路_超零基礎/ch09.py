# ch9_1.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
print(fruits)
print(noodles)
# 列出字典資料型態
print("字典fruits資料型態是: ",type(fruits))

print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_2.py

# ch9_2.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
print("水蜜桃一斤 = ", fruits['水蜜桃'], "元")
print("牛肉麵一碗 = ", noodles['牛肉麵'], "元")


 

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_3.py

# ch9_3.py
fruits = {0:'西瓜', 1:'香蕉', 2:'水蜜桃'}
print(fruits[0], fruits[1], fruits[2])


   

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_4.py

# ch9_4.py
blood = {'A':'誠實', 'B':'開朗', 'O':'自信'}
print('目前血型個性字典:', blood)
blood['AB'] = '聰明少有野心'   # 新增
print('最新血型個性字典:', blood)




      




   

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_5.py

# ch9_5.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊價格香蕉一斤 = ", fruits['香蕉'], "元")
fruits['香蕉'] = 12
print("新價格香蕉一斤 = ", fruits['香蕉'], "元")

   

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_6.py

# ch9_6.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
del fruits['西瓜']
print("新fruits字典內容:", fruits)



   

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_7.py

# ch9_7.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
fruits.clear( )
print("新fruits字典內容:", fruits)


  

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_8.py

# ch9_8.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
del fruits
print("新fruits字典內容:", fruits)       # 錯誤! 錯誤!




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_9.py

# ch9_9.py
season = {}           # 建立空字典
print("空季節字典", season)
season['Summer'] = '夏天'
season['Winter'] = '冬天'
print("新季節字典", season)



print('------------------------------------------------------------')	#60個





#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_10.py

# ch9_10.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
cfruits = fruits.copy( )
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_11.py

# ch9_11.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
empty_dict = {}
print("fruits字典元素數量     = ", len(fruits))
print("noodles字典元素數量    = ", len(noodles))
print("empty_dict字典元素數量 = ", len(empty_dict))



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_12.py

# ch9_12.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
key = input("請輸入鍵(key) = ")
value = input("請輸入值(value) = ")
if key in fruits:
    print("%s已經在字典了" % key)
else:
    fruits[key] = value
    print("新的fruits字典內容 = ", fruits)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_13.py

# ch9_13.py
blood = {'A':'誠實','B':'開朗','O':'自信','AB':'聰明少有野心'}
key = input("請輸入血型 : ")
if key in blood:
    print(blood[key])
else:
    print('輸入錯誤')






      




   

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_14.py

# ch9_14.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
print("Stephen Curry是 %s 的球員" % players['Stephen Curry'])
print("Kevin Durant是 %s 的球員" % players['Kevin Durant'])
print("Paul Gasol是 %s 的球員" % players['Paul Gasol']) 





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_15.py

# ch9_15.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_16.py

# ch9_16.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
for name in players.keys( ):
    print("姓名: ", name)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_17.py

# ch9_17.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_18.py

# ch9_18.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_19.py

# ch9_19.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'
          }
for team in players.values( ):
    print(team)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_20.py

# ch9_20.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_21.py

# ch9_21.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_22.py

# ch9_22.py
fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print("Value = ", ret_value1)
ret_value2 = fruits.get('Grape')
print("Value = ", ret_value2)
ret_value3 = fruits.get('Grape', 10)
print("Value = ", ret_value3)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_23.py

# ch9_23.py
# key在字典內
fruits = {'Apple':20, 'Orange':25}
ret_value = fruits.setdefault('Orange')
print("Value = ", ret_value)
print("fruits字典", fruits)
ret_value = fruits.setdefault('Orange',100)
print("Value = ", ret_value)
print("fruits字典", fruits)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_24.py

# ch9_24.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_25.py

# ch9_25.py
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_26.py

# ch9_26.py
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

wd = input("請輸入欲查詢的星座 : ")
if wd in season:
    print(wd, " 本月運勢 : ", season[wd])
else:
    print("星座輸入錯誤")














print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_27.py

# ch9_27.py
abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msgTest = input("請輸入原始字串 : ")

cipher = []
for i in msgTest:                       # 執行每個字元加密
    v = encry_dict[i]                   # 加密
    cipher.append(v)                    # 加密結果
ciphertext = ''.join(cipher)            # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch09\ch9_28.py

# ch9_28.py
morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.','D':'-..','E':'.',
              'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
              'K':'-.-', 'L':'.-..','M':'--', 'N':'-.','O':'---',
              'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
              'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
              'Z':'--..'}

wd = input("請輸入大寫英文字: ")
for c in wd:
    print(morse_code[c])


























print('------------------------------------------------------------')	#60個


