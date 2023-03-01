#encoding:Big5

#Perl的基本語法
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm

import urllib.request   #用來建立請求

url = "http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm"
data = urllib.request.urlopen(url).read()
data = data.decode('Big5')      #將bytes轉成str
print(data)

fd = open("perl.html", "w")
fd.write(data)
fd.close()


