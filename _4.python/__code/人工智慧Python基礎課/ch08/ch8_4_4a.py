d1 = {"tom":2, "bob":3, "mike":4}
print("d1 = " + str(d1))
i = d1.get("tom")
print("d1.get('tom') = " + str(i))
i = d1.get("jerry", "不存在")
print("d1.get('jerry', '不存在') = " + str(i))
t1 = d1.keys()
print("d1.keys() = " + str(t1))
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")
print()
t1 = d1.values()
print("d1.values() = " + str(t1))
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")