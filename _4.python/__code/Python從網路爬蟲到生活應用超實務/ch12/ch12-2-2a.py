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