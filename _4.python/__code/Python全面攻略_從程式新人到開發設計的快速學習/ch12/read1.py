import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    f = open(fName, 'r')
    str1 = f.read(4)
    print(str1)
    print(f.read())
    f.close()
else:
    print('%s 檔案路徑不存在' %fName)