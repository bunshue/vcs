# coding:utf-8
# 猜數字：幾 A 幾 B

import random

""" 
arr = []
for i in range(9):
    arr.append(i+1)

answer = []
for i in range(4):
    arrLength = int(len(arr)) - 1
    answer.append(arr.pop(random.randint(0, arrLength)))


 """
answer = random.sample(range(1,10), k=4)  # 使用 random.sample
print(answer)

n = 0

while True:
    user = str(input('請輸入四個數字：'))
    a = 0
    b = 0
    n += 1
    result = [0, 0, 0, 0]
    for i in range(4):
        result[i] = int(user[i])
    for i in range(4):
        if (result[i] in answer):
            if(answer[i] == result[i]):
                a += 1
            else:
                b += 1

    print('第 ' + str(n) + ' 次：' + user + \
          ' ( ' + str(a) + ' A ' + str(b) + ' B )')
    if a == 4:
        print('猜中囉')
        break
