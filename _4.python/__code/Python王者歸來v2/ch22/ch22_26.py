# ch22_26.py
import shelve

phone = shelve.open('phonebook')
print(phone['Tom'])
print(phone['John'])
phone.close()















