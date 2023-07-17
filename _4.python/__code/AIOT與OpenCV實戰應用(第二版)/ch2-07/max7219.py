import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 10000000

NOOP		= 0x0
DECODEMODE 	= 0x9
INTENSITY 	= 0xA
SCANLIMIT 	= 0xB
SHUTDOWN 	= 0xC
DISPLAYTEST = 0xF

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

def init():
    send(DISPLAYTEST, 0)
    send(SCANLIMIT, 7)
    send(INTENSITY, 8)
    send(DECODEMODE, 0)
    send(SHUTDOWN, 1)
    
def send(reg, data):
    spi.writebytes([reg, data])

def show(graph):
    for i in range(8):
        send(i + 1, graph[i])

def main():
    init()
    show(love)
    input('enter to stop')
    send(SHUTDOWN, 0)

main()