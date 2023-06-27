print('list使用範例')

print('一維list a')
mylist = ["A", "B", "C", "D", "E"]

for elem in mylist:
    print(elem)

print('一維list b')
my_list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
print('一一取出list內的值')
for v in my_list:
    print(str(v) + " ", end = "")
print()

print('直接印出list')
print(my_list)

print('一維list c')
myList = [1, 2, 3, 4, 5, 6]
for i in range(4, -1, -1):
    myList[i + 1] = myList[i]

for i in range(0, 6): 
    print(myList[i], end = " ")


'''
#list排序

import SelectionSort 

lst = [3, 4, 1, 2, 0]
SelectionSort.selectionSort(lst)
print(lst)
'''

print('二維list')

data = list()

data.append((1, 'Banana', 777))
data.append((2, 'Eagle', 111))
data.append((3, 'Giraffe', 222))
data.append((5, 'Apple', 333))
data.append((6, 'India', 555))
data.append((7, 'Happy', 999))
data.append((8, 'Frog', 666))
data.append((9, 'Dog', 888))
             
print(data)


print('二維list排序')
students = [
    ("John", "Smith", 96),
    ("Susan", "King", 76),
    ("Kim", "Yao", 99)
]
students.sort(key=lambda e: (e[1]))
print(students)
print(sorted(students, key = lambda t: (t[2]), reverse = True))

print('三維list')
dates = [
    [
        [ 1,  3,  5,  7],
        [ 9, 11, 13, 15],
        [17, 19, 21, 23],
        [25, 27, 29, 31]
    ],
    [
        [ 2,  3,  6,  7],
        [10, 11, 14, 15],
        [18, 19, 22, 23],
        [26, 27, 30, 31]
    ],
    [
        [ 4,  5,  6,  7],
        [12, 13, 14, 15],
        [20, 21, 22, 23],
        [28, 29, 30, 31]
    ],
    [
        [ 8,  9, 10, 11],
        [12, 13, 14, 15],
        [24, 25, 26, 27],
        [28, 29, 30, 31]
    ],
    [
        [16, 17, 18, 19],
        [20, 21, 22, 23],
        [24, 25, 26, 27],
        [28, 29, 30, 31]
    ]
]

print('印出三維list')
for i in range(5):
    for j in range(4):
         for k in range(4):
             print(format(dates[i][j][k], '4d'), end = " ")
         print()


