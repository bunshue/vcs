
import requests
from bs4 import BeautifulSoup

# 獲取網頁內容
game_ranking_html = requests.get('https://acg.gamer.com.tw/billboard.php?t=2&p=iOS')

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(game_ranking_html.text, "html.parser")

# 找到所有遊戲排名標題的標籤
games = soup.find_all('div', {'class': 'APP-LI-NAME'})

# 顯示遊戲排名標題
for i, game in enumerate(games, 1):
    print(f"{i}. {game.text.strip()}")
