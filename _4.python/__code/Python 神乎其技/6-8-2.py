# 6-8-2 itertools 模組: cycle() 無限循環

import itertools

for item in itertools.cycle(range(3)):
    print(item)