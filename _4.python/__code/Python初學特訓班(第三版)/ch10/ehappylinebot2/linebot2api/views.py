from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '專業寫作團隊':
                        picurl = 'https://imgur.com/OQyWDus.jpg'
                        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=picurl, preview_image_url=picurl))
                    if mtext == '以電話與我們聯絡':
                        buttonsMessage = TemplateSendMessage(
                            alt_text='Contact us',
                            template=ButtonsTemplate(
                                title='聯絡我們',
                                text='0972367377',
                                actions=[
                                    URIAction(label='撥打電話', uri='tel:0972367377')
                                ]
                            )
                        )
                        line_bot_api.reply_message(event.reply_token, messages=[buttonsMessage])

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

