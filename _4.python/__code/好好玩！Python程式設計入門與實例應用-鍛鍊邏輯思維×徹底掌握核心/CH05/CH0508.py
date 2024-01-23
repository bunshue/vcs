# for/in廻圈讀取字串，enumerate()加入索引
name = 'Python'
print('%5s'% 'index', '%5s'% 'char')
print('-'*12)
for item in enumerate(name):
    print(' ', item)
