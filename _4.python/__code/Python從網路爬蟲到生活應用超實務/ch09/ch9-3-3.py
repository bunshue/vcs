import telegram
 
token = "<API權杖>"
chat_id = "<聊天室識別碼>"

def telegram_bot_sendText(msg):
    bot = telegram.Bot(token=token)
    return bot.sendMessage(chat_id=chat_id, text=msg)
    
test = telegram_bot_sendText("測試Telegram模組!")
print(test)
