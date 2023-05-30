
print('字元轉unicode')
string = '你'

print(ord(string))

print(hex(ord(string)))


number1 = 3
number2 = 5

try:
    result = number1 / number2
    print("Result is " + str(result))
except ZeroDivisionError:
    print("Division by zero!")
except SyntaxError:
    print("A comma may be missing in the input")
except:
    print("Something wrong in the input")
else:
    print("No exceptions")
finally:
    print("The finally clause is executed")



print('十進位 轉 十六進位')

# Convert a decimal to a hex as a string 
def decimalToHex(decimalValue):
    hex = ""
 
    while decimalValue != 0:
        hexValue = decimalValue % 16 
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    
    return hex
  
# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

decimalValue = 170
hexValue = decimalToHex(decimalValue)
print('decimal : %d\thex : %s' % (decimalValue, hexValue) )

decimalValue = 65535
hexValue = decimalToHex(decimalValue)
print('decimal : %d\thex : %s' % (decimalValue, hexValue) )

  



