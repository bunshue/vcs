# F1750 練習 04

def hex_to_dec():
    hexnum = input('輸入十六進位數字: ')
    decnum = 0
 
    for power, digit in enumerate(reversed(hexnum)):
        if digit.isdigit():
            digit_num = int(digit)
        else:
            digit_num = ord(digit.upper()) - ord('A') + 10
        decnum += digit_num * (16 ** power)
 
    print('十進位結果:', decnum)

hex_to_dec()
