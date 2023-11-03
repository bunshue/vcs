import time
import requests

URL = "http://www.majortests.com/word-lists/word-list-0{0}.html"

for i in range(1, 10):
    url = URL.format(i) 
    r = requests.get(url)
    print(r.status_code)
    print("等待5秒鐘...")
    time.sleep(5) 
   
