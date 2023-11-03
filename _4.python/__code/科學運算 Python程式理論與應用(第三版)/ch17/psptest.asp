<%@LANGUAGE=Python%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>use Python in ASP</title>
</head>
<body>
<h1>use Python in ASP</h1>
<%
import os								# 匯入os模組
class Info:								# 定義類別
	def __init__(self):
		Response.Write('<h1>Python Class </h1>')
	def show(self):
		Response.Write('<h1>Class Info</h1>')
def print_br():								# 定義函數
	Response.Write('<br>')
def print_h1(s):
	Response.Write('<h1>')
	Response.Write(s)
	Response.Write('</h1>')
print_h1(u'使用os模組')							# 呼叫函數，使用u表示為unicode
for path in os.sys.path:						# 使用os模組
	Response.Write(path)
	print_br()
print_h1(u'使用string模組')
for s in str.split('Python is great'):				# 使用string模組
	Response.Write(s)
	print_br()
print_h1(u'使用類別')
info = Info()								# 類別案例化
info.show()								# 呼叫類別方法
%>
</body>
</html>
