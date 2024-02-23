# encoding:UTF-8
import time

a = input('請輸入倒數的秒數：')
if(a.isdigit()):
    a = int(a)
    while(a > 0):
        print(a)
        a = a - 1
        time.sleep(1)
    print('時間到！')
else:
  print('你輸入的不是數字呦～')