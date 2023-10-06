# 5-4-2 frozenset - 不可變的 set

vowels = frozenset({'a', 'e', 'i', 'o', 'u'})

print(vowels)

d = {vowels: 'hello'}

print(d)

#vowels.add('p')