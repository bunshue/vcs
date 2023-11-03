# -*- coding:utf-8 -*-
# file: pythontest.py
#
from mod_python import apache
def handler(req):
	req.content_type = 'text/html'
	req.write('''
	<html>
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Python</title>
	</head>
	<body>
	<h1>mod_python<h1>
	</body>
	</html>
  	''')
	return apache.OK
