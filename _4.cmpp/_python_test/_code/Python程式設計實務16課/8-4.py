# _*_ coding: utf-8 _*_
# 程式 8-4.py (Python 3 version)

import sys

if len(sys.argv)<2:
    print("使用方法：python 8-4.py 成績檔案")
    exit(1)

no=1
scores=dict()
while True:
    score = int(input('請輸入第{}號的成績:(-1結束)'.format(no)))
    if score == -1: break;
    scores[no] = score
    no += 1    

with open(sys.argv[1],'w') as fp:
    fp.write(str(scores))
print("{}已被儲存完畢".format(sys.argv[1]))
