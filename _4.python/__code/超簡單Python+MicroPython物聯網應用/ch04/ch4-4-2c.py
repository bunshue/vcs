d1 = {"chicken": 2, "dog": 4, "cat":3}
for animal in d1:
    legs = d1[animal]
    print(animal, legs, end=" ")
print()
for animal, legs in d1.items():
    print("動物: {} 有 {} 隻腳".format(animal, legs))
    