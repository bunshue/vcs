# 2-5-3 f-string 字串格式化 (Python 3.6+)

errno = 50159747054
name = '鮑勃'

print(f'嘿, {name:s}, 有錯誤 0x{errno:x} 發生了!')

a = 5
b = 10

print(f'5 加 10 等於 {a + b} 而非 {2 * (a + b)}')