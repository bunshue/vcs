import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個



import platform
print(platform.win32_ver())
print(platform.platform())



print('------------------------------------------------------------')	#60個

import re

pat = re.compile('[a-z]+')

m = pat.findall('tem12po')
print(m)  # ['tem', 'po']




print('------------------------------------------------------------')	#60個


import time
import datetime

def _format_time(hh, mm, ss, us):
    # Skip trailing microseconds when us==0.
    result = "%02d:%02d:%02d" % (hh, mm, ss)
    if us:
        result += ".%06d" % us
    return result

year = 2023
month = 8
day = 11
sep = 'W'
hour = 12
minute = 34
second = 56
microsecond = 123456
s = _format_time(hour, minute, second, microsecond)
print(s)


s = ("%04d-%02d-%02d%c" % (year, month, day, sep) +
     _format_time(hour, minute, second,microsecond))
print(s)


hh = 12
mm = 34
ss = 56
s = "%d:%02d:%02d" % (hh, mm, ss)
print(s)





print('------------------------------------------------------------')	#60個



import os, string


print('字典範例')
codecs = {
    'cn': ('gb2312', 'gbk', 'gb18030', 'hz'),
    'tw': ('big5', 'cp950'),
    'hk': ('big5hkscs',),
    'jp': ('cp932', 'shift_jis', 'euc_jp', 'euc_jisx0213', 'shift_jisx0213',
           'euc_jis_2004', 'shift_jis_2004'),
    'kr': ('cp949', 'euc_kr', 'johab'),
    'iso2022': ('iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2',
                'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext',
                'iso2022_kr'),
}

print(type(codecs))
print(codecs)

for loc, encodings in codecs.items():
    for enc in encodings:
        print(enc)


print('------------------------------------------------------------')	#60個





import re
import sys
import time
import random


_FMT = '[Non-text (%(type)s) part of message omitted, filename %(filename)s]'
print(_FMT)

_width = len(repr(sys.maxsize-1))
_fmt = '%%0%dd' % _width

print(_width)
print(_fmt)

token = random.randrange(sys.maxsize)
print(token)
boundary = ('=' * 15) + (_fmt % token) + '=='
print(boundary)



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個













'''

        return "%s %s %2d %02d:%02d:%02d %04d" % (
            _DAYNAMES[weekday],
            _MONTHNAMES[self._month],
            self._day,
            self._hour, self._minute, self._second,
            self._year)




'''
