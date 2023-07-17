import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
# 找到威力彩的區塊
datas = sp.find('div', class_='contents_box02')
# 開獎期數
title = datas.find('span', 'font_black15').text
print('威力彩期數：', title)
# 開獎號碼
nums = datas.find_all('div', class_='ball_tx ball_green')
# 開出順序
print('開出順序：', end=' ')
for i in range(0,6):
    print(nums[i].text, end=' ')
# 大小順序
print('\n大小順序：', end=' ')
for i in range(6,12):
    print(nums[i].text, end=' ')
# 第二區
num = datas.find('div', class_='ball_red').text
print('\n第二區：', num)