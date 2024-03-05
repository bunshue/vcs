#各種檔案寫讀範例 txt 3

import sys

print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個




"""
#readlines()可以依照行讀取整個檔案，回傳是一個List，每一個element就是一行字。

file = open("demo_en.txt", "r")

lines = file.readlines()
print(lines)

file.close()
"""

print('------------------------------------------------------------')	#60個

"""
print('一種寫入檔案的方法')
filename = 'tmp.txt'

fp = open(filename,'w')
print('[OPTIONS]', file=fp)
print('Auto Index=Yes', file=fp)
print('Binary TOC=No', file=fp)
print('Binary Index=Yes', file=fp)
print('Compatibility=1.1', file=fp)
print('Error log file=ErrorLog.log', file=fp)
print('Display compile progress=Yes', file=fp)
print('Full-text search=Yes', file=fp)
print('Default window=main', file=fp)
print('', file=fp)  #寫一個空白列
print('[WINDOWS]', file=fp)
print('main=,"' + '","'
+ '","","",,,,,0x23520,222,0x1046,[10,10,780,560],'
'0xB0000,,,,,,0', file=fp)
print('', file=fp)
print('[FILES]', file=fp)
print('', file=fp)
fp.close()
"""


"""
print('11')
filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline())#讀一行

print('22')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    data = f.read() #讀全部成一行串列

print(repr(data))
print(data)
print(data.split())
data = data.split()
for d in data:
    d.strip()
print(data)

print('33')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.readlines())#讀全部成多行串列
"""

print("------------------------------------------------------------")  # 60個


"""
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行
with open(fn, encoding='utf-8-sig') as file_Obj:  # 開啟utf-8檔案
    obj_list = file_Obj.readlines()               # 每次讀一行
"""



file = open("data/temp.txt", "w+")

file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

file.flush()

print("寫入之後的游標位置：", file.tell())

print('往後跳16拜')
file.seek(16, 0)

print('擷取至位置26')
file.truncate(26)

print('讀出來')
print(file.read())

file1=open("data/temp.txt","r")
text=file1.read(1) #以read()方法讀取檔案
print(text)
text=file1.read(3) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
file1.close()


print("------------------------------------------------------------")  # 60個

print("讀出檔案最後一行字")

def read_final_line(filename):
    f = open(filename, 'r')
    for line in f:
        pass
    f.close()
    return line

print(read_final_line(r'.\data\login.log'))


print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


#練習 20 統計檔案的字元數、字數與行數

def wordcount(filename):
    result = {
        'Characters': 0,
        'Words': 0,
        'Unique words': 0,
        'Lines': 0,
        }
    unique_words = set()
 
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            result['Lines'] += 1
            result['Characters'] += len(line)
            result['Words'] += len(words)
            unique_words.update(words)
 
        result['Unique words'] = len(unique_words)
 
    for key, value in result.items():
        print(f'{key}: {value}')

wordcount(r'.\data\text.txt')

print('------------------------------------------------------------')	#60個

#練習 21 找出檔案內的最長單字

def find_longest_word(filename):
    longest = ''
    with open(filename, 'r') as f:
        for line in f:
            for word in line.replace('.', '').split():
                if len(word) > len(longest):
                    longest = word
    return longest

print(find_longest_word(r'.\data\text2.txt'))

print('------------------------------------------------------------')	#60個

#練習 31 豬拉丁文 --- 檔案翻譯機

