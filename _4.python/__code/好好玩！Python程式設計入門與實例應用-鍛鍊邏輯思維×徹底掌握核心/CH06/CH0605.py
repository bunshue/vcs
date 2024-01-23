#Packing和Unpacking的用法(2)

name = 'Tom', 'Mary'    # Tuple
t, m = name             # Unpacking
print(f'置換前:{t}, {m}')
t, m = m, t             # Swap
print(f'置換後:{t}, {m}')
