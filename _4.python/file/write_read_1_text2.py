#各種檔案寫讀範例 txt 2


filename_rw2 = 'C:/______test_files3/sample5.txt'

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

filename_rw3 = 'C:/______test_files3/Presidents.txt'

# Open file for output
outfile = open(filename_rw3, "w")

# Write data to the file
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama")

outfile.close() # Close the output file


filename_rw4 = 'C:/______test_files3/Info.txt'
# Open file for appending data
outfile = open(filename_rw4, "a")
outfile.write("\nPython is interpreted\n")
outfile.close() # Close the input file



import random

filename = 'C:/______test_files3/numbers.txt'

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





filename = 'C:/_git/vcs/_1.data/______test_files1/Presidents.txt'

fp = open(filename, "r")
zops = fp.readlines()
fp.close()

i=1
print("檔案內容")
for zen in zops:
    print("第 {} 行 : {}".format(i, zen), end="")
    i += 1

print()



print('讀出檔案 1 英文')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_en.txt'
file = open(filename, "r")

content = file.read()
print(content)

file.close()

print('讀出檔案 2 中文')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_ch.txt'
file = open(filename, "r", encoding="utf-8")

content = file.read()
print(content)

file.close()

print('讀出檔案 3')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_en.txt'
file = open(filename, "r")

lines = file.readlines()
print(lines)

file.close()

print('讀出檔案 4')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_en.txt'
with open(filename, "r") as file:
    content = file.read()
    print(content)


print('寫入檔案')
filename = 'C:/______test_files3/demo_en222.txt'

file = open(filename, "a")

file.write("Take me home, country road\n")

file.close()




print('測試完成')

    



