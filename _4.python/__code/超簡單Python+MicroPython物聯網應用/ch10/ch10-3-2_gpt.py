from machine import Pin, ADC
import utime
import umail
import xtools

xtools.connect_wifi_led()
button = Pin(4, Pin.IN, Pin.PULL_UP)
adc = ADC(0)

# 建立電子郵件內容
sender_email = "hueyan@gmai.com"
sender_name = "Witty Cloud機智雲"
sender_app_password = "owith---------cec"
recipient_email = "hueyan@ms2.hinet.net"
email_subject = "請注意！目前環境亮度"

print("請按下按鍵開關來送出Email…")
while True:
    if button.value() == 0:   # 值 0 是按下
        print("送出Email!")
        smtp = umail.SMTP("smtp.gmail.com", 587, ssl=False)
        smtp.login(sender_email, sender_app_password)
        smtp.to(recipient_email)
        smtp.write("From:" + sender_name + " <" + sender_email + ">\n")
        smtp.write("Subject:" + email_subject + "\n")
        smtp.write("目前ESP8266的光敏電阻值: " + str(adc.read()) + "\n")
        smtp.send()
        smtp.quit()
        utime.sleep(10)
