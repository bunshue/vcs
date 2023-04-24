import sys

print('打印訊息')

print('有顏色的打印訊息', file=sys.stderr)

print('%s: %s, line %d, column %d' % (
'aaaa', 'bbbb', 123, 456),
file=sys.stderr)

print((
'*** %(file)s:%(lineno)s: 發生錯誤在 "%(token)s"'
) % {
'token': '函數名',
'file': '檔案',
'lineno': '行號'
}, file=sys.stderr)


infile = 'aaaaaaa'
lno = 1234
print('Syntax error on %s:%d' % (infile, lno), 'before:', file=sys.stderr)


print("aaaaaa", file=sys.stdout)


print(__doc__, file=sys.stderr)


byteyears = 1234
print(repr(int(byteyears)).rjust(8))



print(__doc__)
print(globals())


print(sys.version)

print()

print("Python:", sys.version)



print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))

print(sys.platform)

if sys.platform.startswith("win"):
    print('你用的作業系統是Windows')
else:
    print('你用的作業系統不是Windows')


import sys
if sys.platform == 'win32':
    print('Windows')
else:
    print('Non-Windows')




sys.exit(1)	#立刻退出程式
