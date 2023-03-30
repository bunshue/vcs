html = """
<html><head><title>網頁標題</title></head>
<p class="header"><h2>文件標題</h2></p>
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
sp = BeautifulSoup(html,'html.parser') 

print(sp.title) # <title>網頁標題</title>

print(sp.find('h2')) # <h2>文件標題</h2>

print(sp.find_all('a')) 
print(sp.find_all("a", {"class":"red"}))

data1=sp.find("a", {"href":"http://example.com/one"})
print(data1.text) # First

data2 = sp.select("#link1") 
print(data2[0].text) # First
print(data2[0].get("href")) # http://example.com/one
print(data2[0]["href"])     # http://example.com/one

print(sp.find_all(['title','h2'])) # [<title>網頁標題</title>, <h2>文件標題</h2>]

print(sp.select('div img')[0]['src']) # http://example.com/three.jpg


