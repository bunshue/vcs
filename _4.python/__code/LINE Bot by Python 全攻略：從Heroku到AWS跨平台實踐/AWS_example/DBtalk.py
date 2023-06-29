import os

from linebot import LineBotApi
from linebot.models import TextSendMessage, FlexSendMessage

import DBhardwork, DBflex, DBdynamo

line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])

def google_translate(event):
    # 確認查詢目標
    target = event.message.text.lower().strip()
    print(target)
    
    # 從 DynamoDB 查詢
    check_result = DBdynamo.check(target)
    
    if check_result:
        target, title, reply_dict = check_result
        contents = DBflex.word_flex_card(target, title, reply_dict, 'memory', event.message.id)
    # 從 Google 查詢
    else:
        target, title, reply_dict = DBhardwork.do_google_translate(target)

        contents = DBflex.word_flex_card(target, title, reply_dict, 'Google', event.message.id)
    print(contents)
    # reply_str = target + '，' + title + ':\n' + str(reply_dict)
    line_bot_api.reply_message(
        event.reply_token, 
        FlexSendMessage(
            alt_text='flex ' + target, 
            contents = contents
        )
    )

def reply_default(event):
    if event.type == 'message':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='在 AWS 的中心大聲呼喊：' + event.message.text))
    elif event.type == 'postback':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='在 AWS 的中心大聲呼喊：Review'))
    
def reply_save(event, result):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=result))
    
def reply_review(event, items):
    contents = DBflex.review_flex_card(items)
    line_bot_api.reply_message(
        event.reply_token, 
        FlexSendMessage(
            alt_text='review', 
            contents=contents
        )
    )

def push_review(user_id, items):
    contents = DBflex.review_flex_card(items)
    line_bot_api.push_message(
        user_id, 
        FlexSendMessage(
            alt_text='review', 
            contents=contents
        )
    )
    
def push_default(user_id):
    line_bot_api.push_message(user_id, TextSendMessage(text='在 AWS 的中心大聲呼喊：Review'))