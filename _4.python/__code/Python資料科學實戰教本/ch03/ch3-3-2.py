import requests

r = requests.get("https://fchart.github.io/test.html")
print(r.text)
print(r.encoding)
