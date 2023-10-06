# 7-1-3 用 setdefault 分類資料

data = ['Bucky', 'Lucky', 'Randy', 'Buddy', 'Bolt', 'Larry']
dog_names = dict()

for name in data:
    dog_names.setdefault(name[0], []).append(name)


print(dog_names)