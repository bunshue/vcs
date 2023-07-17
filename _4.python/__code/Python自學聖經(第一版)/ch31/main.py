from esp8266_i2c_lcd import I2cLcd
from machine import I2C,Pin,ADC
from time import sleep

# GPIO 12-D6,GPIO 13-D7
DEFAULT_I2C_ADDR = 0x27 # 位址
A0 = ADC(0) # 讀取 A0 埠

i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.clear()

while True:
  A0_value = A0.read() #讀取A0埠
  print(A0_value)      #顯示轉換後的數值  

  lcd.move_to(0, 0)    #(0,0) 位置
  lcd.putstr("A0=" + str(A0_value)  + "   ") 
  sleep(0.5)