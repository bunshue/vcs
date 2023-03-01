"""
import urllib.request   #用來建立請求

url = "http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm"
a = urllib.request.urlopen(url)
print("type : ")
print(type(a))
print("info : ")
print(a.info())

print("geturl : ")
print(a.geturl())
print("getcode : ")
print(a.getcode())
print("getheaders : ")
print(a.getheaders())
print("length : ")
print(a.length)
print("version : ")
print(a.version)

data = a.read()
#data = data.decode('UTF-8')
#print(data)

fd = open("tmp.html", "wb")
fd.write(data)
fd.close()
"""

import urllib
import urllib.request
 
data={}
data['word']='明仁天皇'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
#data=data.decode('UTF-8')
print(data)

fd = open("b2.html", "wb")
fd.write(data)
fd.close()

