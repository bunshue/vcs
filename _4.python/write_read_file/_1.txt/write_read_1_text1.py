"""
各種檔案寫讀範例 txt

先寫後讀 寫新檔 讀舊檔

f = open(檔案, 模式, 編碼)

讀寫模式有
r - 讀取 (檔案需存在)
w - 寫入 新建檔案寫入(檔案可不存在，若存在則清空)
a - 附加 資料附加到舊檔案後面(游標指在EOF)

先
# 使用with
後
# 不使用with

先寫
1. write(
2. writelines(

後讀
3. read() read(N)
4. readline()
5. readlines()
6. for line in f:

7. 應用範例

8. 其他 & 新進


所有的 開啟檔案
先寫
# 使用with, 不需要f.close()
with open(filename, "wt") as f:
with open(filename, "w") as f:  # 覆寫模式
with open(filename, "a") as f:  # 附加模式
with open(filename, "w", encoding="cp950") as f:

# 不使用with
f = open(filename, "w")  # 預設編碼
f = open(filename, "w", encoding="UTF-8")  # 指定編碼
f = open(filename, "a", encoding="UTF-8")  # 指定編碼
f = open(filename, 'r', encoding='UTF-8-sig')
f = open(filename, mode="w")  # 取代先前資料
f = open(filename, mode="a")  # 附加資料後面
f = open(filename, mode="w", encoding="utf-8")
f = open(filename, mode="a", encoding="cp950")

後讀
# 使用with, 不需要f.close()

with open(filename, "r") as f:
with open(filename) as f:  # 用預設mode=r開啟檔案,傳回檔案物件f
with open(filename, mode="r") as f:
with open(filename, "rt", encoding="utf8") as f:
with open(filename, "r", encoding="UTF-8-sig") as f:
with open(filename, "r", encoding="UTF-8") as f:
with open(filename, "r", encoding="cp950") as f:
with open(filename, encoding="utf-8") as f:
with open(filename, encoding="utf-8-sig") as f:

# 不使用with
f = open(filename)
f = open(filename, "r")
f = open(filename, "rt")
f = open(filename, "r+")
f = open(filename, "r+", encoding="utf8")
f = open(filename, "r", encoding="utf8")
f = open(filename, "r", encoding="UTF-8")
f = open(filename, "r", encoding="UTF-8-sig")
f = open(filename, "r", encoding="cp950")
f = open(filename, "r+", encoding="utf8")
f = open(filename, encoding="utf-8")
f = open(filename, encoding="cp950")
"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

poem_text = """黃河遠上白雲間\n
一片孤城萬仞山\n
羌笛何須怨楊柳\n
春風不度玉門關\n
"""

print("------------------------------------------------------------")  # 60個
print("1. write() 一次寫入一個字串")
print("------------------------------------------------------------")  # 60個

filename = "tmp_write_text01.txt"

f = open(filename, "a")

f.write(poem_text)
f.write("ABC ")
f.write("DEF ")
f.write("Bill Clinton ")
f.write("Barack Obama ")

f.close()

print("附加模式寫檔案")
f = open(filename, "a")
f.write("UVWXYZ")

count = f.write(poem_text)
print("這個 f.write() 指令 寫了", count, "個字元")

f.close()

print("------------------------------------------------------------")  # 60個

poem_text = "黃河遠上白雲間一片孤城萬仞山羌笛何須怨楊柳春風不度玉門關"

filename = "tmp_write_text02_poem.cp950.txt"
print("用cp950編碼 分段寫檔, 檔名 :", filename)
size = len(poem_text)
offset = 0
chunk = 5  # 每次寫入的單位

with open(filename, "w", encoding="cp950") as f:
    while True:
        if offset > size:
            break
        count = f.write(poem_text[offset : offset + chunk])
        print("這個 f.write() 指令 寫了", count, "個字元")
        offset += chunk

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("2. writelines() 一次寫入一個字串串列")
print("------------------------------------------------------------")  # 60個

string1 = "黃河遠上白雲間\n"
string2 = "一片孤城萬仞山\n"
string3 = "羌笛何須怨楊柳\n"
string4 = "春風不度玉門關"
strings = [string1, string2, string3, string4]

filename = "tmp_write_text03_poem.cp950.txt"

print("用cp950編碼寫一檔, 檔名 :", filename)
with open(filename, "w", encoding="cp950") as f:
    f.writelines(strings)
    f.write("AAAA")
    f.writelines(["\nBBBB", "\nCCCC"])

print("------------------------------------------------------------")  # 60個
print("3. read() read(N)")
# read(無參數), 從目前檔案位置讀到檔尾
# read(N), 讀N字元
print("------------------------------------------------------------")  # 60個

filename = "data/abc.txt"

f = open(filename, "r")

print("讀取N字元 => 字串")
cc = f.read(5)  # read(N), 讀N字元
print(cc)

print("從目前檔案位置讀到檔尾")
cc = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
f.close()
print("檔案內容 :", cc)

print("用read()取得檔案大小")
filename = "data/abc.txt"
f = open(filename, "r")
cc = f.read()  # 一次讀完全部
f.close()
print("檔案大小 :", len(cc), "拜")

print("------------------------------------------------------------")  # 60個

# 設定一次讀取的數量
filename = "data/poem.utf-8.txt"
chunk = 10
msg = ""
with open(filename, "r", encoding="utf-8") as f:
    while True:
        print("讀N個字元出來")
        cc = f.read(chunk)  # 一次讀取chunk數量
        # print(cc)
        if not cc:
            break
        msg += cc
print(msg)

print("------------------------------------------------------------")  # 60個

filename = "data/poem.utf-8.txt"

print("讀取一個檔案 binary, 檔名 : " + filename)
with open(filename, "rb") as f:
    lines = f.read().decode("utf-8")
    print(lines)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("4. readline() 一次讀一行")
print("------------------------------------------------------------")  # 60個

filename = "data/poem.utf-8.txt"

f = open(filename, "r", encoding="UTF-8-sig")

print("讀出1行")
line = f.readline()
print(line)

print("跳回檔頭")
f.seek(0)

print("讀出5個字元 readline(N)")
print(f.readline(5))

f.close()

print("------------------------------------------------------------")  # 60個

print("用 while + readline() 一次讀一行 讀到完")

filename = "data/王之渙_涼州詞.big5.txt"

f = open(filename, "r")

while True:
    # print("讀出1行")
    line = f.readline()
    if len(line) == 0:  # Zero length indicates EOF
        break
    print(line.strip())
f.close()

# 一樣

f = open(filename, "r")
# print("讀出1行")
line = f.readline()
while line != "":
    print(line.strip())
    line = f.readline()
f.close()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("5. readlines()")
print("用readlines()一次讀完全檔 至一個 list")
# readlines()可以依照行讀取整個檔案，回傳是一個List，每一個element就是一行字。
print("------------------------------------------------------------")  # 60個

filename = "data/王之渙_涼州詞.big5.txt"

f = open(filename)

lines = f.readlines()
for line in lines:
    print(line)

f.close()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("6. for line in f:")
print("------------------------------------------------------------")  # 60個

filename = "data/王之渙_涼州詞.big5.txt"

f = open(filename, "r")

# 通過迭代器訪問
# 通过for-in循环逐行读取
for line in f:  # 逐行讀取檔案到變數line
    print(line)
    # print(line.strip())
f.close()

print("------------------------------------------------------------")  # 60個

temperatures = []
with open("data/temperature.txt") as f:
    for row in f:
        temperatures.append(float(row.strip()))

print("取得溫度資料 :\n", temperatures)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("seek tell truncate")
print("------------------------------------------------------------")  # 60個

print("檔案指標操作 fseek ftell")

filename = "tmp_write_text04_seek1.txt"

f = open(filename, "w+")
f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
f.flush()

print("目前檔案指標位置 :", f.tell())

print("跳到檔案位置5")
f.seek(5)

print("預計讀到的位置 15")
f.truncate(15)

print("目前檔案指標位置 :", f.tell())

print("讀出來 5~15")
cc = f.read()
print(cc)

print("目前檔案指標位置 :", f.tell())

f.close()

f = open(filename, "rb")
f.seek(6)  # 移到索引第 6 (第7個字元)位置
string1 = f.read(7)  # 讀取 7 個字元
print(string1)  # b'Python\n'

print("跳回檔頭")
f.seek(0)  # 回文件最前端

string2 = f.read(5)  # 讀取 5 個字元
print(string2)  # b'Hello'

f.seek(-8, 2)  # 移至最尾端，向前取 8 個字元

string3 = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
print(string3)  # b'Welcome\n'

# f.seek(8, 0)

f.close()

print("------------------------------------------------------------")  # 60個

print("開啟檔案 : " + filename)
f = open(filename, "r+")
print("讀取N字元")
string = f.read(5)
print("read 10 string is : ", string)

print("讀取檔案 : " + filename)

print("目前檔案指標位置 :", f.tell())

print("將檔案位置調到 20")
f.seek(20)

print("讀取N字元")
string = f.read(5)
print("讀取10拜 : ", string)

print("將檔案位置調到檔頭")
print("跳回檔頭")
f.seek(0)

print("讀取N字元")
string = f.read(5)
print("讀取10拜 : ", string)
f.close()

print("------------------------------------------------------------")  # 60個

filename = "data/abc.txt"

print("開啟檔案 : " + filename)

f = open(filename, "r", encoding="cp950")
print(f"目前指針位置 {f.tell()}")
string1 = f.read(7)
print(f"讀出資料 : {string1}, 目前指針位置 {f.tell()}")
string2 = f.read(7)
print(f"讀出資料 : {string2}, 目前指針位置 {f.tell()}")
string3 = f.read(7)
print(f"讀出資料 : {string3}, 目前指針位置 {f.tell()}")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("7. 應用範例")
print("------------------------------------------------------------")  # 60個


# 統計檔案的字元數、字數與行數


def wordcount(filename):
    result = {
        "Characters": 0,
        "Words": 0,
        "Unique words": 0,
        "Lines": 0,
    }
    unique_words = set()

    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            result["Lines"] += 1
            result["Characters"] += len(line)
            result["Words"] += len(words)
            unique_words.update(words)

        result["Unique words"] = len(unique_words)

    for key, value in result.items():
        print(f"{key}: {value}")


filename = "data/text.txt"
wordcount(filename)

print("------------------------------------------------------------")  # 60個

# 找出檔案內的最長單字


def find_longest_word(filename):
    longest = ""
    with open(filename, "r") as f:
        for line in f:
            for word in line.replace(".", "").split():
                if len(word) > len(longest):
                    longest = word
    return longest


print(find_longest_word("../data/text2.txt"))

print("------------------------------------------------------------")  # 60個

# 豬拉丁文 --- 檔案翻譯機


def pl_word(word):
    if word[0] in "aeiou":
        return f"{word}way"
    return f"{word[1:]}{word[0]}ay"


def pl_file(filename):
    with open(filename, "r") as f:
        return " ".join(
            [
                pl_word(word.lower().replace(".", ""))
                for line in f
                for word in line.split()
            ]
        )


print(pl_file("../data/text2.txt"))

print("------------------------------------------------------------")  # 60個

# 過濾檔案中特定條件的單字


def word_filter(filename):
    vowels = {"a", "e", "i", "o", "u"}
    with open(filename, "r") as f:
        words = [
            word.replace(".", "")
            for line in f
            for word in line.split()
            if len(set(word) & vowels) >= 3
        ]
    return words


print(word_filter("../data/text2.txt"))

print("------------------------------------------------------------")  # 60個

# 希伯來數字密碼（Part I + Part II）

import string


def gematria_dict():
    return {char: index for index, char in enumerate(string.ascii_lowercase, 1)}


GEMATRIA = gematria_dict()


def gematria_value(word):
    return sum(GEMATRIA[char] for char in word.lower() if char in GEMATRIA)


def gematria_equal_words(my_word, filename):
    my_value = gematria_value(my_word)
    with open(filename, "r", encoding="utf-8") as f:
        return [
            word
            for line in f
            for word in line.lower().split()
            if my_value == gematria_value(word)
        ]


print(gematria_equal_words("programming", "../data/book.txt"))

print("------------------------------------------------------------")  # 60個

# 檔案單字產生器


def word_generator(filename, max_words):
    index = 0
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                if index >= max_words:
                    return
                yield word.replace(".", "")
                index += 1


ten_words = word_generator("../data/text2.txt", 10)

for word in ten_words:
    print(word)

print("------------------------------------------------------------")  # 60個

filename = "data/Romeo&Juliet.txt"

f = open(filename, "r")

count = 0
for line in f:
    string1 = line.strip()
    if len(string1) > 0:
        count += 1

print("total", count, "lines")
f.close()

print("------------------------------------------------------------")  # 60個


# 處理劇本中的單一句子，去除標點並切割
def processString(str1):
    tup1 = (",", ".", ";", "?", "!", "'", "-", ":")
    strK = str1
    # Why, such is love's transgression. 要轉換成：
    # Why  such is love s transgression 然後用空白切割
    for tok in tup1:
        strK = strK.replace(tok, " ")
    strK = strK.lower()
    slist = strK.split()
    # 串列生成，將兩個字母以上的文字以及a和i留下
    slist2 = [s for s in slist if len(s) > 1 or s == "a" or s == "i"]
    return slist2


filename = "data/Romeo&Juliet.txt"

f = open(filename, "rt", encoding="utf-8")

freq = {}
for line in f:
    string1 = line.strip()
    # 處理劇本中的單一句子，去除標點並切割
    slist = processString(string1)
    # 將切好的詞彙紀錄頻率
    for tok in slist:
        freq[tok] = freq.get(tok, 0) + 1
f.close()

# 開始找尋最長以及最常的詞彙
longest = ""  # 最長
maxoccur = ""  # 最常
maxv = 0
for k, v in freq.items():
    # 比出目前最長
    if len(k) > len(longest):
        longest = k
    # 比出目前最常
    if v > maxv:
        maxoccur = k
        maxv = v

print("最長用詞:", longest, ", 長度", len(longest))
print("最頻繁用詞:", maxoccur, ", 次數", maxv)

print("------------------------------------------------------------")  # 60個

filename = "../data/DatingTestSet.txt"
stat = {}
tags = ["largeDoses", "smallDoses", "didntLike"]
with open(filename, "rt", encoding="utf-8") as f:
    for line in f:
        slist = line.strip().split("\t")
        try:
            idx = tags.index(slist[-1])
            key = tags[idx]
            stat[key] = stat.get(key, 0) + 1
        except:
            # 沒出現過的tag使用index()方法
            # 會產生ValueError例外，跳過
            pass

# 使用串列生成加上sum()來找出總數
sum1 = sum([v for v in stat.values()])
for k, v in stat.items():
    # 計算百分比並完成輸出
    stat[k] = 100.0 * v / sum1
    print(k + ":", str(stat[k]) + "%")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("7. 應用範例")
print("------------------------------------------------------------")  # 60個


def wordsNum(filename):
    # 適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數
    try:
        with open(filename) as f:  # 用預設mode=r開啟檔案
            data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
    except Exception:
        print("Exception找不到 %s 檔案" % filename)
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()  # 將文章轉成串列
        print("檔案 :", filename, "字數 :", len(wordList), "字")  # 列印文章字數


filename = "data/song1.txt"
wordsNum(filename)

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/quotes.txt"


def get_random_quote():
    start_line = None
    end_line = None

    with open(filename) as f:
        lines = f.readlines()
        print("total lines = ", str(len(lines)))

    # Let's begin with some random line number
    # When '%%' is found, save the line number and break the loop
    for i in range(len(lines) - 1):
        random_line = random.randint(0, len(lines) - 1)
        print(random_line)
        if "%%" in lines[random_line]:
            start_line = random_line
            print("break at start", start_line)
            break

    # Find the closest next '%%' line number
    for i in range(start_line + 1, len(lines)):
        if "%%" in lines[i]:
            end_line = i
            print("break at end", end_line)
            break

    # We don't need the '%%' to be printed
    start_line += 1

    # Join all the text between these two '%%'
    quote = "".join(lines[start_line:end_line])

    return quote


mesg = get_random_quote()
print(mesg)

print("------------------------------------------------------------")  # 60個

import ast

# 讀取文字檔後轉換為 dict
filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_password.txt"

data = dict()

with open(filename, "r", encoding="UTF-8-sig") as f:
    filedata = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
    if filedata != "":
        data = ast.literal_eval(filedata)

print(data)

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print("新增資料 2筆")
data["david"] = "12345678"
data["john"] = "88888888"

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print("檢查資料")

name = "david"
if not name in data:
    print("{} 帳號不存在!".format(name))
else:
    print("{} 帳號存在!, 修改資料".format(name))
    data[name] = "3333"

name = "alex"
if not name in data:
    print("{} 帳號不存在!".format(name))
else:
    print("{} 帳號存在!, 修改資料".format(name))
    data[name] = "3333"

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print("刪除資料")
name = "david"
del data[name]

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

filename = "tmp_write_text05_password.txt"

print("將字典寫為檔案")
with open(filename, "w", encoding="UTF-8-sig") as f:
    f.write(str(data))
print("{}已被儲存完畢".format(name))

print("程式執行完畢！")

print("------------------------------------------------------------")  # 60個

1111


def modifySong(songStr):  # 將歌曲的標點符號用空字元取代
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch, "")
    return songStr  # 傳回取代結果


def wordCount(songCount):
    songList = songCount.split()  # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    for wd in songList:
        if wd in mydict:
            mydict[wd] += 1
        else:
            mydict[wd] = 1


filename = "data/AreYouSleeping.txt"
with open(filename) as f:  # 開啟歌曲檔案
    data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
    print("以下是所讀取的歌曲")
    print(data)  # 列印歌曲檔案

mydict = {}  # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)  # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)  # 列印字典

print("------------------------------------------------------------")  # 60個

"""
2222
def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch, "")
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    mydict = {wd:songList.count(wd) for wd in set(songList)}

