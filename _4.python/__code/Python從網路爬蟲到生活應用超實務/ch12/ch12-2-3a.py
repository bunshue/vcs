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
