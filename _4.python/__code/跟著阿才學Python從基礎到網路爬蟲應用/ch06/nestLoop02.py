name = ["小明","小華","小莉","小呆"]           # 姓名
score = [[77,66,88],[83,92,56],[90,98,79],[89,81,70]]     # 成績   
print('姓名   國文   英文   數學   總分')
print('================================')
for i in range(len(name)):
    print('%s' %name[i], end = '   ')
    sum = 0
    for j in range(len(score[i])):
        print('%3d' %score[i][j], end = '    ')
        sum += score[i][j]
    print('%3d' %sum)

