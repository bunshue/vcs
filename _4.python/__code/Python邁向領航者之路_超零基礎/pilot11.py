import sys
'''

副程式一大堆

'''

print('------------------------------------------------------------')	#60個

print('預設參數')

def interest(interest_type, subject = '敦煌'):
    """ 顯示興趣和主題 """
    print("我的興趣是 " + interest_type )
    print("在 " + interest_type + " 中, 最喜歡的是 " + subject)
    print()

interest('旅遊')                          # 傳遞一個參數
interest('閱讀', '旅遊類')                # 傳遞二個參數,不同的主題

print('------------------------------------------------------------')	#60個

def make_icecream(icecream_type, *toppings):
    # 列出製作冰淇淋的配料
    print("一定要有的參數 ", icecream_type, "\n不定長度參數 : ")
    for topping in toppings:
        print("--- ", topping)
    print()

make_icecream('固定參數', '參數1')
make_icecream('固定參數', '參數1', '參數2', '參數3')

print('------------------------------------------------------------')	#60個

def printmsg( ):
    # 函數本身沒有定義變數, 只有執行列印全域變數功能
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數

print('------------------------------------------------------------')	#60個

def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    for wd in songList:
        if wd in mydict:
            mydict[wd] += 1
        else:
            mydict[wd] = 1

data = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""

mydict = {}                         # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)                       # 列印字典

print('------------------------------------------------------------')	#60個

def my_divmod(x, y):
    # 模擬divmod()
    a = x // y
    b = x % y
    return a, b

x = 123
y = 18
rtn = my_divmod(x, y)
print('回傳多筆資料的形態 : {}'.format(type(rtn)))
print('商 = {},  餘數 = {}'.format(rtn[0], rtn[1]))

print('------------------------------------------------------------')	#60個

# 輾轉相除法, 也就是歐幾里德演算法 
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

a = 234
b = 456
print("最大公約數是 : ", gcd(a, b))

print('------------------------------------------------------------')	#60個

def factorial(n):
    """ 計算n的階乘, n 必須是正整數 """
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

N = 10
print(N, " 的階乘結果是 = ", factorial(N))

print('------------------------------------------------------------')	#60個

