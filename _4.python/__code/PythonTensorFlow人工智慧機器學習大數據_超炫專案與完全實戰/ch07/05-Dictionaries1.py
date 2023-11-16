d = {'cat': 'cute',
     'dog': 'love'}
print(d['cat'])        
print('cat' in d)     
d['fish'] = 'wet'
print(d['fish'])        
print(d.get('monkey', 'N/A'))   
print(d.get('fish', 'N/A')) 
del(d['fish'])        
print(d.get('fish', 'N/A'))  



d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))

