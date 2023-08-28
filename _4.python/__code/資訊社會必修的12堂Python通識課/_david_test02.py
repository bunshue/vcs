import requests


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



'''
import urllib.request, json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'
with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
    print(data)
'''

    
'''
import urllib.request, json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'
with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
    for k in data['retVal'].keys():
        print("{:>2}/{:>2}\t{}".format(
            data['retVal'][k]['sbi'],
            data['retVal'][k]['tot'],
            data['retVal'][k]['sna']))
'''

import urllib.request, json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'
with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
    msg = "<table>"
    for k in data['retVal'].keys():
        msg += "<tr><td>{:>2}</td><td>{:>2}</td><td>{}</td></tr>".format(
            data['retVal'][k]['sbi'],
            data['retVal'][k]['tot'],
            data['retVal'][k]['sna'])
    msg += "</table>"
    
html = """
<!DOCTYPE html>
<html>
  <head>
    <title>{}</title>
  </head>
  <body>
  {}
  </body>
</html>
""".format("桃園公共自行車各站可租數量", msg)
with open("taoyouan-bike-v1.html", "wt", encoding='utf-8') as fp:
    fp.write(html)
print("Done!")


from dominate import document
html = document("My Title")
print(html)


from dominate import document
from dominate.tags import *
html = document("桃園公共自行車各站可租數量")
with html.head:
    meta(charset='utf-8')
with html.body:
    h1("這是一個示範網頁")
    hr()
    p("這是一個段落")
    p("這是另外一個段落，以下示範的是清單")
    items = ul()
    items += li("第一點")
    items += li("這是第二點")
with open("sample.html", "wt", encoding='utf-8') as fp:
    fp.write(str(html))
print("Done!")




#以表格的方式呈現公共自行車租借站資訊
import dominate
from dominate.tags import *
import urllib.request, json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'
with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
html = dominate.document(title="桃園公共自行車各站可租數量")
with html.head:
    meta(charset="utf-8")
with html:
    h1("桃園公共自行車各站可租數量")
    hr()
    with table():     
        head = tr(bgcolor='#888888')
        head += td("站名")
        head += td("可租數量")
        head += td("自行車總量")
        head += td("本站位置")
        for index, k in enumerate(data['retVal'].keys()):
            if index % 2 == 0:
                row = tr(bgcolor='#ccffcc')
            else:
                row = tr(bgcolor='#ffccff')
            row += td(data['retVal'][k]['sna'])
            row += td(data['retVal'][k]['sbi'])
            row += td(data['retVal'][k]['tot'])
            row += td(data['retVal'][k]['ar'])
with open("taoyuan-bike-list.html", "wt", encoding='utf-8') as fp:
    fp.write(str(html))
print("Done!")




import dominate
from dominate.tags import *
from dominate.util import raw
import urllib.request, json
url = 'https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f'
with urllib.request.urlopen(url) as jsonfile:
    data = json.loads(jsonfile.read().decode())
html = dominate.document(title="桃園公共自行車各站可租數量")
with html.head:
    meta(charset="utf-8")
    script(src="http://code.jquery.com/jquery-3.3.1.slim.js", 
           integrity="sha256-fNXJFIlca05BIO2Y5zh1xrShK3ME+/lYZ0j+ChxX2DA=",
           crossorigin="anonymous")
    cmd = '''
$(document).ready(function() {
    $("#bike-station").change(function() {
        $('#target').html($("select option:selected").val())
    });
});
'''
    script(raw(cmd))
with html:
    h1("桃園公共自行車各站可租數量查詢")
    hr()
    p("請選擇自行車租借站：")
    with form(method="POST"):
        with select(id='bike-station'):
            for k in data['retVal'].keys():
                option(value="{}/{}".format(
                    data['retVal'][k]['sbi'],
                    data['retVal'][k]['tot'])).add(
                    data['retVal'][k]['sna'])
    d = div()
    d += h3("可租借數量/總數：")
    d += span(id="target")
with open("taoyuan-bike.html", "wt", encoding='utf-8') as fp:
    fp.write(str(html))
print("Done!")




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



