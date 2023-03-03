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

adict = {'book':10, 'pen':3, 'earser':6, 'ruler':2}
for key, value in adict.items():
    if value < 5:
      print("({},{})".format(key, value))




#字典(dictionary)的資料型態
mydict = {'a':3, 'b':2, 'c':5}
print(mydict['a'])
mydict['d'] = 7
print(mydict)




