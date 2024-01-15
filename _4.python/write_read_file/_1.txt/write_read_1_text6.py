'''
模式有

r - 讀取(檔案需存在)

w - 新建檔案寫入(檔案可不存在，若存在則清空)

a - 資料附加到舊檔案後面(游標指在EOF)
'''

filename = 'C:/_git/vcs/_1.data/______test_files2/test_write1.txt'

f = open(filename, 'a', encoding = 'UTF-8')   # 也可使用指定路徑等方式，如： C:\A.txt
f.write('你好1\n')
f.write('你好2\n')
f.write('你好3\n')
f.close()

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file3.txt'

f = open(filename)
print(f.readline())
print(f.readline())
#f.close()


f.seek(0)
for line in f:
    print(line.strip())
    
f.close()

with open(filename) as f:
    for line in f:
        print(line.strip())          


filename = 'C:/_git/vcs/_1.data/______test_files2/test_write2.txt'
# write to test_write.txt
# Write a file
with open(filename, "w") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")



filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file4.txt'
text = open(filename).read().strip()
print(text)

print('----------------------------------------------------')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file3.txt'

text = open(filename).read().strip()
print(text)





