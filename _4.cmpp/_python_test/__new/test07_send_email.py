
#讀取遠端純文字檔
from urllib.request import urlopen

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())



