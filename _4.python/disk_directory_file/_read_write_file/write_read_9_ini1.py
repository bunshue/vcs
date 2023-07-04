filename = 'C:/_git/vcs/_1.data/______test_files1/menu.xml'


import configparser

config = configparser.ConfigParser()
config.read('config.ini')

secret_key = config.get('DEFAULT', 'ServerAliveInterval')

print(secret_key)




import configparser

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = config.get('line-bot', 'channel_access_token')
handler = config.get('line-bot', 'channel_secret')

print(line_bot_api)
print(handler)






