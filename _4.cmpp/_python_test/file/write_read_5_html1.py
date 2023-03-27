pre_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>中油油價歷史資料</title>
</head>
<body>
<h2>中油油價歷史資料（取自中油官方網站）</h2>
<table width=600 border=1>
<tr><td>日期</td><td>92無鉛</td><td>95無鉛</td><td>98無鉛</td></tr>
'''

post_html = '''
</table>
</body>
</html>
'''
prices = list()
#item = [cols[0].text, cols[1].text, cols[2].text, cols[3].text]
prices.append('1234')

html_body = ''
for p in prices:
    html_body += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".\
          format(p[0],p[1],p[2],p[3])
html_file = pre_html + html_body + post_html

fp = open('oilprice.html','w')
fp.write(html_file)
fp.close()
