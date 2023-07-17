import time, RF24

radio = RF24.RF24(22, 0) #(CE, CSN)
r_pipe_1 = b'1node'
r_pipe_2 = b'2node'
w_pipe   = b'ardu' # 命名未完成

radio.begin()
radio.setRetries(15, 15)
radio.openReadingPipe(1, r_pipe_1)
radio.openReadingPipe(2, r_pipe_2)

radio.printDetails()
print("NRF24L01+ is ready.")

radio.startListening()
while True:
    t = radio.available_pipe()   # 調整
    if (t[0]):                   # 調整
        len = radio.getDynamicPayloadSize()
        data = radio.read(len)
        print('{}: [{}]'.format(t[1], data.decode('utf-8'))) # 調整
        
        radio.stopListening()
        # 組合出完整的 writing pipe 名稱
        pipe_num = str(t[1]).encode('utf-8') + w_pipe
        radio.openWritingPipe(pipe_num + w_pipe)   
        radio.write(b"echo: " + data)
        radio.startListening()

    time.sleep(0.1)
