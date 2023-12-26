# ex11_18.py
mylist = [5, 10, 15, 20, 25, 30]

evenlist = list(filter(lambda x: (x % 2 == 0), mylist))

# 輸出偶數串列
print("偶數串列: ",evenlist)

