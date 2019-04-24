days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for index in range(len(days)):
   print('index = ', str(index), ', day = ', days[index])

for letter in 'Hello Python':
   print('Current Letter :', letter)


for letter in "Hello Python":
    if letter == 'h':
        pass   #空指令
    else:
        print('Current Letter :', letter)
   

import my_print  #把整個 my_print.py 都引進來
print("測試導入整個模組")
my_print.print_func("Python")



