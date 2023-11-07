page = """
<html>
  <head><title>旗標科技</title></head>
  <body>
    <div class="section" id="main">
      <img alt="旗標圖示" src="http://flag.tw/logo.png">
      <p>產品類別</p>
      <button id="books"><h4 class="bk">圖書</h4></button>
      <button id="maker"><h4 class="pk">創客</h4></button>
      <button id="teach"><h4 class="pk">教具</h4></button>
    </div>
    <div class="section" id="footer">
      <p>杭州南路一段15-1號19樓</p>
      <a href="http://flag.tw/contact">聯絡我們</a>
    </div>
  </body>
</html>
"""

from bs4 import BeautifulSoup
bs = BeautifulSoup(page, 'lxml')

print(bs.title)
print(bs.a)

print(bs.a.text)
print(bs.a.get('href'))
print(bs.a['href'])

print(bs.find('h4'))
print(bs.find('h4', {'class': 'pk'}))
print(bs.find('h4').text)

print(bs.find_all('h4'))
print(bs.find_all('h4', {'class': 'pk'}))

print(bs.find_all(['title', 'p']))
print(bs.find_all(['title', 'p'])[1].text)  #← 傳回第 1 個 (由 0 算起) 符合標籤中的文字

print('h4:', bs.select('h4'))         #←查詢所有 h4 標籤
print('#book:', bs.select('#books'))  #←查詢所有 id 為 'books' 的標籤
print('.pk:', bs.select('.pk'))       #←查詢所有 class 為 'pk' 的標籤
print('h4.bk', bs.select('h4.bk'))    #←查詢所有 class 為 'bk' 的 h4 標籤

print(bs.select('#main button .pk'))

print(bs.select('#main button .pk')[1].text)
print(bs.select('#footer a')[0]['href'])

