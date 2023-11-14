#from *.py 合併

import sys

print('------------------------------------------------------------')	#60個

#練習 02 加總一系列數字

def my_sum(*numbers):
    output = 0
    for n in numbers:
        output += n
    return output

print(my_sum(10, 20, 30, 40, 50))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#練習 04 將 16 進位數轉為 10 進位

def hex_to_dec():
    hexnum = 'ff'
    decnum = 0
 
    for power, digit in enumerate(reversed(hexnum)):
        if digit.isdigit():
            digit_num = int(digit)
        else:
            digit_num = ord(digit.upper()) - ord('A') + 10
        decnum += digit_num * (16 ** power)
 
    print('十進位結果:', decnum)

hex_to_dec()

print('------------------------------------------------------------')	#60個

#練習 05 豬拉丁文

def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

print(pig_latin('python'))

print('------------------------------------------------------------')	#60個

#練習 06 豬拉丁文 --- 句子翻譯機

def pl_sentence(sentence):
    output = []
    for word in sentence.lower().split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(output)

print(pl_sentence('this is a test'))


print('------------------------------------------------------------')	#60個

#練習 07 ROT13 加密法

def rot13(word):
    output = []
    for c in word.lower():
        new_ord = ord(c) + 13
        if new_ord > ord('z'):
            new_ord -= 26
        output.append(chr(new_ord))
    return ''.join(output)

print(rot13('apple'))

print('------------------------------------------------------------')	#60個

#練習 08 字元排序

def strsort(s):
    return ''.join(sorted(s))

print(strsort('python'))

print('------------------------------------------------------------')	#60個

#練習 09 擷取和合併多種容器的頭尾元素

def first_last(seq):
    return seq[:1] + seq[-1:]

print(first_last('abcde'))
print(first_last([1, 2, 3, 4, 5]))

print('------------------------------------------------------------')	#60個

#練習 10 萬用加總函式

def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('abc', 'd', 'e'))
print(mysum([10, 20, 30], [40, 50], [60]))

print('------------------------------------------------------------')	#60個

#練習 11 依姓名排序聯絡資料

people = [
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'primeminister@canada.gov'),
    ('Angela', 'Merkel', 'primeminister@germany.gov'),
    ('Jacinda', 'Ardern', 'primeminister@newzealand.gov')
    ]

for person in sorted(people, key=lambda d: (d[1], d[0])):
    print(f'{person[1]}, {person[0]}: {person[2]}')

print('------------------------------------------------------------')	#60個

#練習 12 用排版格式輸出容器資料

import operator

def sorted_grades(grades):
    grades.sort(key=operator.itemgetter(2), reverse=True)
    output = []
    for first, last, grade in grades:
        output.append(f'{last:12s}{first:10s}{grade:.1f}')
    return '\n'.join(output)

grades = [
    ('Alice', 'Wooding', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
    ]

print(sorted_grades(grades))

print('------------------------------------------------------------')	#60個

#練習 13 尋找單字中重複最多次的字母

import operator

def most_repeated_letter(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter, word.count(letter)))
    result = sorted(letters_count, key=operator.itemgetter(1))[-1]
    print(f'{result[0]} 重複了 {result[1]} 次')

most_repeated_letter('independence')

print('------------------------------------------------------------')	#60個

#練習 14 餐廳點餐機

menu = {
    '三明治': 50,
    '咖啡': 40,
    '沙拉': 30
    }

price = menu['三明治']
print(price)

print('------------------------------------------------------------')	#60個

#練習 15 降雨量資料庫

def record_rainfall():
    rainfall = {}
    while True:
        city_name = input('輸入城市: ')
        if not city_name:
            break
        rain_mm = input('輸入雨量 (mm): ')
        if not rain_mm:
            rain_mm = 0
 
        rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)
 
    for city, rain in rainfall.items():
        print(f'{city}: {rain} mm')

record_rainfall()

print('------------------------------------------------------------')	#60個

#練習 16 有幾個不重複的數字?