def pl_word(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

def pl_file(filename):
    with open(filename, 'r') as f:
        return ' '.join([pl_word(word.lower().replace('.', ''))
                         for line in f
                         for word in line.split()])

print(pl_file(r'.\data\text2.txt'))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#練習 34 過濾檔案中特定條件的單字

def word_filter(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(filename, 'r') as f:
        words = ([word.replace('.', '')
                  for line in f
                      for word in line.split()
                      if len(set(word) & vowels) >= 3])
    return words

print(word_filter(r'.\data\text2.txt'))

print('------------------------------------------------------------')	#60個

#練習 35 希伯來數字密碼（Part I + Part II）

import string

def gematria_dict():
    return {char: index
            for index, char
            in enumerate(string.ascii_lowercase, 1)}

GEMATRIA = gematria_dict()

def gematria_value(word):
    return sum(GEMATRIA[char]
               for char in word.lower()
               if char in GEMATRIA)

def gematria_equal_words(my_word, filename):
    my_value = gematria_value(my_word)
    with open(filename, 'r', encoding='utf-8') as f:
        return [word
                for line in f
                for word in line.lower().split()
                if my_value == gematria_value(word)]

print(gematria_equal_words('programming', r'.\data\book.txt'))



print('------------------------------------------------------------')	#60個

#練習 48 檔案單字產生器

def word_generator(filename, max_words):
    index = 0
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if index >= max_words:
                    return
                yield word.replace('.', '')
                index += 1

ten_words = word_generator(r'.\data\text2.txt', 10)

for word in ten_words:
    print(word)

print('------------------------------------------------------------')	#60個

print('直接 print 到檔案')

with open('tmp_cccccc.txt', 'wt') as f:
    print('Hello World!', file = f)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/Romeo&Juliet.txt'

infile = open(filename, 'r')

count = 0
for line in infile:
    str1 = line.strip()
    if len(str1)>0:
        count += 1

print('total', count, 'lines')
infile.close()

print("------------------------------------------------------------")  # 60個

def distinctNN(n):
    set1 = set()
    for i in range(2, n+1):
        for j in range(1, n+1):
            set1.add(i*j)
    return set1

def doOutput(fname, outlist):
    outfile = open(fname, 'w')
    
    count = 0
    for num in outlist:
        outfile.write(str(num)+' ')
        count += 1
        if count%5==0:
            outfile.write('\n')
            
    outfile.close()
    print(fname+' created')

setNN = distinctNN(19)
list1 = sorted(list(setNN))
#print(list1)
outfname = 'tmp_SortedNN.txt'
doOutput(outfname, list1)

print("------------------------------------------------------------")  # 60個

"""
filename = 'myfile.txt'
inf = open(filename, 'r')
outfname = filename[:-4]+'2.txt'
outf = open(outfname, 'w')

for line in inf:           # 讀進來的line字串是有包含檔案內的換行字元哦！
    str1 = line.strip()    # 移除line的多餘空白
    if len(str1)>0:        # 如果移除完還有內容，寫進輸出檔
        outf.write(str1+'\n')
inf.close()
outf.close()
"""

print("------------------------------------------------------------")  # 60個

filename = 'data/en-us2.log'
infile = open(filename, 'r')

# 前50行
count = 0
for line in infile:
    if count>=50:
        break
    print((count+1), line, end='')
    count += 1
    
infile.close()


print("------------------------------------------------------------")  # 60個

""" many

filename = 'C:/_git/vcs/_4.python/_data/Romeo&Juliet.txt'
infile = open(filename, 'r')

count = 0
str1 = infile.readline()
len1 = len(str1)
while len1>0:
    count += 1
    print(count, str1.strip())
    str1 = infile.readline()
    len1 = len(str1)
    

print('total', count, 'lines')
infile.close()
"""

"""
with open("myfile.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
        
# 不用關檔了！！
"""
print("------------------------------------------------------------")  # 60個



"""
从文本文件中读取数据

"""

""" fail
import time

def main():
    # 一次性读取整个文件内容
    with open('data/致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('data/致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('data/致橡树.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()
"""

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python-100-Days-zh_TW-master\Day01-15\code\Day11\file2.py

print('读取圆周率文件判断其中是否包含自己的生日')

birth = "0311"
with open('data/pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')



print("------------------------------------------------------------")  # 60個


# 處理劇本中的單一句子，去除標點並切割
def processString(str1):
    tup1 = (',', '.', ';', '?', '!', "'", '-', ':')
    strK = str1
    #Why, such is love's transgression. 要轉換成：
    #Why  such is love s transgression 然後用空白切割
    for tok in tup1:
        strK = strK.replace(tok, ' ')
    strK = strK.lower()
    slist = strK.split()
    # 串列生成，將兩個字母以上的文字以及a和i留下
    slist2 = [s for s in slist if len(s)>1 or s=='a' or s=='i']
    return slist2

filename = 'C:/_git/vcs/_4.python/_data/Romeo&Juliet.txt'

infile = open(filename, 'rt', encoding='utf-8')

freq = {}
for line in infile:
    str1 = line.strip()
    # 處理劇本中的單一句子，去除標點並切割
    slist = processString(str1)
    # 將切好的詞彙紀錄頻率
    for tok in slist:
        freq[tok] = freq.get(tok, 0)+1
infile.close()

# 開始找尋最長以及最常的詞彙
longest = ''    # 最長
maxoccur = ''    # 最常
maxv = 0
for k, v in freq.items():
    # 比出目前最長
    if len(k)>len(longest):
        longest = k
    # 比出目前最常
    if v>maxv:
        maxoccur = k
        maxv = v
        
print('最長用詞:', longest, ', 長度', len(longest))
print('最頻繁用詞:', maxoccur, ', 次數', maxv)


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

filename = 'data/DatingTestSet.txt'
stat = {}
tags = ['largeDoses', 'smallDoses', 'didntLike']
with open(filename, 'rt', encoding='utf-8') as inf:
    for line in inf:
        slist = line.strip().split('\t')
        try:
            idx = tags.index(slist[-1])
            key = tags[idx]
            stat[key] = stat.get(key, 0)+1
        except:
            # 沒出現過的tag使用index()方法
            # 會產生ValueError例外，跳過
            pass

# 使用串列生成加上sum()來找出總數
sum1 = sum([v for v in stat.values()])
for k, v in stat.items():
    # 計算百分比並完成輸出
    stat[k] = 100.0*v/sum1
    print(k+':', str(stat[k])+'%')
    
print("------------------------------------------------------------")  # 60個







print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個





