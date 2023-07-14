import time

copyright = '1990-%s, Python Software Foundation' % time.strftime('%Y')

print(copyright)




a_dict = {}
print(type(a_dict))


a_list = []
print(type(a_list))

model = 'aaaa'
year = '2023'
mileage = 1234
money = 123456

message = "{:<10}({}年式)，{:>10,}KM，售價：{:>10,}元"

print(message.format(model, year, mileage, money))


target_url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php'

for page in range(1, 6):
    html = target_url.format(page)
    print(html)


data = list()
for page in range(1, 6):
    pdate = 'aaaa'
    title = 'bbbb'
    link = 'cccc'
    data.append((pdate, link, title))
print(type(data))
print(data)


from bs4 import BeautifulSoup

from platform import python_version
print(python_version())
import bs4
print(bs4.__version__)


contents = list()

for page in range(1, 6):
    content = dict()
    content['link'] = 'aaaaa'
    content['content'] = 'bbbbb'
    content['date'] = 'ccccc'
    content['title'] = 'ddddd'
    contents.append(content)
    
print(contents)


import os
import re
import sys

def get_header_version_info(srcdir):
    print()
    print(srcdir)
    print()
    
    patchlevel_h = os.path.join(srcdir, '..', 'Include', 'patchlevel.h')
    print(patchlevel_h)

def get_sys_version_info():
    major, minor, micro, level, serial = sys.version_info
    release = version = '%s.%s' % (major, minor)
    release += '.%s' % micro
    if level != 'final':
        release += '%s%s' % (level[0], serial)
    return version, release

def get_version_info():
    try:
        return get_header_version_info('.')
    except (IOError, OSError):
        version, release = get_sys_version_info()
        print >>sys.stderr, 'Can\'t get version info from Include/patchlevel.h, ' \
              'using version of this interpreter (%s).' % release
        return version, release

get_header_version_info('.')
print('aaa', get_sys_version_info())
print('bbb', get_version_info())





