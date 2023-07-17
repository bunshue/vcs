import smbus, time

i2c = smbus.SMBus(1)
addr = 0x53     # 裝置位址

# 設定運作頻率 100HZ
i2c.write_byte_data(addr, 0x2C, 0x0B)
# 設定電源管理為自動休眠
i2c.write_byte_data(addr, 0x2D, 0x08)
# 設定感測範圍 正負8G
i2c.write_byte_data(addr, 0x31, 0x08 | 0x02) 

# 讀資料
def axesData(reg):
    bytes = i2c.read_i2c_block_data(addr, reg, 2)
    axes = bytes[0] | (bytes[1] << 8)
    if(axes & (1 << 16 - 1)):
        axes = axes - (1<<16)

    return round(axes * 0.004, 2)

while True:
    x = axesData(0x32)
    y = axesData(0x34)
    z = axesData(0x36)
    print('x:{}\ty={}\tz={}'.format(x, y, z))
    time.sleep(0.2)
