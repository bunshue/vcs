# ch22_23.py
import shelve

with shelve.open('phonebook') as phone:
    for name in phone:
        print(phone[name])
















