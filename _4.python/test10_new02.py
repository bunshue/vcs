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




import os

target = 'https://tw.appledaily.com/new/realtime/{}'

for page in range(1, 11):
    url = target.format(page)
    print(url)

'''
filename = 'C:/_git/vcs/_1.data/______test_files2/news_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';
with open(filename, "w", encoding = 'utf-8') as fp:
    print(filename + " is dumping...")
    json.dump(titles, fp)
'''

base_dir = os.path.dirname(os.path.abspath(__file__))

print(base_dir)



query_string = 'abcdefghijklmn'
query_number = 12345678901234
replace_parameter = "無f替換變數"
replace_parameter += " WHERE {query_string}"
replace_parameter += " ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)


replace_parameter = "有f替換變數"
replace_parameter += f" WHERE {query_string}"
replace_parameter += f" ORDER BY record_no DESC LIMIT {query_number}"
print(replace_parameter)


table_columns = '(alpaca_name, training, duration, date)'
postgres_insert_query = f"""INSERT INTO alpaca_training {table_columns} VALUES (%s,%s,%s,%s)"""

print(postgres_insert_query)


print('全圖640X480, 每160X160裁一塊出來')
W = 640
H = 480
w = 160
h = 160

'''
for(y = 0; y < H; y += h)
  for(x = 0; x < W; x += w)
'''
for y in range(0, H, h):
    for x in range(0, W, w):
        box = x, y, min(W, x + w), min(H, y + h)
        print(box)
        #tile = ImageTk.PhotoImage(image.crop(box))
        #canvas.create_image(x, y, image = tile, anchor = NW)
        #print(x, y)
        #print(box)




import time

print(time.localtime()) #獲取格式化的時間

localtime = time.asctime(time.localtime())
print (localtime)

#格式化日期成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))