def unique_num_len(numbers):
    return len(set(numbers))

numbers = [1, 2, 3, 1, 2, 3, 4, 1, 2]
print(unique_num_len(numbers))

print('------------------------------------------------------------')	#60個

#練習 17 比較兩個 dict 的差異

def dict_diff(first, second):
    output = {}
    all_keys = sorted(first.keys() | second.keys())
 
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 5}
d2 = {'a': 1, 'b': 2, 'd': 4, 'e': 6}
print(dict_diff(d1, d2))

print('------------------------------------------------------------')	#60個

#練習 18 讀出檔案最後一行字

def read_final_line(filename):
    f = open(filename, 'r')
    for line in f:
        pass
    f.close()
    return line

print(read_final_line(r'.\data\login.log'))

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

print('------------------------------------------------------------')	#60個

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

passwd_to_csv(r'.\data\passwd.cfg', r'.\data\passwd.csv')

print('------------------------------------------------------------')	#60個

#練習 23 讀取 JSON 檔

import json
from collections import defaultdict

def print_scores(filename):
    with open(filename) as json_file:
        record = json.load(json_file)
        result = defaultdict(list)
 
        print('班級:', record['class'])
        for record in record['score']:
            for subject, score in record.items():
                result[subject].append(score)
 
        for subject, scores in result.items():
            print('科目:', subject)
            print('\t最高分:', max(scores))
            print('\t最低分:', min(scores))
            print('\t平均:', sum(scores) / len(scores))

print_scores(r'.\data\score.json')

print('------------------------------------------------------------')	#60個

#練習 24 批次檔案讀取

import os, json
from collections import defaultdict

def print_scores(filename):
    with open(filename) as json_file:
        record = json.load(json_file)
        result = defaultdict(list)
 
        print('班級:', record['class'])
        for record in record['score']:
            for subject, score in record.items():
                result[subject].append(score)
 
        for subject, scores in result.items():
            print('科目:', subject)
            print('\t最高分:', max(scores))
            print('\t最低分:', min(scores))
            print('\t平均:', sum(scores) / len(scores))

def print_dir_scores(dirname):
    for filename in os.listdir(dirname):
        if filename.endswith('.json'):
            print('讀取檔案: ', filename)
            print_scores(os.path.join(dirname, filename))

print_dir_scores(r'.\data\scores')

print('------------------------------------------------------------')	#60個

#練習 25 XML 產生器

def myxml(tag, content='', **kwargs):
    attrs_list = []
    for key, value in kwargs.items():
        attrs_list.append(f' {key}="{value}"')
    attrs = ''.join(attrs_list)
    return f'<{tag}{attrs}>{content}</{tag}>'

print(myxml('foo', 'bar', a=1, b=2, c=3))

print('------------------------------------------------------------')	#60個

#練習 26 簡易前序式計算機

import operator

def prefix_cal(to_solve):
    operation = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        }
    op, num1, num2 = to_solve.split()
    return operation[op](float(num1), float(num2))

print(prefix_cal('+ 2 3'))

print('------------------------------------------------------------')	#60個

#練習 27 自訂密碼產生器

import random

def set_password_source(source):
    def password_gen(length):
        output = []
        for i in range(length):
            output.append(random.choice(source))
        return ''.join(output)
    return password_gen

my_password_gen = set_password_source('0123456789abcdefghij')
print(my_password_gen(10))

print('------------------------------------------------------------')	#60個

#練習 28 輸出一組數字的絕對值

def abs_numbers(numbers):
    # return [abs(x) for x in numbers]
    return list(map(abs, numbers))

print(abs_numbers([1, -2, 3, -4, 5]))

print('------------------------------------------------------------')	#60個

#練習 29 只加總資料中的數字

def sum_numbers(data):
    return sum([int(d)
                for d in data.split()
                if d.isdigit()])

print(sum_numbers('10 abc 20 de44 30 55fg 40'))

print('------------------------------------------------------------')	#60個

#練習 30 用巢狀生成式『壓平』二維 list

