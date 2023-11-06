from telegram import Bot

bot = Bot("<APIÅv§ú>")
updates = bot.getUpdates() 
print(updates[0].update_id)
print(updates[0].message)

