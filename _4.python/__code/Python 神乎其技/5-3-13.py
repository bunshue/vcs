# 5-3-13 strut.Strut - C 語言序列化結構

from struct import Struct

MyStruct = Struct('i?f')

data = MyStruct.pack(23, False, 42.0)

print(data)

print(MyStruct.unpack(data))