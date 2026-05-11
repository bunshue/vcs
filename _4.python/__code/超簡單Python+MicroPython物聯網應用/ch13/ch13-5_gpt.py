from machine import ADC, Timer

# 初始化ADC
adc = ADC(0)

# 定義回調函數
def read_adc(timer):
    adc_value = adc.read()
    print(adc_value)

# 初始化並配置Timer
timer = Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=read_adc)