def flatten(data):
    return [sub_element
            for element in data
                for sub_element in element]

print(flatten([[1,2], [3,4]]))

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

#練習 32 顛倒一個 dict 的鍵與值

def flipped_dict(my_dict):
    return {value: key
            for key, value in my_dict.items()}

print(flipped_dict({'a': 1, 'b': 2, 'c': 3}))

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

#練習 36 所得稅計算模組

# 以下為模組 \data\income_tax.py 的內容：

TAX_RATE = {
    0: 0.1,
    10000: 0.2,
    50000: 0.3,
    100000: 0.4,
    500000: 0.5
    }

def find_tax_rage(amount):
    result = 0.0
    for income, rate in TAX_RATE.items():
        if amount >= income:
            result = rate
    return result

def calculate_tax(amount):
    return amount * find_tax_rage(amount)

# 匯入 \data 下的模組

import sys

sys.path.append(r'.\data')

# 主程式

from income_tax import calculate_tax

print(calculate_tax(77000))

print('------------------------------------------------------------')	#60個

#練習 37 函式選單模組

# 以下為 \data\menu.py 檔的內容：

def menu(**options):
    def menu_selector():
        option_string = '/'.join(options)
        while True:
            choice = input(f'選擇項目 ({option_string}): ')
            if choice in options:
                return options[choice]
                break
            print('選項不存在!')
    return menu_selector

# 匯入 \data 下的模組

import sys

sys.path.append(r'.\data')

# 主程式
from menu import menu

def func_a():
    return '執行函式 A'

def func_b():
    return '執行函式 B'

def func_x():
    return '執行函式 X'

my_menu = menu(a=func_a, b=func_b, x=func_x)

func = my_menu()
print(func())

print('------------------------------------------------------------')	#60個

#練習 38 冰淇淋球

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class Scoop_Maker:
    def create(self, flavors):
        return [Scoop(flavor) for flavor in flavors]

scoop_maker = Scoop_Maker()
scoops = scoop_maker.create(['巧克力', '香草', '薄荷'])

for scoop in scoops:
    print(scoop, scoop.flavor)

print('------------------------------------------------------------')	#60個

#練習 39 冰淇淋碗

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = []
    
    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            self.scoops.append(new_scoop)
    
    def flavors(self):
        return '/'.join(scoop.flavor
                        for scoop in self.scoops)

bowl = Bowl()
bowl.add_scoop(Scoop('巧克力'))
bowl.add_scoop(Scoop('香草'), Scoop('薄荷'))

print(bowl.flavors())

print('------------------------------------------------------------')	#60個

#練習 40 類別屬性：冰淇淋碗上限

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        
    def __repr__(self):
        return f'Scoop({self.flavor})'

class Bowl:
    max_scoops = 3
    
    def __init__(self):
        self.scoops = []
    
    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)
    
    def __repr__(self):
        return f'Bowl(scoops={self.scoops}'

bowl = Bowl()
bowl.add_scoop(Scoop('巧克力'))
bowl.add_scoop(Scoop('香草'), Scoop('薄荷'))
bowl.add_scoop(Scoop('焦糖'), Scoop('抹茶'))

print(bowl)

print('------------------------------------------------------------')	#60個

#練習 41 特大碗冰淇淋

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
        
    def __repr__(self):
        return f'Scoop({self.flavor})'

class Bowl:
    max_scoops = 3
    
    def __init__(self):
        self.scoops = []
    
    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)
    
    def __repr__(self):
        return f'Bowl(scoops={self.scoops}'

class ExtraBowl(Bowl):
    max_scoops = 5
    

bowl = ExtraBowl()
bowl.add_scoop(Scoop('巧克力'))
bowl.add_scoop(Scoop('香草'), Scoop('薄荷'))
bowl.add_scoop(Scoop('焦糖'), Scoop('抹茶'))

print(bowl)

print('------------------------------------------------------------')	#60個

#練習 42 以字串為鍵的自訂 dict

