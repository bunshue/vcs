#encoding:Big5

#Perl���򥻻y�k
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm

import urllib.request   #�Ψӫإ߽ШD

url = "http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm"
data = urllib.request.urlopen(url).read()
data = data.decode('Big5')      #�Nbytes�নstr
print(data)

fd = open("perl.html", "w")
fd.write(data)
fd.close()


