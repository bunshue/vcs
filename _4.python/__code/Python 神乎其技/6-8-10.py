# 6-8-10 itertools 模組: tee() 同單一來源建立多個走訪器

import itertools

data = [1, 2, 3, 4, 5]

generators = itertools.tee(data, 3)

for g in generators:
    print(list(g))