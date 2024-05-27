import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    with open(fName, 'r') as f:
        lst = f.readlines()
        for i in range(3):
            st = lst[i].strip()
            print(st)
else:
    print('%s 檔案路徑不存在' %fName)