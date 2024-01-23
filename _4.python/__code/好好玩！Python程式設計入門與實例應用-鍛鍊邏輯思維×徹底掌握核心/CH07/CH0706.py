#定義函式
def funcTest(name, score):
    print('定義函式的。。。')
    name = 'Judy'      #情形一
    score.append(83)   #情形二
    print(name, 'id =', id(name))    
    print(score, 'id =', id(score))
    
#呼叫函式
one = 'Mary'; two = [75, 68]
funcTest(one, two)

print('\n呼叫函式時...')
print(one, '分數：', two)

#name不可變物件, score為可變物件
print('one', 'id =', id(one))
print('two', 'id =', id(two))










