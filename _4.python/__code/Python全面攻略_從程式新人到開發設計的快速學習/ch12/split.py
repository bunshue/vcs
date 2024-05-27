import os
fName = 'C:/pcYah/score.txt'
if os.path.isfile(fName):
    print ('姓名','國文','數學','平均',sep='\t')
    with open(fName, 'r') as f:
       lst = f.readlines()
       for i in range(3):
           st = lst[i].strip()
           stA = st.split(',')
           print(stA[0], end='\t')
           print(stA[1], end='\t')
           print(stA[2], end='\t')
           avg = (float(stA[1])+float(stA[2]))/2
           print(avg)
else:
    print('%s 檔案路徑不存在' %fName)