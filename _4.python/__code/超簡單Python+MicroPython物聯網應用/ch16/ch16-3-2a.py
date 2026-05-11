from machine import Pin, SoftI2C
import ssd1306

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.fill(0)  # 清除內容
oled.text("Raspberry Pi Pico W", 0, 0)
oled.text("MicroPython", 0, 10)
oled.text("Hello, World!", 0, 20)
oled.show()
