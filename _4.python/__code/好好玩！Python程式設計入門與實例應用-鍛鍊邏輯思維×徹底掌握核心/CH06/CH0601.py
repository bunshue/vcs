# 建立Tuple，+運算子串接
tp1 = 22, 44; tp2 = (11, 33)
print('串接兩個Tuple', tp1 + tp2)

tp3 = 'Mary', 'look' + ' at', ' Tom'
print(tp3)

print('\n數值     索引')
print('-' * 14)

# 建立Tuple，使用index()方法
data = 38, 14, 45, 14, 117
print(f'第1個14{data.index(14):5}')

#index()方法從索引編號2開始
print(f'第2個14{data.index(14, 2):5}')

# 搜尋最後一個要加入邊界值
print(f'   117{data.index(117, 0, 5):5}')
