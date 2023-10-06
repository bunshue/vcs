# 5-1-6 MappingProxyType: 給 dict 加上唯讀包裝層

from types import MappingProxyType

writable = {'一':1, '二':2}
readonly = MappingProxyType(writable)

print(readonly['一'])

writable['一'] = 42

print(readonly['一'])

#readonly['一'] = 23