import RPi.GPIO as GPIO
import spidev

pinCS = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinCS, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 10000000

NOOP		= 0x0
DECODEMODE 	= 0x9
INTENSITY 	= 0xA
SCANLIMIT 	= 0xB
SHUTDOWN 	= 0xC
DISPLAYTEST     = 0xF

love = (
    0b01000010,
    0b11100111,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100,
    0b00011000,
    0b00000000
)

smile = (
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10011001,
    0b01000010,
    0b00111100
)

def init():
    send(DISPLAYTEST, 0)
    send(SCANLIMIT, 7)
    send(INTENSITY, 15)
    send(DECODEMODE, 0)
    send(SHUTDOWN, 1)
    
def send(reg, data, which=[1, 1]):
    GPIO.output(pinCS, 0)

    for p in which:
        if p == 1:
            spi.writebytes([reg, data])
        else:
            spi.writebytes([NOOP, data])

    GPIO.output(pinCS, 1)


def show(graph, which):
    for i in range(8):
        send(i + 1, graph[i], which)

def main():
    import time
    init()
    try:
        while True:
            show(love, [0, 1])
            time.sleep(1)
            show(smile, [1, 0])
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    send(SHUTDOWN, 0)

main()
