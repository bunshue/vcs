#定義函式一
def main():
    # 呼叫函式factorial()
    outcome = factorial(
        port = [5, 11, 17, 23], begin = 1)
    print(f'數值 5, 11, 17, 23 相乘結果: {outcome:,}')
    
# 定義函式二
def factorial(port, begin):
    result = begin #階乘的開始值
    for item in port:
        result *= item #讀進數值並相乘
    return result

#呼叫函式main()
main()

