from machine import Pin,I2C
i2c = I2C(scl=Pin(13), sda=Pin(12), freq=100000)
print(i2c.scan())

