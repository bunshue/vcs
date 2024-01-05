def swap_test(x,y):
    print('函數內交換前：x=%d, y=%d' %(x,y))
    x,y=y,x #交換過程
    print('函數內交換前：x=%d, y=%d' %(x,y))     

a=10
b=20 #設定a,b的初值
print('函數外交換前：a=%d, b=%d' %(a,b))
swap_test(a,b) #函數呼叫
print('函數外交換後：a=%d, b=%d' %(a,b))
