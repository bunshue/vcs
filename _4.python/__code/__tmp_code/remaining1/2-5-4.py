# 2-5-1 Python 舊式字串格式化

errno = 50159747054
name = '鮑勃'

print('嘿, %s, 有錯誤 0x%x 發生了!' % (name, errno))

print('嘿, %(name)s, 有錯誤 0x%(errno)x 發生了!' % {'name': name, 'errno': errno})

# 2-5-2 Python 新式字串格式化

errno = 50159747054
name = '鮑勃'

print('嘿, {}, 有錯誤 0x{:x} 發生了!'.format(name, errno))

print('嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!'.format(name=name, errno=errno))


# 2-5-3 f-string 字串格式化 (Python 3.6+)

errno = 50159747054
name = '鮑勃'

print(f'嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!')

a = 5
b = 10

print(f'5 加 10 等於 {a + b} 而非 {2 * (a + b)}')



# 2-5-4 樣板字串格式化

from string import Template

errno = 50159747054
name = '鮑勃'

templ_string = '嘿 $name, 有錯誤 $error 發生了!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))


