# step1 定義函式：有3個參數，運算值以return敘述回傳
def total(start, finish, step):
    outcome = 0 # 儲存計算結果
    for item in range(num1, num2+1, num3):
        outcome += item # 儲存相加結果
    return outcome

print('計算數值總和')
num1, num2, num3 = eval(input(
    '輸入起始值, 終止值, 間距值-> '))

#2.呼叫自訂函式total 
result = total(num1, num2, num3)
# 單一變數，呼叫 BIF format()做格式化輸出
print(f'總和 = {result:,}')

    
