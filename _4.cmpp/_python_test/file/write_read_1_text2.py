#各種檔案寫讀範例 txt 2

filename_rw1 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/sample3.txt'

import csv
# 開啟輸出的 csv 檔案
with open(filename_rw1, 'w', newline='') as csvfile:
  # 建立 csv 檔寫入物件
  writer = csv.writer(csvfile)

  # 寫入欄位名稱
  writer.writerow(['姓名', '身高', '體重'])
  # 寫入資料
  writer.writerow(['chiou', 170, 65])
  writer.writerow(['David', 183, 78])


import csv
with open(filename_rw1, 'w', newline='') as csvfile:
    # 定義欄位
    fieldnames = ['姓名', '身高', '體重']

    # 將 dictionary 寫入 csv 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入欄位名稱
    writer.writeheader()
    # 寫入資料
    writer.writerow({'姓名': 'chiou', '身高': 170, '體重': 65})
    writer.writerow({'姓名': 'David', '身高': 183, '體重': 78})




import csv
# 開啟 csv 檔案
with open(filename_rw1, newline='') as csvfile:
    # 讀取 csv 檔案內容
    rows = csv.reader(csvfile)
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row)


import csv
# 開啟 csv 檔案
with open(filename_rw1, newline='') as csvfile:
    # 讀取 csv 檔內容，將每一列轉成 dictionary
    rows = csv.DictReader(csvfile)   
    
    # 以迴圈顯示每一列
    for row in rows:
        print(row['姓名'],row['身高'],row['體重'])






filename_rw2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/sample5.txt'

content='''Hello Python
中文字測試
Welcome
'''

f=open(filename_rw2, 'w')
f.write(content)
f.close()


content='''Hello Python
中文字測試
Welcome
'''

f=open(filename_rw2, 'w',encoding='UTF-8')
f.write(content)
f.close()



f=open(filename_rw2, 'r',encoding='UTF-8')
for line in f:
    print(line,end="")
f.close()

with open(filename_rw2, 'r',encoding='UTF-8') as f:
    for line in f:
        print(line,end="")


with open(filename_rw2, 'r',encoding='UTF-8') as f:
    str1=f.read(5)
    print(str1)  # Hello


with open(filename_rw2, 'r',encoding='UTF-8') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)



with open(filename_rw2, 'r',encoding ='UTF-8') as f:
    content=f.readlines() 
    print(content)      
    
f=open(filename_rw2, 'r',encoding ='UTF-8')
str1=f.read(5)
print(str1)  # 123中
f.close()


with open(filename_rw2, 'r',encoding ='UTF-8-sig') as f:
    content=f.readlines() 
    print(content)      
    
f=open(filename_rw2, 'r',encoding ='UTF-8-sig')
str1=f.read(5)
print(str1)  # 123中文
f.close()


f=open(filename_rw2, 'r',encoding ='UTF-8-sig')
print(f.readline())  # 123中文字\n
print(f.readline(3)) # abc
f.close()
'''
f=open(filename_rw2, 'r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()
'''

filename_rw3 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/Presidents.txt'

# Open file for output
outfile = open(filename_rw3, "w")

# Write data to the file
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama")

outfile.close() # Close the output file


filename_rw4 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/Info.txt'
# Open file for appending data
outfile = open(filename_rw4, "a")
outfile.write("\nPython is interpreted\n")
outfile.close() # Close the input file



import random

filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/numbers.txt'

# Open file for writing data
outfile = open(filename, "w")
for i in range(10):
    outfile.write(str(random.randint(0, 9)) + " ")
outfile.close() # Close the file

# Open file for reading data
infile = open(filename, "r")
s = infile.read()
numbers = [eval(x) for x in s.split()]
for number in numbers:
    print(number, end = " ")
infile.close() # Close the file





filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/Presidents.txt'

fp = open(filename, "r")
zops = fp.readlines()
fp.close()

i=1
print("檔案內容")
for zen in zops:
    print("第 {} 行 : {}".format(i, zen), end="")
    i += 1

print()





print('測試完成')

    



