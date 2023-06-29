import os
from linebot import WebhookHandler
from linebot.models import MessageEvent, TextMessage, PostbackEvent
from linebot.exceptions import InvalidSignatureError

import DBtalk, DBdynamo

import datetime

handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])

def lambda_handler(event, context):
    
    print(os.listdir())
    print(os.listdir('/'))
    print(event)
    
    if 'body' in event:
        result = line_handler(event, context)
        return result
    else:
        scheduled_handler()

def line_handler(event, context):
    print('datetime from lambda:', datetime.datetime.today())
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
            reply = False
            reply_method = [DBtalk.google_translate, DBtalk.reply_default]
            while not reply:
                try:
                    reply_method[0](event)
                    reply = True
                    print('reply by:', reply_method[0])
                except:
                    reply_method = reply_method[1:]
                    reply = False
    
    @handler.add(PostbackEvent)
    def handle_postback(event):
        job = event.postback.data
        if job.startswith('save'):
            target = job.split(':')[1]
            result = DBdynamo.save(target)
            DBtalk.reply_save(event, result)
        elif job.startswith('review'):
            items = DBdynamo.review()
            if items:
                DBtalk.reply_review(event, items)
            else:
                DBtalk.default(event)

    try:
        # get X-Line-Signature header value
        copy_headers = {key.lower(): value for key, value in event['headers'].items()}
        signature = copy_headers['x-line-signature']

        # get request body as text
        body = event['body']
        
        # handle webhook body
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        return {'statusCode': 400, 'body': 'InvalidSignature'}
        
    except Exception as e:
        print(e)
        return {'statusCode': 400, 'body': str(e)}

    return {'statusCode': 200, 'body': 'OK'}
    
def scheduled_handler():
    user_id = 'U7b5acbfb05903273a2eaeb566cdb55c2'
    items = DBdynamo.review()
    if items:
        DBtalk.push_review(user_id, items)
    else:
        DBtalk.push_default(user_id)