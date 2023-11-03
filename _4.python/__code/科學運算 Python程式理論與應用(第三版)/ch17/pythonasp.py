# -*- coding:utf-8 -*-
# file: pythonasp.py
#
import os														# 匯入os模組
print('''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Python</title>
</head>
<body>
''')
print('<h1>Python 路徑</h1>')
i = 1
for path in os.sys.path:											# 使用os模組
	print(i, ' ', path)
	print('<br>')
	i = i + 1
print('''
</body>
</html>
''')

