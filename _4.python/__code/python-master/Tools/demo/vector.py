class Vec:
    def __init__(self, *v):
        self.v = list(v)

    @classmethod
    def fromlist(cls, v):
        if not isinstance(v, list):
            raise TypeError
        inst = cls()
        inst.v = v
        return inst

    def __repr__(self):
        args = ', '.join(repr(x) for x in self.v)
        return 'Vec({})'.format(args)

    def __len__(self):
        return len(self.v)

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, other):
        # Element-wise addition
        v = [x + y for x, y in zip(self.v, other.v)]
        return Vec.fromlist(v)

    def __sub__(self, other):
        # Element-wise subtraction
        v = [x - y for x, y in zip(self.v, other.v)]
        return Vec.fromlist(v)

    def __mul__(self, scalar):
        # Multiply by scalar
        v = [x * scalar for x in self.v]
        return Vec.fromlist(v)

    __rmul__ = __mul__

a = Vec(1, 2, 3)
b = Vec(3, 2, 1)

c = a + b
print(c)

c = a - b
print(c)

c = 3.0 * a
print(c)

c = a * 3.0
print(c)

'''
    >>> a - b
    Vec(-2, 0, 2)

    and multiplied by a scalar on the left
    >>> 3.0 * a
    Vec(3.0, 6.0, 9.0)

    or on the right
    >>> a * 3.0
    Vec(3.0, 6.0, 9.0)
'''
