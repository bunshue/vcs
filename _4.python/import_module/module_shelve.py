"""


"""


import shelve

book = shelve.open("addresses")

book['167'] = ('邱大熊', '0912-345678', '台北市忠孝路1號')
book['928'] = ('陳小天', '0987-654321', '新竹市中山路2號')
book.close()

print('------------------------------------------------------------')	#60個

import shelve
book = shelve.open("addresses")

print(book['167'] )
book.close()

print('------------------------------------------------------------')	#60個

import shelve

with shelve.open('phonebook') as phone:
    phone['Tom'] = ('Tom', '0912-112112', '台北市')
    phone['John'] = ('John', '0928-888888', '台中市')

print("------------------------------------------------------------")  # 60個

import shelve

with shelve.open('phonebook') as phone:
    print(phone['Tom'])
    print(phone['John'])

print("------------------------------------------------------------")  # 60個

import shelve
with shelve.open('phonebook') as phone:
    for name in phone:
        print(phone[name])

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



