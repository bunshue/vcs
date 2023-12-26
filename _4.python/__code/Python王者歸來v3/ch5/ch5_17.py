# ch5_17.py
v = eval(input("請輸入火箭速度 : "))
if (v < 7.9):
    print("人造衛星無法進入太空")
elif (v == 7.9):
    print("人造衛星可以環繞地球作圓形移動")
elif (v > 7.9 and v < 11.2):
    print("人造衛星可以環繞地球作橢圓形移動")
elif (v >= 11.2 and v < 16.7):
    print("人造衛星可以環繞太陽移動")
else:
    print("人造衛星可以脫離太陽系")
    
