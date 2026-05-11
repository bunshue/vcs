import xtools  

xtools.connect_wifi_led()

token = "<存取權杖>"
message = "使用MicroPython送出Notify通知訊息"
xtools.line_msg(token, message)

