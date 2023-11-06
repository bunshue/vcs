from urllib.parse import urlparse

o = urlparse("http://www.example.com:80/test/index.php?user=joe")

print('使用urlparse()方法剖析URL網址成為組成的元素')
print("通訊協定: ", o.scheme)
print("網域名稱: ", o.netloc)
print("通訊埠號: ", o.port)
print("網頁路徑: ", o.path)
print("查詢字串: ", o.query)
