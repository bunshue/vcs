# 5-1-3 defaultdict: 找不到鍵時會新增元素

import collections

dd = collections.defaultdict(lambda: '小汪')

dd['Bucky'] = '小八'
dd['Lucky'] = '來福'

print(dd.keys())

print(dd['Randy'])

print(dd.keys())