class StrDict(dict):
    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)
    
    def __getitem__(self, key):
        if not str(key) in self:
            self[key] = None
        return dict.__getitem__(self, str(key))

sd = StrDict()
sd[1] = 1
sd[3.14] = 3.14
sd['10'] = 'test'

print(sd[1])
print(sd['3.14'])
print(sd[10])
print(sd['a'])
print(sd)

print('------------------------------------------------------------')	#60個

#練習 43 動物類別

class Animal:
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num
    
    def __repr__(self):
        return f'{self.species}(color={self.color!r}, leg_num={self.leg_num})'

class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

elephant = Elephant('灰')
zebra = Zebra('黑白')
snake = Snake('綠')
parrot = Parrot('灰')

print(elephant)
print(zebra)
print(snake)
print(parrot)

print('------------------------------------------------------------')	#60個

#練習 44 動物展示區類別

class Animal():
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num
    
    def __repr__(self):
        return f'{self.color}色 {self.species} ({self.leg_num} 條腿)'

class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Exhibit():
    def __init__(self, id_num):
        self.id_num = id_num
        self.animals = []
    
    def add_animals(self, *new_animals):
        for animal in new_animals:
            self.animals.append(animal)
    
    def __repr__(self):
        return f'展示區編號 {self.id_num}: ' + \
               f'{", ".join([str(animal) for animal in self.animals])}'

ex1 = Exhibit(1)
ex2 = Exhibit(2)

ex1.add_animals(Elephant('灰'), Zebra('黑白'))
ex2.add_animals(Snake('綠'), Parrot('灰'))

print(ex1)
print(ex2)

print('------------------------------------------------------------')	#60個

#練習 45 動物園類別

class Animal():
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num
    
    def __repr__(self):
        return f'{self.color}色 {self.species} ({self.leg_num} 條腿)'

class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

class Exhibit():
    def __init__(self, id_num):
        self.id_num = id_num
        self.animals = []
        
    def add_animals(self, *new_animals):
        for animal in new_animals:
            self.animals.append(animal)
    
    def __repr__(self):
        return f'展示區編號 {self.id_num}: ' + \
               f'{", ".join([str(animal) for animal in self.animals])}'

class Zoo():
    def __init__(self):
        self.exhibits = []
    
    def add_exhibits(self, *new_exhibits):
        for exhibit in new_exhibits:
            self.exhibits.append(exhibit)
    
    def __repr__(self):
        return '動物園:\n' + \
                   '\n'.join([str(exhibit)
                              for exhibit in self.exhibits])
    
    def animals_by_color(self, color):
        return [animal
                for exhibit in self.exhibits
                for animal in exhibit.animals
                if animal.color == color]
    
    def animal_by_leg_num(self, leg_num):
        return [animal
                for exhibit in self.exhibits
                for animal in exhibit.animals
                if animal.leg_num == leg_num]
    
    def animal_total_leg_num(self):
        return sum([animal.leg_num
                    for exhibit in self.exhibits
                    for animal in exhibit.animals])

zoo = Zoo()
ex1 = Exhibit(1)
ex2 = Exhibit(2)

ex1.add_animals(Elephant('灰'), Zebra('黑白'))
ex2.add_animals(Snake('綠'), Parrot('灰'))
zoo.add_exhibits(ex1, ex2)

print(zoo)
print('灰色動物:', zoo.animals_by_color('灰'))
print('4 條腿動物:', zoo.animal_by_leg_num(4))
print('腿的總數:', zoo.animal_total_leg_num())

print('------------------------------------------------------------')	#60個

#練習 46 自訂列舉容器

class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

myEnum = MyEnumerate('abcde')
for index, letter in myEnum:
    print(f'{index} -> {letter}')

print('------------------------------------------------------------')	#60個

#練習 47 循環取值器

class CycleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value

class CycleList():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CycleIterator(self.data, self.max_times)

clist = CycleList(['a', 'b', 'c'], 5)
for c in clist:
    print(c)

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

#練習 49 產生器運算式

