# encoding:UTF-8


def inn():
    a = input('輸入文字並轉換為 ASCII：')
    print('{} 的 ASCII：{}'.format(a, ord(a)))
    inn()


inn()
