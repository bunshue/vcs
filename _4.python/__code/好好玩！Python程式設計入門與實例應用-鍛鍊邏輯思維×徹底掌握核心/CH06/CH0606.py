# List呼叫append()方法新增元素

ambit = 5    # 設定range()函式範圍
friends = [] # 建立空的串列

# 以for廻圈讀取資料
print('請輸入5個名字：')
for item in range(ambit):
   name = input() # 取得輸入名稱   
   # 將輸入名字以append()方法新增到List
   if name != '':
       friends.append(name)
else:
   print('輸入完畢...')

# 輸出資料
print('名字', end = '->')
for item in friends:   
   print(f'{item:7}', end = '')
