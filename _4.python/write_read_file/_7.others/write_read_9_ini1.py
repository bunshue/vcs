import sys

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import configparser

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('data/config1.ini')

line_bot_api = config.get('line-bot', 'channel_access_token')
handler = config.get('line-bot', 'channel_secret')

print(line_bot_api)
print(handler)

print("------------------------------------------------------------")  # 60個

import configparser

config = configparser.ConfigParser()
config.read('data/config2.ini')

secret_key = config.get('DEFAULT', 'ServerAliveInterval')
print(secret_key)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
