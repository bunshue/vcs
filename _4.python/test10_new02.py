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

import os
user = os.getlogin()
print(user)

version = __version__ = "4.61.0.166 Unreleased"
print(version)

font_file = os.path.join(os.path.dirname(__file__), "OpenFlame.ttf")
print(font_file)

print(__doc__)
print(globals())

import sys

major, minor, micro, level, serial = sys.version_info

print('version_info')
print(sys.version_info)
print(major)
print(minor)
print(micro)
print(level)
print(serial)

level = 123
levelnum = 170
print(" * PY_RELEASE_LEVEL = %r = %s" % (level, hex(levelnum)))


