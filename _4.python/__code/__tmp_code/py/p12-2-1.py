import json
import requests
api_url = "https://www.dcard.tw/_api/forums/funny/posts?limit=100"
res = requests.get(api_url).text

data = json.loads(res)
for post in data:
    print(post["title"])

print(res)

