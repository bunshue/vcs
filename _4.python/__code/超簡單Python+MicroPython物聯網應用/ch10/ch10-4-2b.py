from linenotify import LineNotify  
import xtools

xtools.connect_wifi_led()

token = "<存取權杖>"

line = LineNotify(token)
# 寄送LINE訊息與貼圖
# https://developers.line.biz/en/docs/messaging-api/sticker-list/#sticker-definitions
line.notifySticker(8522, 16581266, "OK! 你好!")
