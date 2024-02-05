#各種檔案寫讀範例 新進暫存

print('------------------------------------------------------------')	#60個

import sys, ast

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores.csv'

scores = dict()
with open(filename,'r') as fp:
    filedata = fp.read()
    #scores = ast.literal_eval(filedata)
print("以下是{}成績檔的字典型態資料:".format(filename))

print('------------------------------------------------------------')	#60個

"""
import sys

std_data = dict()
with open(filename, encoding='utf-8') as fp:
    alldata = fp.readlines()
    for item in alldata:
        no, name = item.rstrip('\n').split(',')
        std_data[no] = name
print(std_data)
"""

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
json

filename = 'C:/_git/vcs/_1.data/______test_files2/news_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)
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

print("------------------------------------------------------------")  # 60個

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

#練習 19 擷取登入帳號資訊

def passwd_to_dict(filename):
    users = {}
    with open(filename) as f:
        for line in f:
            user_info = line.split(':')
            users.update({user_info[0]: user_info[2]})
    return users

print(passwd_to_dict(r'.\data\passwd.cfg'))



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

#練習 22 讀寫 CSV 檔

import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename, 'r') as f_read, \
            open(csv_filename, 'w', newline='') as f_write:
        csv_reader = csv.reader(f_read, delimiter=':')
        csv_writer = csv.writer(f_write, delimiter='\t', lineterminator='\n')
        for line in csv_reader:
            csv_writer.writerow([line[0], line[2]])

passwd_to_csv(r'.\data\passwd.cfg', r'tmp_passwd.csv')

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


#練習 33 擷取登入帳號資訊（生成版）

def passwd_to_dict_2(filename):
    with open(filename) as f:
        d = {words[0]: words[2]
             for words
             in [line.split(':') for line in f]}
    return d

print(passwd_to_dict_2(r'.\data\passwd.cfg'))

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



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
