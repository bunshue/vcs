"""
读取圆周率文件判断其中是否包含自己的生日

"""

birth = input('请输入你的生日: ')
with open('pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')
