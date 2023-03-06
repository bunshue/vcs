from esp8266_i2c_lcd import I2cLcd
from machine import I2C,Pin

# GPIO 12-D6,GPIO 13-D7
i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.clear()

lcd.move_to(2, 0)  #(0,2) 位置
lcd.putstr("R=100")
lcd.putchar(chr(0xF4)) #Ω

lcd.move_to(2, 1)  #(1,2) 位置
lcd.putstr("T=25") 
lcd.putchar(chr(0xDF)) #°
lcd.putchar("C") #C