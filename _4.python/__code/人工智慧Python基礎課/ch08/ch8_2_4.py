lst1 = [4, 2, 8, 9, 1]
print("lst1 = " + str(lst1))
s = len(lst1)
print("len(lst1) = " + str(s))
s = max(lst1)
print("max(lst1) = " + str(s))
s = min(lst1)
print("min(lst1) = " + str(s))
str1 = 'Hello World!'
lst2 = list(str1)
print("lst2 = " + str(lst2))
for i, v in enumerate(lst2, 0):
    print(i, ":", v, end=" ")
print()
s = sum(lst1)
print("sum(lst1) = " + str(s)) 
lst3 = sorted(lst1)
print("lst3 = sorted(lst1) = " + str(lst3))
 