import urllib.request
#將想要開啟網址指定給字串變數
addr = 'http://www.drmaster.com.tw/'
#以with/as敘述來取得網址，離開之後會自動釋放資源
with urllib.request.urlopen(addr) as response:
    print('網頁網址',response.geturl())
    print('網頁表頭',response.getheaders())
    print('伺服器狀態碼',response.getcode())
    drmaster= response.read().decode('UTF-8')
print('網頁程式碼如下: ',drmaster)
