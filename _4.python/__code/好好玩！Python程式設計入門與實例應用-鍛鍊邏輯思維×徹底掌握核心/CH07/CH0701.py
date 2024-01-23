# 自訂函式
# step 1.定義函式 - 傳入兩個數值，比較它們的大小
def funcMax(n1, n2):
    if n1 > n2:
        result = n1
    else:
        result = n2
    return result

# step 2.呼叫函式
num1, num2 = eval(input('輸入兩個數值：'))
print('較大值', funcMax(num1, num2))
