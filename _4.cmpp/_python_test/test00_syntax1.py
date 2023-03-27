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

print('設定變數')
ROWS, COLUMNS = 19, 4
print(ROWS)
print(COLUMNS)

#設定一個二維矩陣
money=[[41.36, 28.96, 3.77, 8.45],
[29.08, 3.58, 6.81, 0.77],
[15.68, 12.76, 3.79, 3.29],
[15.61, 10.93, 3.28, 2.95],
[11.27, 8.89, 10.22, 1.00],
[23.20, 2.26, 4.22, 0.58],
[11.28, 9.14, 6.50, 2.88],
[13.96, 9.18, 2.93, 2.84],
[14.44, 6.94, 4.70, 2.24],
[26.93, 0.63, 0.28, 0.47],
[9.05, 10.95, 1.93, 2.74],
[9.71, 7.47, 4.13, 1.90],
[9.00, 6.18, 7.20, 0.71],
[8.92, 8.03, 3.60, 2.15],
[15.00, 4.89, 0.24, 1.69],
[9.01, 8.49, 2.53, 1.77],
[7.02, 9.09, 0.98, 3.96],
[9.43, 0.40, 0.41, 10.57],
[12.78, 3.75, 3.54, 0.55]]

#設定一個一維矩陣
games= ["Wii Sports", "Super Mario Bros", "Mario Kart Wii", "Wii Sports Resort",
        "Pokemon Red/Pokemon Blue", "Tetris", "New Super Mario Bros", "Wii Play", 
        "New Super Mario Bros Wii", "Duck Hunt", "Nintendogs", "Mario Kart DS",
        "Pokemon Gold/Pokemon Silver", "Wii Fit", "Kinect Adventures!", "Wii Fit Plus",
        "Gramd Theft Auto V", "Grand Theft Auto: San Andreas","Super Mario World" ]




