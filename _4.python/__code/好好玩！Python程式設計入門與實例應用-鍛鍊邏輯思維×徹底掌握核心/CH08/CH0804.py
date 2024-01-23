from CH0803 import number #匯入模組

count = 1 #統計次數
guess = 0 #儲存輸入數值

while guess != number :
   guess = int(input('輸入1~100之間的數字->'))
   # if/elif 敘述來反應猜測狀況
   if guess == number:
      print(f'第{count}次猜對，數字：{number}')
   elif guess >= number:
      print('數字太大了')
   else:
      print('數字太小了')
   count += 1
