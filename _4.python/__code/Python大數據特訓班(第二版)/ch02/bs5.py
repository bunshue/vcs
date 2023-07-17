html = """
<html><head><title>網頁標題</title></head>
<h1>文件標題</h1>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">Third
    </a>
</div>
"""

from bs4 import BeautifulSoup
sp = BeautifulSoup(html,'lxml') 

print(sp.title) # <title>網頁標題</title>

print(sp.find('h1')) # <h1>文件標題</h1>

print(sp.find_all('a')) 
print(sp.find_all("a", {"class":"red"}))

data1=sp.find("a", {"href":"http://example.com/one"})
print(data1.text) # First

data2 = sp.select("#link1") 
print(data2[0].text) # First
print(data2[0].get("href")) # http://example.com/one
print(data2[0]["href"])     # http://example.com/one

print(sp.find_all(['title','h1'])) # [<title>網頁標題</title>, <h1>文件標題</h1>]

print(sp.select('div img')[0]['src']) # http://example.com/three.jpg


