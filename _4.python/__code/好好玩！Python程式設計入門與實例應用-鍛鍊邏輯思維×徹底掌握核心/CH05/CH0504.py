# 1。使用巢狀if敘述 - 由小而大做條件判斷
score = 64
if score >= 60:
    if score >= 70:
        if score >= 80:            
            if score >= 90:
                print('A')
            else:
                print('B')
        else:
            print('C')
    else:
        print('D')
else:
    print('E')

'''    
# 2.使用巢狀if敘述 - 由小而大做條件判斷

grade = int(input('請輸入分數-> '))
#grade = 68
if grade >= 90:
    print('A')
else:
    if grade >= 80:
        print('B')
    else:
        if grade >= 70:
            print('C')
        else:
            if grade >= 60:
                print('D')
            else:
                print('E')
'''

