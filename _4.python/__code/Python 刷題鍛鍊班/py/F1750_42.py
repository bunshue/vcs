# F1750 練習 42

class StrDict(dict):
    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)
    
    def __getitem__(self, key):
        if not str(key) in self:
            self[key] = None
        return dict.__getitem__(self, str(key))

sd = StrDict()
sd[1] = 1
sd[3.14] = 3.14
sd['10'] = 'test'

print(sd[1])
print(sd['3.14'])
print(sd[10])
print(sd['a'])
print(sd)
