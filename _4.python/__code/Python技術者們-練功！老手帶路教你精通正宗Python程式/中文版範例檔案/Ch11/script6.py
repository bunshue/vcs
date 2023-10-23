#! /usr/bin/env python3 

#數字與英文的對應字典
_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three',  
             '4': 'four','5': 'five', '6': 'six', '7': 'seven',     
             '8': 'eight','9': 'nine'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve',
               '3': 'thirteen', '4': 'fourteen', '5': 'fifteen',
               '6': 'sixteen', '7': 'seventeen', '8': 'eighteen',
               '9': 'nineteen'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', 
               '5': 'fifty','6': 'sixty', '7': 'seventy',  
               '8': 'eighty', '9': 'ninety'}

def num2words(num_string): 
    if num_string == '0': 
        return'zero'
    if len(num_string) > 2:  
        return "抱歉此程式只能處理0~99的2位整數"
    num_string = '0' + num_string 
 
    tens, ones = num_string[-2], num_string[-1] 

    if tens == '0':    
        return _1to9dict[ones]
    elif tens == '1':  
        return _10to19dict[ones]
    else:              
        return _20to90dict[tens] + ' ' + _1to9dict[ones]

#定義主控函式
def main():                        
    print(num2words(sys.argv[1]))

main() 
