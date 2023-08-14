# coding: utf-8
lst1 = [1, 5]
lst1.append(7)
print(lst1)
lst1.extend([9, 11, 13])
print(lst1)
lst1.insert(1, 3)
print(lst1)
del lst1[2]
print(lst1)
e1 = lst1.pop()
print(e1, lst1)
e2 = lst1.pop(1)
print(e2, lst1)
lst1.remove(9)
print(lst1)
