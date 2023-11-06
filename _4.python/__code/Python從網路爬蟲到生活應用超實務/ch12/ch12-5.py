from telegram.ext import Updater, CommandHandler
import requests 
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler

api_key = "<API金鑰>"
token = "<API權杖>"

def email_alert(first, second=None, third=None):
    URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
    event_name = "web_scraping"
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    requests.get(url)    

def task():
    url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    span = soup.find('span', class_="current")
    temp = span.text
    summary = span.get("aria-label")
    email_alert(temp, summary)
    
scheduler = BackgroundScheduler() 
scheduler.add_job(task, "interval", minutes=2)

updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="已經啟動Email排程天氣通知")
    scheduler.start()

def shutdown(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="已經停止Email排程天氣通知")
    scheduler.shutdown()
    
def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="已經停止Telegram Bot 管家機器人")
    updater.stop()

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("shutdown", shutdown))
dispatcher.add_handler(CommandHandler("stop", stop))
print("Telegram Bot 管家機器人啟動中...")
updater.start_polling()
updater.idle()