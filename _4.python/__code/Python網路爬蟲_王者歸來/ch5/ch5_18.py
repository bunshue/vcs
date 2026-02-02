# ch5_18.py
import requests
import bs4

# 使用自己的IP
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'http://ip.filefab.com/index.php'
htmlFile = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
ip = soup.find('h1', id='ipd')
print(ip.text.strip())




















