import serial
ser = serial.Serial('COM7')  # open serial port
print(ser.port)
print(ser.baudrate)
print(ser.bytesize)
print(ser.parity)
print(ser.timeout)
ser.close()             # close port