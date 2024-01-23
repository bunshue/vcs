word = 'Python'

# continue敘述
print('Continue: ', end = ' ')
for cha in word:
    if cha == 't':
        continue # 只中斷此次的執行
    print(cha, end = '')

# break敘述
print('\nBreak: ', end = ' ')
for cha in word:
    if cha == 't':
        break # 中斷廻圈的執行
    print(cha, end = '')
