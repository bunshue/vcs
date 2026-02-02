# ch3_40.py
import requests

proxies = {
  "http": "http://111.231.81.109:3128",         # ip:port
  "https": "https://111.231.81.109:1080",       # ip:port
}

r = requests.get("https://docs.python.org", proxies=proxies)

















