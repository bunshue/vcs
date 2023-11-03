# ch7_32.py
msg1 = '人機對話專欄,請告訴我妳喜歡吃的水果!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
while True:                     # 這是while無限迴圈
    input_msg = input(msg)
    if input_msg == 'q':        # 輸入q可用break跳出迴圈          
        break
    else:
        print("我也喜歡吃 %s " % input_msg.title( ))
