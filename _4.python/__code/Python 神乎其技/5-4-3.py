# 5-4-3 Counter - 多重集合 (計數器)

from collections import Counter

inventory = Counter()

loot = {'寶劍':1, '麵包':3}
inventory.update(loot)

print(inventory)

more_loot = {'寶劍', '金幣'}
inventory.update(more_loot)

print(inventory)

yet_more_loot = ['麵包', '麵包', '藥草']
inventory.update(yet_more_loot)

print(inventory)

print('鍵種類 =', len(inventory))

print('值總和 =', sum(inventory.values()))