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