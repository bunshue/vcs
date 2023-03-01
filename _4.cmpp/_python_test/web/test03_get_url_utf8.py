#encoding:UTF-8

#百度
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm

import urllib.request   #用來建立請求

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
print(data)

fd = open("bbb.html", "wb")
fd.write(data)
fd.close()

