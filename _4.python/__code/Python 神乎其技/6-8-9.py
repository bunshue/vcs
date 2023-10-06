# 6-8-9 itertools 模組: groupby() 給連續資料分組

import itertools

data = ['a', 'a', 'a', 'b', 'b', 'b', 'a', 'a', 'c', 'c', 'd']

for key, item in itertools.groupby(data):
    print(key, list(item))

print('')
data.sort()

for key, item in itertools.groupby(data):
    print(key, list(item))


print('')
data = ['Python', 'Java', 'C#', 'Perl', 'Basic', 'Go', 'COBOL', 'Ruby']
data.sort(key=len)

for key, item in itertools.groupby(data, len):
    print(key, list(item))


print('')
first_letter = lambda i: i[0]
data.sort(key=first_letter)

for key, item in itertools.groupby(data, first_letter):
    print(key, list(item))