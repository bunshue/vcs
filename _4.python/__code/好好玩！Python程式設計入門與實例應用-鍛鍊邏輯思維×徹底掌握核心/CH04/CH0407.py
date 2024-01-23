#雙層for建立九九乘法表

# 建立表頭
print('  |', end = '')
for k in range(1, 10):
   #不自動換行，只留空白字元
   print(format(k, '3d'), end = '') 
print() #換行
print('-' * 32)
 
# 第一層 for/in
for one in range(1, 10):
   print(one, '|', end = '')   # 輸出表頭
   # 第二層 for/in
   for two in range(1, 10):
      print(format(one * two, '3d'), end = '')   # 3d 表示欄寬為3
   print() #換行
