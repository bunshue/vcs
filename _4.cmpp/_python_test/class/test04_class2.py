print("Class測試")


class animalBaseClass:
	animallegs = 4
	def walk(self):
		print('走動')
	def cry(self):
		print('吼叫')
	def getLegsNum(self):
		print(self.animallegs)

class dogClass(animalBaseClass):
	def __init__(self):
		print('我是小狗')

wanko = dogClass()
wanko.walk()
wanko.cry()
wanko.getLegsNum()


class animalBaseClass:
	animallegs = 2
	def walk(self):
		print('走動')
	def cry(self):
		print('吼叫')

class birdClass(animalBaseClass):
	def __init__(self):
		print('我是小鳥')
	def cry(self):
		print('啾啾')

piyo_suke = birdClass()
piyo_suke.walk()
piyo_suke.cry()

class animalBaseClass:
	def __init__(self, num):
		self.animallegs = num
	def walk(self):
		print('走動')
	def cry(self):
		print('吼叫')
	def getLegsNum(self):
		print(self.animallegs)

class snakeClass(animalBaseClass):
	def __init__(self, num):
		parent_class = super(snakeClass, self)
		parent_class.__init__(num)
		print('我是蛇')

nyoro = snakeClass(0)
nyoro.getLegsNum()

class snakeClass(animalBaseClass):
	def __init__(self):
		snake_leg = 0 
		parent_class = super(snakeClass, self)
		parent_class.__init__( snake_leg)
		print('我是蛇')

nyoro = snakeClass()
nyoro.getLegsNum()

