import sys

print("------------------------------------------------------------")  # 60個

from apscheduler.schedulers.blocking import BlockingScheduler
import time, datetime 


def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務1...", text)

scheduler = BlockingScheduler() 


run_date = datetime.date(2020,9,4)
scheduler.add_job(task, "date", run_date=run_date, args=["工作1"])
run_date = datetime.datetime(2020,9,4,14,10,0)
scheduler.add_job(task, "date", run_date=run_date, args=["工作2"])
run_date = "2020-9-4 14:15:00"
scheduler.add_job(task, "date", run_date=run_date, args=["工作3"])

""" NG
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 
"""

print("------------------------------------------------------------")  # 60個

from apscheduler.schedulers.blocking import BlockingScheduler
import time 

def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務2...", text)
scheduler = BlockingScheduler() 
scheduler.add_job(task, "interval", minutes=1, args=["工作1"])
start_date = '2020-09-04 14:25:00'
end_date = '2020-09-04 14:28:00'
scheduler.add_job(task, "interval", minutes=1, seconds = 30, 
    start_date=start_date, end_date=end_date, args=["工作2"])
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 

print("------------------------------------------------------------")  # 60個

from telegram import Bot

bot = Bot("<API�v��>")
print(bot.getMe())

print("------------------------------------------------------------")  # 60個

from telegram import Bot

bot = Bot("<API�v��>")
updates = bot.getUpdates() 
print(updates[0].update_id)
print(updates[0].message)


print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    from_user = update.message.from_user
    name = from_user.last_name + from_user.first_name
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="你好! {}".format(name))

def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="已經停止Telegram Bot 歡迎機器人")
    updater.stop()

dispatcher.add_handler(CommandHandler("hello", hello))
dispatcher.add_handler(CommandHandler("stop", stop))
print("Telegram Bot 歡迎機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=update.message.text)

def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="已經停止Telegram Bot 鸚鵡機器人")
    updater.stop()

dispatcher.add_handler(CommandHandler("stop", stop))
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
print("Telegram Bot 鸚鵡機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    buttons = [
        [InlineKeyboardButton("IFTTT", callback_data="1"),
         InlineKeyboardButton("LINE Notify", callback_data="2")],
        [InlineKeyboardButton("Telegram Bot", callback_data="3")]
        ]
    markup = InlineKeyboardMarkup(buttons)             
    update.message.reply_text("請選擇: ", reply_markup=markup)

def answer(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text("你的選擇是: " + query.data)

def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="已經停止Telegram Bot 選單機器人")
    updater.stop()
    
dispatcher.add_handler(CommandHandler("stop", stop))
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(answer))
print("Telegram Bot 選單機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from random import randint

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

def math_add(update, context):
    a, b = randint(1, 100), randint(1, 100)
    buttons = []
    for s in range(a+b-randint(1,3),a+b+randint(1,3)):
        data = "{} {} {}".format(a,b,s)
        buttons.append(InlineKeyboardButton(str(s), callback_data=data))
    
    text = "{} + {} = ?".format(a, b)    
    markup = InlineKeyboardMarkup([buttons])             
    update.message.reply_text(text, reply_markup=markup)

def check_answer(update, context):
    a, b, s = [int(x) for x in update.callback_query.data.split()]
    if a + b == s:
        update.callback_query.edit_message_text("答對了!")
    else:
        update.callback_query.edit_message_text("答錯囉!")

def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="已經停止Telegram Bot 加法測驗機器人")
    updater.stop()
    
dispatcher.add_handler(CommandHandler("stop", stop))
dispatcher.add_handler(CommandHandler("add", math_add))
dispatcher.add_handler(CallbackQueryHandler(check_answer))
print("Telegram Bot 加法測驗機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

import requests 
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

api_key = "<API金鑰>"

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
    
scheduler = BlockingScheduler() 
scheduler.add_job(task, "interval", minutes=2)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 

print("------------------------------------------------------------")  # 60個

from image_downloader.image_downloader import download_csv_file_images
from apscheduler.schedulers.blocking import BlockingScheduler

csvfile = "tmp_ptt_beauty.csv"

def task(file):
    download_csv_file_images(file)

scheduler = BlockingScheduler() 
run_date = "2020-9-6 14:40:00"
scheduler.add_job(task, "date", run_date=run_date, args=[csvfile])
print("自動排程在", run_date, "下載 ", csvfile, " 的圖檔...")
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

from apscheduler.schedulers.blocking import BlockingScheduler
import time 

def task():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務3...")
scheduler = BlockingScheduler() 
scheduler.add_job(task, "interval", seconds=3)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 

print("------------------------------------------------------------")  # 60個

