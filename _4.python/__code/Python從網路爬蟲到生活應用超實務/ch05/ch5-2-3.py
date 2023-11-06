import requests
import re

url = "https://fchart.github.io/"
response = requests.get(url)
links = re.findall(r'href="https://.*?"', response.text)
for link in links:
    print(link)

