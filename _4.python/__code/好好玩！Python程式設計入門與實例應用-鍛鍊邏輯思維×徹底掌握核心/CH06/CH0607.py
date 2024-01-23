# list.sort()做遞增、遞減排序
name = ['Tom', 'Judy', 'Anthea', 'Charles']

#省略參數，依字母做遞增
name.sort()
print(f'依字母遞增排序：\n{name}')

number = [49, 131, 85, 247]
number.sort(reverse = True) #遞減排序
print('遞減排序：', number)
