from bs4 import BeautifulSoup
import requests
import random

if __name__ == '__main__':
    # 代理伺服器查詢: http://cn-proxy.com/
    proxy_ips = ['39.137.69.8:8080', '222.88.147.121:8060']
    ip = random.choice(proxy_ips)
    print('Use', ip)
    resp = requests.get('http://ip.filefab.com/index.php',
                        proxies={'http': 'http://' + ip})
    soup = BeautifulSoup(resp.text, 'html5lib')
    print(soup.find('h1', id='ipd').text.strip())