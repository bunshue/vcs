# ch7_31.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
active = True
while active:                   # 迴圈進行直到active是False
    input_msg = input(msg)
    if input_msg != 'q':        # 如果輸入不是q才輸出訊息         
        print(input_msg)
    else:
        active = False          # 輸入是q所以將active設為False



