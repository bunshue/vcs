# ch3_41.py
import requests

proxies = {
  "http": "http://203.83.182.86:8080",         # ip:port
}

r = requests.get("https://docs.python.org", proxies=proxies)
if r.status_code == 200:
    print('代理IP使用成功')




















