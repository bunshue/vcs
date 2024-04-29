# import pprint

print("------------------------------------------------------------")  # 60個

import json
from pprint import pprint
from urllib.request import urlopen

with urlopen("https://pypi.org/pypi/sampleproject/json") as resp:
    project_info = json.load(resp)["info"]

pprint(project_info)

print("------------------------------------------------------------")  # 60個

from pprint import pprint

config = {
    "lang": "Python",
    "version": [3.6, 3.7, 3.8],
    "date": "2019-10-14",
    "platform": "linux",
    "org": "Python Software Foundation",
    "config_status": 0xC0FFEE,
    "the_answer": 42,
}

pprint(config, indent=4, sort_dicts=False)

print("------------------------------------------------------------")  # 60個


print("print與 pprint的比較")

import sys
from pprint import pprint

print("使用print")
print(sys.path)

print("使用pprint")
pprint(sys.path)


print("------------------------------------------------------------")  # 60個


import requests, pprint

api_url = "https://zh.wikipedia.org/w/api.php"

api_params = {
    "format": "json",
    "action": "query",
    "titles": "柔道",
    "prop": "revisions",
    "rvprop": "content",
}

wiki_data = requests.get(api_url, params=api_params).json()

pprint.pprint(wiki_data)


print("------------------------------------------------------------")  # 60個


import requests, pprint

search_api_url = "https://collectionapi.metmuseum.org/public/collection/v1/search?"
query_parameter = "q=python&hasImages=true"
search_url = search_api_url + query_parameter
print(search_url)
search_response = requests.get(search_url)
pprint.pprint(search_response.json())


print("------------------------------------------------------------")  # 60個


import pprint

r = requests.get("https://tw.yahoo.com/")
pprint.pprint(r.text)
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
