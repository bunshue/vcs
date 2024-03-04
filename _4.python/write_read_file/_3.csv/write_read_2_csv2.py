import pathlib
import csv

infile = "data/namelist.csv"
f = pathlib.Path(infile).open(encoding="UTF-8")
dataReader = csv.reader(f)
for row in dataReader:          #取得每一列資料
    for value in row:           #取得資料時，以逗號間隔
        print(value)
        
print("------------------------------------------------------------")  # 60個

import pathlib
import csv

infile = "xxxxx.csv"
try:
    f = pathlib.Path(infile).open(encoding="UTF-8")
    dataReader = csv.reader(f)
    for row in dataReader:          #取得每一列資料
        for value in row:           #取得資料時，以逗號間隔
            print(value)
except:
    print("無法載入檔案。")

print("------------------------------------------------------------")  # 60個

import csv

filename = 'data/csvReport2.csv'
with open(filename) as csvFile:               # 開啟csv檔案
    csvReader = csv.reader(csvFile)     # 讀檔案建立Reader物件
    listReport = list(csvReader)        # 將資料轉成串列
total2025 = 0
total2026 = 0
for row in listReport:
    if row[0] == 'Steve':
        if row[1] == '2025':
            total2025 += int(row[5])
        if row[1] == '2026':
            total2026 += int(row[5])

print("Steve's Total Revenue of 2025 = ", total2025)
print("Steveis Total Revenue of 2026 = ", total2026)

print("------------------------------------------------------------")  # 60個

print('2025年1月台北天氣報告')

import csv

filename = 'data/TaipeiWeatherJan.csv'
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)          # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []                       
    for row in csvReader:
        highTemps.append(int(row[1]))    # 儲存最高溫
        meanTemps.append(int(row[2]))    # 儲存均溫
        lowTemps.append(int(row[3]))     # 儲存最低溫

print('高溫', highTemps)
print('均溫', meanTemps)
print('低溫', lowTemps)

print("------------------------------------------------------------")  # 60個

import ast

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores.csv'

scores = dict()
with open(filename,'r') as fp:
    filedata = fp.read()
    #scores = ast.literal_eval(filedata)
print("以下是{}成績檔的字典型態資料:".format(filename))

print("------------------------------------------------------------")  # 60個

import csv

#擷取登入帳號資訊

def passwd_to_dict(filename):
    users = {}
    with open(filename) as f:
        for line in f:
            user_info = line.split(':')
            users.update({user_info[0]: user_info[2]})
    return users

print(passwd_to_dict(r'.\data\passwd.cfg'))

#擷取登入帳號資訊（生成版）

def passwd_to_dict_2(filename):
    with open(filename) as f:
        d = {words[0]: words[2]
             for words
             in [line.split(':') for line in f]}
    return d

print(passwd_to_dict_2(r'.\data\passwd.cfg'))


def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename, 'r') as f_read, \
            open(csv_filename, 'w', newline='') as f_write:
        csv_reader = csv.reader(f_read, delimiter=':')
        csv_writer = csv.writer(f_write, delimiter='\t', lineterminator='\n')
        for line in csv_reader:
            csv_writer.writerow([line[0], line[2]])

passwd_to_csv(r'.\data\passwd.cfg', r'tmp_passwd.csv')

print('------------------------------------------------------------')	#60個

import csv

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/animals.csv'

try:
    with open(filename, encoding = 'utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print('无法打开文件:', filename)
else:
    for item in data:
        print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))

print('------------------------------------------------------------')	#60個

import csv

csvfile = "data/Example.csv"
with open(csvfile, 'r') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(','.join(row))

print("------------------------------------------------------------")  # 60個

import csv

csvfile = "data/Example2.csv"
list1 = [[10,33,45], [5, 25, 56]]
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["Data1","Data2","Data3"])
    for row in list1:
        writer.writerow(row)

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

