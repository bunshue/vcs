# 使用if/elif敘述來逐一過濾條件
score = int(input('請輸入分數-> '))

if score <= 60:
   print('請多多努力！')
elif score <= 70:
   print('表現尚可！')
elif score <= 80:
   print('不錯噢')
elif score <= 90:
   print('好成績')
else:
   print('非常好！')
'''

score = int(input('請輸入分數-> '))
if score >= 90:
   print('非常好！')
elif score >= 80:
   print('好成績！')
elif score >= 70:
   print('不錯噢')
elif score >= 60:
   print('表現尚可')
else:
   print('請多多努力！')'''

