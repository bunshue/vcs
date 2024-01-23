# 自訂函式，呼叫main()，它會呼叫cubeV

# 定義函式一main()
def main():
    number = int(input('輸入數值：'))
    result = funCube(number)
    
# 自訂函式二 funCube
def funCube(num):
    print('立方值：')
    for item in range(1, num + 1):
        result = item ** 3
        print(format(result, ','), end = ' ')  

# 呼叫主程式
main()
