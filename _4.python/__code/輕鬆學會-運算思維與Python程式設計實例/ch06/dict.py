labor = {'高中仁':'RD', '許富強':'SA'} #設定字典的資料
labor['陳月風'] = 'CEO' #新增一個項目
labor.setdefault('陳月風')
print('目前字典:')
print(labor)
labor['陳月風'] ='PRESIDENT' 
#以update()方法更新字典
labor.update({'周慧宏':'RD', '鄭大富':'SA'})
print('依名字遞增排序:')
for key in sorted(labor):
    print('%8s %9s' % (key, labor[key]))

person = {'陳志強':'SA','蔡工元':'RD'}
labor.update(person) # 更新字典
labor.update(胡慧蘭 = 'RD', 周大全 = 'SA')#以指派方式更新
print('更新字典內容：\n', labor)
labor.pop('陳志強')#刪除指定資料
print('刪除後依名字排序:')
for value in sorted(labor, reverse = False):
    print('%8s %9s' % (value, labor[value]))
print('將字典內容清空:')
print(labor.clear())
print(labor)#輸出字典
