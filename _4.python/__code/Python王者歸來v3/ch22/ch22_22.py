# ch22_22.py
import shelve

with shelve.open('phonebook') as phone:
    print(phone['Tom'])
    print(phone['John'])
















