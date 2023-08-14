# coding: utf-8
lst1 = [1, 2, 3, 4, 5, 6]
print(lst1[0])
print(lst1[1])
print(lst1[-1])
print(lst1[-2])
lst1[1] = 10
lst1[2] = "Python"
for e in lst1:
    print(e, end=" ")
animals = ['cat', 'dog', 'bat']
for index, animal in enumerate(animals):
    print(index, animal)
lst2 = [[2, 4], ['cat', 'dog', 'bat'], [1, 3, 5]]
print(lst2[1][0])
lst2[2][1] = 7
for e1 in lst2:
    for e2 in e1:
        print(e2, end=" ")
