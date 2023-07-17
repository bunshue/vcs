from machine import Pin,ADC
import time

led = Pin(2, Pin.OUT) #DPIO2對應到D4
a0 = ADC(0) 

while True:
  value = a0.read() #讀取A0埠
  print(value)      #顯示轉換後的數值
  if value<600:
      led.value(0)  #開燈
  else:
      led.value(1)  #關燈
  time.sleep(0.1) 