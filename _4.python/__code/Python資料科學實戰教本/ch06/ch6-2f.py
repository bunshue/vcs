from urllib.parse import urljoin

URL = "http://www.majortests.com/word-lists/word-list-01.html"
PTT = "https://wwww.ptt.cc/bbs/movie/index.html"

catalog = ["movie", "NBA", "Gossiping"]

for i in range(1, 5):
    url = urljoin(URL, "world-list-0{0}.html".format(i)) 
    print(url)
print("-----------------")
for item in catalog:
    url = urljoin(PTT, "../{0}/index.html".format(item))
    print(url)
 