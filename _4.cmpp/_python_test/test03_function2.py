# 自定義函數



def area(radius):
	result = radius * radius * 3.14
	return result


def washingMachine():
	print('注水')
	print('輕柔清洗')
	print('洗淨洗劑')
	print('脫水')
	print('烘乾')

washingMachine()

def washingMachine(mode):
	print('注水')
	if (mode == 'soft'):
		print('輕柔清洗')
	elif (mode == 'hard'):
		print('強力清洗')
	else:
		print('一般清洗')


mode = 'soft'
if (mode == 'soft'):
	print('輕柔清洗')
elif (mode == 'hard'):
	print('強力清洗')
else:
	print('一般清洗')





