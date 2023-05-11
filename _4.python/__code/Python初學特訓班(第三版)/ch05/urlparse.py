from urllib.parse import urlparse
url = 'http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1'
o = urlparse(url)
print(o) 

print("scheme={}".format(o.scheme)) # http
print("netloc={}".format(o.netloc)) # taqm.epa.gov.tw
print("port={}".format(o.port))     # 80
print("path={}".format(o.path))     # /pm25/tw/PM25A.aspx
print("query={}".format(o.query))   # area=1