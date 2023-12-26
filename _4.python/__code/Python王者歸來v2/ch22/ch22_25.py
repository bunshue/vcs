# ch22_25.py
import shelve

phone = shelve.open('phonebook')
phone['Tom'] = ('Tom', '0912-112112', '台北市')
phone['John'] = ('John', '0928-888888', '台中市')
phone.close()















