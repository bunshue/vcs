from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

print("正在掃瞄 I2C 裝置...")
devices = i2c.scan()
if len(devices) == 0:
    print("沒有找到 I2C 裝置!")
else:
    print("找到 " + str(len(devices)) + " 個 I2C 裝置.")
    for device in devices:
        print("I2C 裝置的位址: ", hex(device))
        