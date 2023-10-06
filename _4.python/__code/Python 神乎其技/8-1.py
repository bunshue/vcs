# 8-1 以 dir() 與 help() 探索 Python 模組與物件

import datetime

print(dir(datetime))

print('')

print([_ for _ in dir(datetime) if 'date' in _.lower()])

#help(datetime)