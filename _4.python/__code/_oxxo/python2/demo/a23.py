import re

# 取出一段文字中的阿拉伯數字
a = '123 + 456'
b = re.findall(r'\d+', a.replace(' ', ''))
print(b)

# 取出一段文字中的「非」阿拉伯數字
c = 'hello 123 !!!'
d = re.findall(r'\D+', c.replace(' ', ''))
print(d)

# 取出每個非空白字元
msg1 = 'hello world!!'
msg1r = re.findall(r'\S', msg1)
print(msg1r)


# 替換指定區間文字
msg2 = 'hello {name}, {age}'
msg2r = re.findall(r'\{.+?\}', msg2)
print(msg2r)
text = {
    'name': 'oxxo',
    'age': '18'
}
for i in range(0, len(msg2r)):
    o = re.sub(r'\{|\}', '', msg2r[i])
    msg2 = re.sub(msg2r[i], text[o], msg2)

print(msg2)

aa = 'abc'
aa = aa + 'def'
print(aa)
