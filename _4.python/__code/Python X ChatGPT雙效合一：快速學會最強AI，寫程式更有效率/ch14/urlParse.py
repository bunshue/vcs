from urllib.parse import urlparse

addr = 'http://www.drmaster.com.tw/Bookinfo.asp?BookID=MI22004'

result = urlparse(addr)
print('回傳的 ParseResult 物件:')
print(result)
print('通訊協定:'+result.scheme)
print('網站網址:', result.netloc)
print('路徑:', result.path)
print('查詢字串:', result.query)
