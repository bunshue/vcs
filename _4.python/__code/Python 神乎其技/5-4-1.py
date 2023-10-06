# 5-4-1 set 集合

vowels = {'a', 'e', 'i', 'o', 'u'}

print('e' in vowels)

vowels.add('x')

print(vowels)

vowels.discard('x')

print(vowels)

letters = set('alice')

print(letters)

print(letters.intersection(vowels))
print(letters & vowels)

print(letters.union(vowels))
print(letters | vowels)

print(letters.difference(vowels))
print(letters - vowels)

print(letters.symmetric_difference(vowels))
print(letters ^ vowels)

subnet = {'a', 'e'}

print(subnet.issubset(letters))
print(subnet <= letters)

print(letters.issuperset(subnet))
print(letters >= subnet)