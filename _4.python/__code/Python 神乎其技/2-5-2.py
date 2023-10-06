# 2-5-2 Python 新式字串格式化

errno = 50159747054
name = '鮑勃'

print('嘿, {}, 有錯誤 0x{:x} 發生了!'.format(name, errno))

print('嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!'.format(name=name, errno=errno))