import json
import requests

url = "https://fchart.github.io/json/GoogleBooks.json"
jsonfile = "Books.json"
r = requests.get(url)
r.encoding = "utf8"
json_data = json.loads(r.text)
with open(jsonfile, 'w') as fp:
    json.dump(json_data, fp)    


