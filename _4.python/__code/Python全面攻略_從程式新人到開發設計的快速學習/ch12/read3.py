import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    with open(fName, 'r') as f:
       lst = f.readlines()
       print(lst[0], end='')
       print(lst[1], end='')
       print(lst[2], end='')
else:
    print('%s 檔案路徑不存在' %fName)
