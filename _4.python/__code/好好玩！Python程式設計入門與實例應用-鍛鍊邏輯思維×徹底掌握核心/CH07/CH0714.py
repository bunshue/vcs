# List 含有 Tuple
student = [('Eugene', 1989, 'Taipei'),
            ('Davie', 1993, 'Kaohsiung'),
            ('Michelle', 1999, 'Yilan'),
            ('Peter', 1988, 'Hsinchu'),
            ('Connie', 1997, 'Pingtung')]

#定義sort()方法參數key
na = lambda item: item[0] 
student.sort(key = na)
print('依名字排序：')
for name in student:
    print('{:6s},{}, {:10s}'.format(*name))

#直接在sort()方法帶入lamdba()函式
student.sort(key = lambda item: item[2],
             reverse = True)
print('依出生地遞減排序：')
for name in student:
    print('{:6s},{}, {:10s}'.format(*name))
