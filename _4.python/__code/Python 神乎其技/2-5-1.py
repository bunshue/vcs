# 2-5-1 Python 舊式字串格式化

errno = 50159747054
name = '鮑勃'

print('嘿, %s, 有錯誤 0x%x 發生了!' % (name, errno))

print('嘿, %(name)s, 有錯誤 0x%(errno)x 發生了!' % {'name': name, 'errno': errno})