import requests

r = requests.get("https://fchart.github.io/json/Example.json")
print(r.text)
print(type(r.text))
print("----------------------")
print(r.json())
print(type(r.json()))


