import time, RF24

radio = RF24.RF24(22, 0) #(CE, CSN)
r_pipe = b'11111'
w_pipe = b'22222'   # 增加

radio.begin()
radio.setRetries(15, 15)
radio.openReadingPipe(1, r_pipe)
radio.openWritingPipe(w_pipe) # 增加

radio.printDetails()
print("NRF24L01+ is ready.")

radio.startListening()
while True:
    if radio.available():
        len = radio.getDynamicPayloadSize()
        data = radio.read(len)
        print('[{}]'.format(data.decode('utf-8')))

        radio.stopListening()         # 增加
        radio.write(b"echo: " + data) # 增加
        radio.startListening()        # 增加

    time.sleep(0.1)
