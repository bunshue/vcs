from random import randint

#產生10~100的整數亂數
num1, num2 = eval(input(
    '請輸入小於100的兩個數值來產生隨意值：'))
number = randint(num1, num2)

if __name__ == '__main__':
    print('我是主程式')
print('隨意數值：', number)
