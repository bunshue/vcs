from machine import Pin, ADC
import utime
import umail
import xtools

xtools.connect_wifi_led()
button = Pin(14, Pin.IN, Pin.PULL_UP)
adc = ADC(Pin(27))
# 建立電子郵件內容
sender_email = "<寄件者的Gmail電郵地址>"
sender_name = "ESP8266-Micropython"
sender_app_password = "<應用程式密碼>"
recipient_email = "<收件者的電郵地址>"
email_subject = "警告: Witty Cloud開發板的光敏電阻值"

print("請按下按鍵開關來送出Email…")
while True:
    if button.value() == 0:   # 值 0 是按下
        print("送出Email!")
        smtp = umail.SMTP("smtp.gmail.com", 587, ssl=False)
        smtp.login(sender_email, sender_app_password)
        smtp.to(recipient_email)
        smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
        smtp.write("Subject:" + email_subject + "\n")
        smtp.write("目前ESP8266的光敏電阻值:" + str(adc.read_u16()))
        smtp.send()
        smtp.quit()
        utime.sleep(10)
        
        
