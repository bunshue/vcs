import RPi.GPIO as GPIO

pinBN = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ret = GPIO.wait_for_edge(pinBn, GPIO.FALLING, timeout=5000)
if ret is None:
    print ('5秒內按鈕沒按下')
else:
    print ('按鈕按下，GPIO{}發生中斷訊號'.format(ret))
GPIO.cleanup()
