import RPi.GPIO as GPIO

pinBN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

n = 1
def event_occurred(pin):
    global n
    GPIO.remove_event_detect(pin)
    print('按了{}次'.format(n))
    n += 1
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=event_occurred, bouncetime=300)
#GPIO.add_event_detect(pinBN, GPIO.FALLING, callback=event_occurred)
GPIO.add_event_detect(pinBN, GPIO.FALLING, callback=event_occurred, bouncetime=300)

try:
    # 中斷未發生時想要做的其他事情寫這裡
    # 若沒想要做什麼就讓他睡到天荒地老
    while True:
        time.sleep(1000000)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
