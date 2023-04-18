import sys

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



print(__doc__)
print(globals())




print("Python:", sys.version)