filename = "data/AreYouSleeping.txt"
with open(filename) as f:          # 開啟歌曲檔案
    data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
    print("以下是所讀取的歌曲")
    print(data)  # 列印歌曲檔案

mydict = {}                         # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
dictList = sorted(mydict.items(), key=lambda item:item[1], reverse=True)
for key, val in dictList:
    print(key, ":", val)
"""
print("------------------------------------------------------------")  # 60個


def disp_area():
    i = 0
    for a in climate_data:
        print("{:>2}:{:<6}\t".format(i, a[0]), end="")
        i += 1
        if not (i % 5):
            print()
    print()


def disp_temp(data):
    print("顯示區域:", data[0])
    print("---------------------")
    for i in range(1, 13):
        print("{:>2}月均溫:{:>.1f}度".format(i, float(data[i])))
    print("本地區年均溫為{}度".format(data[13]))
    print("---------------------")


filename = "C:/_git/vcs/_1.data/______test_files1/data_climate.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(lines)

climate_data = []
for item in lines:
    climate_data.append(item.rstrip("\n").split("\t"))

disp_area()
disp_temp(climate_data[4])

print("------------------------------------------------------------")  # 60個

filename = "data/Romeo&Juliet.txt"
f = open(filename, "r")

count = 0
print("讀出1行")
line = f.readline()
len1 = len(line)
while len1 > 0:
    count += 1
    # print(count, line.strip()) many
    line = f.readline()
    len1 = len(line)


print("total", count, "lines")
f.close()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

filename = "../data/en-us2.log"
f = open(filename, "r")

# 前50行
count = 0
for line in f:
    if count >= 50:
        break
    print((count + 1), line, end="")
    count += 1

f.close()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("8. 其他 & 新進")
print("------------------------------------------------------------")  # 60個

print("使用 print 寫入檔案")

filename = "tmp_write_text06_by_print.txt"

# f = open(filename, "wt")
f = open(filename, "w")
print("王之渙 涼州詞", file=f)
print("", file=f)  # 寫一個空白列
print("黃河遠上白雲間", file=f)
print("一片孤城萬仞山", file=f)
print("羌笛何須怨楊柳", file=f)
print("春風不度玉門關", file=f)
f.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("製作一個純文字檔 用 tab 分隔")


print("讀取一個純文字檔 用 tab 分隔")

def loadDataSet3(filename):
    X = []
    Y = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        X.append(float(curLine[0]))
        Y.append(float(curLine[-1]))
    return X, Y


# 数据矩阵,分类标签
xArr, yArr = loadDataSet3("data/sep_tab_regdataset.txt")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


def compareString(string):
    # 檢查是否是搜尋的字串
    if string == searchStr:
        return True
    else:
        return False


def parseString(string):
    global num
    # notFoundSignal = True     # 註記沒有找到電話號碼為True
    for i in range(len(data)):  # 用迴圈逐步抽取字串長度做測試
        msg = data[i : i + len(string)]
        if compareString(msg):
            num += 1


# filename = 'C:/_git/vcs/_4.python/_data/射鵰英雄傳.big5.txt'
filename = "C:/_git/vcs/_4.python/_data/python_word_count1.txt"
filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/琵琶行.txt"
with open(filename) as f:  # 讀取ex21_2.txt
    data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
    # print(data)

searchStr = "琵琶"
num = 0
parseString(searchStr)
print("所搜尋字串 %s 共出現 %d 次" % (searchStr, num))

print("------------------------------------------------------------")  # 60個

filename = "file_not_found.txt"

try:
    with open(filename) as f:  # 用預設mode=r開啟檔案
        data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    print("找不到 %s 檔案" % filename)
else:
    print(data)  # 輸出變數data

print("------------------------------------------------------------")  # 60個

filename = "data/王之渙_涼州詞.big5.txt"

try:
    with open(filename) as f:  # 用預設mode=r開啟檔案
        data = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    print(f"找不到 {filename} 檔案")
else:
    wordList = data.split()  # 將文章轉成串列
    print("檔案 :", filename)
    print("字數 :", len(wordList))
    for _ in wordList:
        continue
        print(_)

print("------------------------------------------------------------")  # 60個

print("統計一個檔案的字數")

filename = (
    "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/little_women.txt"
)

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    pass
else:
    words = contents.split()
    num_words = len(words)
    print("檔案 :", filename)
    print("字數 :", num_words)

print("------------------------------------------------------------")  # 60個

print("統計一個檔案的字數")

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/english_book/alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()  # read(無參數), 從目前檔案位置讀到檔尾
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print("檔案 :", filename)
    print("字數 :", num_words)

print("------------------------------------------------------------")  # 60個

print("字串的處理")

# 北美獨立宣言
text = (
    "Resolved: That these United Colonies are, and of right ought to be, "
    + "free and independent States, that they are absolved from all allegiance "
    + "to the British Crown, and that all political connection between them and "
    + "the State of Great Britain is, and ought to be, totally dissolved."
)

print(text)

print("依以下符號split字串")

seplist = [":", ",", "."]
for i in range(len(seplist) - 1):
    text = text.replace(seplist[i], seplist[-1])

slist = text.split(seplist[-1])
print(slist)

with open("tmp_resolution.txt", "wt") as f:
    for s in slist:
        f.write("-------------------------\n")
        f.write(s.strip() + "\n")

print("------------------------------------------------------------")  # 60個

# 以下不能單獨執行
sys.exit()


# 讀出來的資料再處理
poem_text = poem_text.encode("utf-8")  # 轉成 bytes
with open(filename, "wb") as f:
    f.write(poem_text)

text = open(filename).read().strip()
print(text)


# print(string.decode("utf-8")) # 這是什麼？
# print(string.decode("utf-8").encode("utf-8")) # 這是什麼？


stops = f.read().split("\n")
print(stops)


print(repr(data))
print(data)
print(data.split())
data = data.split()
for d in data:
    d.strip()
print(data)

print("------------------------------------------------------------")  # 60個

print("讀txt的第1欄資料出來")

filename = "data/school.txt"
with open(filename, "r") as fp:
    schools = fp.readlines()

school = list()
for s in schools:
    school.append(int(s.split()[1]))

print(school)

print("讀txt的資料進字典")

filename = "data/yrborn.txt"
with open(filename, "r") as fp:
    populations = fp.readlines()

yrborn = dict()

for p in populations:
    yr, tl, boy, girl = p.split()
    yrborn[yr] = {"boy": int(boy), "girl": int(girl)}

print(yrborn)
print(yrborn.keys())


yrlist = sorted(list(yrborn.keys()))
bp = list()
bp_b = list()
bp_g = list()
for yr in yrlist:
    boys = yrborn[yr]["boy"]
    girls = yrborn[yr]["girl"]
    bp.append(boys + girls)
    bp_b.append(boys)
    bp_g.append(girls)

print(yrlist)
