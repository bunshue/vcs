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
