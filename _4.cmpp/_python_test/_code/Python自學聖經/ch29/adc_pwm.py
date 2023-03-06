from machine import Pin,ADC,PWM
import time

led = PWM(Pin(2), freq=1000) #DPIO2對應到D4
a0 = ADC(0) 

while True:
  value = a0.read() #讀取A0埠
  print(value)      #顯示轉換後的數值
  led.duty(value)   #亮度
  time.sleep(0.1) 