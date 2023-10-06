# 4-4-3 拷貝任何物件

import copy

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


class Rectangle:
    
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    
    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')


rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
drect = copy.deepcopy(rect)

print('rect =', rect)
print('srect =', srect)
print('drect =', drect)
print('rect == srect', rect == srect)
print('rect is srect', rect is srect)
print('rect == drect', rect == drect)
print('rect is drect', rect is drect)

rect.topleft.x = 999

print('rect =', rect)
print('srect =', srect)
print('drect =', drect)

drect.topleft.x = 222

print('rect =', rect)
print('srect =', srect)
print('drect =', drect)