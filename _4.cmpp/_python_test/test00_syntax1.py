# 各種python專用的語法

print("各種python專用的語法")

print(__name__)

if __name__ == '__main__':
    print('happy new year !!')

menu = {'拉麵':500, '炒飯':430, '煎餃':210}
for order in menu:
	print(order)
	print(menu[order] * 1.08)


music_list = ['DEATH METAL', 'ROCK', 'ANIME', 'POP']
for music in music_list:
	print('now playing... ' + music)

family = ['ryo-ko', 'mako', 'satsuki']
for kid in family:
	print('早安！' + kid)
	print('起床')
	print('吃早餐')
	continue
	print('出門上學')

#使用dir()內置函數返回一個包含一個模塊中定義名稱的字符串的排序列表。
#該列表包含在一個模塊中定義的所有模塊，變量和函數的名稱。

#查看 math
import math
content = dir(math)
print("math 模組所支援的指令 : " + str(content))

#查看 serial
import serial
content = dir(serial)
print("serial 模組所支援的指令 : " + str(content))


