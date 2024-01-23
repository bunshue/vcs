# 自訂函式，return有多個回傳值
# step1 自訂函式
def funcMulti(a, b):
    return a+b, a*b, a/b
    
#呼叫函式
one, two = eval(input('輸入兩個數值做運算:'))
result = funcMulti(one, two)
print('運算結果:')
# 針對每一個Tuple元素做格式化
print('加 = {0[0]:6d} \n乘 = {0[1]:,d}\
      \n除 = {0[2]:11.4f}'.format(result))
