'''
# 其他

'''


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
if __name__ == '__main__':    
    a = shape(100, 200)
    b = shape(200, 300)
    print(a.info())
    print(b.info())
    

print('------------------------------------------------------------')	#60個


class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
    
class circle(shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def info(self):
        return ("圓形", self.x, self.y, self.r)
    
class rectangle(shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    
    def info(self):
        return ("矩形", self.x, self.y, self.w, self.h)

if __name__ == '__main__':
    a = shape(100, 200)
    b = shape(200, 300)
    c = circle(100, 200, 50)
    d = rectangle(100, 200, 50, 50)
    shapes = [a, b, c, d]
    for s in shapes:
        print(s.info())
        
print('------------------------------------------------------------')	#60個

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def info(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
class circle(shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def info(self):
        return ("圓形", self.x, self.y, self.r)
    
class rectangle(shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    
    def info(self):
        return ("矩形", self.x, self.y, self.w, self.h)

if __name__ == '__main__':
    d = rectangle(100, 200, 50, 50)
    print(d.info())
    print("往x前進50點，y後退20點")
    d.move(50, -20)
    print(d.info())
    


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import random
class poker():
    def __init__(self):
        self.deck = [i for i in range(52)]
        random.shuffle(self.deck)
        self.card_type = ['黑桃', '紅心', '梅花', '方塊']
        self.index = 0
    
    def decode(self, card):
        suit = self.card_type[card // 13]
        no = card % 13 + 1
        if no == 1:
            no = 'A'
        elif no > 10:
            no = chr((no - 11) + ord('J'))
        return (suit, str(no))
        
    def showAll(self):
        for card in self.deck:
            print(self.decode(card), end='')
        print()
    
    def dealFive(self):
        for i in range(5):
            print(self.decode(self.deck[self.index]), end='')
            self.index += 1
        print()
    
    def oneMore(self):
        print(self.decode(self.deck[self.index]), end='')
        self.index += 1
        print()
    
    def shuffle(self):
        random.shuffle(self.deck)
        self.index = 0

if __name__ == '__main__':
    p = poker()
    p.showAll()
    print("------")
    p.dealFive()
    for i in range(3):
        p.oneMore()
    print("------")
    p.shuffle()
    p.showAll()
    print("------")
    p.dealFive()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


