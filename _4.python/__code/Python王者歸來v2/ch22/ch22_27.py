# ch22_27.py
import shelve

phone = shelve.open('phonebook')
for name in phone:
    print(phone[name])
phone.close()















