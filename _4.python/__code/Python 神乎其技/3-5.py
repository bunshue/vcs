# 3-5 函式參數解包

def print_vector(x, y, z):
    print('<{}, {}, {}>'.format(x, y, z))


tuple_vec = (1, 0, 1)
dict_vec = {'y':0, 'z':1, 'x':1}

print_vector(*tuple_vec)
print_vector(**dict_vec)