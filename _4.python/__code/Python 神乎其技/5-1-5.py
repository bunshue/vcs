# 5-1-5 ChainMap: 把多個 dict 當作單一對照表

import collections

dict1 = {'one':1, 'two':2}
dict2 = {'two': '貳', 'three':3, 'four':4}

chain = collections.ChainMap(dict1, dict2)

print(chain)

print(chain['three'])

print(chain['two'])

chain['six'] = 6

print(chain)

for d in chain.maps:
    if 'two' in d:
        d['two'] = 'II'

print(chain)