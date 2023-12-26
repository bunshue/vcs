# ch10_16.py
animals = {'dog', 'cat', 'bird'}
print("刪除前的animals集合    ", animals)
# 欲刪除元素有在集合內
animals.discard('cat')        
print("刪除後的animals集合    ", animals)
# 欲刪除元素沒有在集合內 
animals.discard('pig')
print("刪除後的animals集合    ", animals)
# 列印傳回值
print("刪除資料存在的傳回值   ", animals.discard('dog'))
print("刪除資料不存在的傳回值 ", animals.discard('pig'))


