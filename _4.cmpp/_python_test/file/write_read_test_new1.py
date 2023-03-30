#各種檔案寫讀範例 新進暫存


from random import randint

filename = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/numbers.txt'

# Open file for writing data
outfile = open(filename, "w")
for i in range(10):
    outfile.write(str(randint(0, 9)) + " ")
outfile.close() # Close the file

# Open file for reading data
infile = open(filename, "r")
s = infile.read()
numbers = [eval(x) for x in s.split()]
for number in numbers:
    print(number, end = " ")
infile.close() # Close the file













print('測試完成')

    


'''


fp = open("data\article.txt", "r")
zops = fp.readlines()
fp.close()
i=1
print("The Zen of Python")
for zen in zops:
    print("Zen {}: {}".format(i, zen),end="")
    i += 1



import sys, ast

filename = 'scores.csv'

scores = dict()
with open(filename,'r') as fp:
    filedata = fp.read()
    #scores = ast.literal_eval(filedata)
print("以下是{}成績檔的字典型態資料:".format(filename))




import sys

std_data = dict()
with open(filename, encoding='utf-8') as fp:
    alldata = fp.readlines()
    for item in alldata:
        no, name = item.rstrip('\n').split(',')
        std_data[no] = name
print(std_data)






#readlines()可以依照行讀取整個檔案，回傳是一個List，每一個element就是一行字。

file = open("demo_en.txt", "r")

lines = file.readlines()
print(lines)

file.close()






'''
