# coding: utf-8
d1 = {"chicken": 2, "dog": 4, "cat":3}
print(d1["cat"])
print(d1["dog"])
print(d1["chicken"])
d1["cat"] = 4
print(d1)
d1["spider"] = 8
print(d1)
for animal in d1:
    legs = d1[animal]
    print(animal, legs)
for animal, legs in d1.items():
    print("動物: {0} 有 {1} 隻腳".format(animal, legs))