def num_generator(num):
    return (int(digit) for digit in str(num) if digit.isnumeric())

numbers = num_generator(3.14159)

for num in numbers:
    print(num)

print('------------------------------------------------------------')	#60個

#練習 50 能計算時間長度的產生器

import time, random

def elapsed_time_gen():
    last_time = time.perf_counter()
    while True:
        now = time.perf_counter()
        yield now - last_time
        last_time = now

elapsed_time = elapsed_time_gen()

for _ in range(5):
    time.sleep(random.randint(1, 10) / 10)
    print(next(elapsed_time))

print('------------------------------------------------------------')	#60個

#附錄 A-1

def sum_of_two(data, k):
    for a_index, a_value in enumerate(data):
        for b_index, b_value in enumerate(data):
            if a_index != b_index and a_value + b_value == k:
                return [a_index, b_index]
    return []

print(sum_of_two([2, 7, 11, 15], 9))

print('------------------------------------------------------------')	#60個

#附錄 A-2

def find_majority_num(data):
    counter = [(data.count(i), i) for i in set(data)]
    return sorted(counter, reverse=True)[0][1]
    """
    import statistics
    return statistics.mode(data)
    """

print(find_majority_num([1, 2, 2, 3, 2, 3, 1]))

print('------------------------------------------------------------')	#60個

#附錄 A-3

def find_missing_nums(data):
    all_data = set(range(1, len(data) + 1))
    return list(all_data - set(data))

print(find_missing_nums([1, 2, 8, 5, 1, 6, 4, 9, 5]))

print('------------------------------------------------------------')	#60個

#附錄 A-4

class Stack():
    def __init__(this):
        this.data = []
 
    def push(this, x):
        this.data.append(x)
 
    def pop(this):
        if this.data:
            return this.data.pop()
 
    def top(this):
        return this.data[-1]
 
    def min_num(this):
        return min(this.data)

    def max_num(this):
        return max(this.data)

stack = Stack()
stack.push(3)
stack.push(2)
stack.push(8)
stack.push(6)
stack.push(5)
print(stack.pop())
print(stack.top())
print(stack.min_num())
print(stack.max_num())

print('------------------------------------------------------------')	#60個

#附錄 A-5

def are_brackets_valid(s):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
 
    for b in s:
        if b in brackets:
            stack.append(brackets[b])
        else:
            if not (stack and b == stack.pop()):
                return False
    return True if not stack else False

print(are_brackets_valid('[()]'))

print('------------------------------------------------------------')	#60個

#附錄 A-6

def zeroes_to_the_end(data):
    for _ in range(data.count(0)):
        idx = data.index(0)
        data = data[:idx] + data[idx+1:] + data[idx:idx+1]
    return data

print(zeroes_to_the_end([2, 3, 0, 1, 0, 5]))

print('------------------------------------------------------------')	#60個

#附錄 A-7

def find_common_prefix(strs):
    prefix = []
    for c in zip(*strs):
        if len(set(c)) == 1:
            prefix.append(c[0])
        else:
             break
    return ''.join(prefix)

print(find_common_prefix(['expensive', 'export', 'experience']))

print('------------------------------------------------------------')	#60個

#附錄 A-8

def reverse_num_digits(x):
    answer = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
    return answer

print(reverse_num_digits(-123))

print('------------------------------------------------------------')	#60個

#附錄 A-9

def reverse_binary(n):
    binary = f'{n:08b}'
    return int(binary[::-1], 2)

print(reverse_binary(121))

print('------------------------------------------------------------')	#60個

#附錄 A-10

def roman_num_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    roman_special = {
        'IV': -2,
        'IX': -2,
        'XL': -20,
        'XC': -20,
        'CD': -200,
        'CM': -200,
    }
    normal_value = sum([roman[c] for c in s if c in roman])
    special_value = sum([value for key, value in roman_special.items() if key in s])
    return normal_value + special_value

print(roman_num_to_int('MMCDXIX'))

print('------------------------------------------------------------')	#60個



