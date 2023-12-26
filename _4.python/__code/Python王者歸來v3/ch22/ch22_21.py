# ch22_21.py
import shelve

with shelve.open('phonebook') as phone:
    phone['Tom'] = ('Tom', '0912-112112', '台北市')
    phone['John'] = ('John', '0928-888888', '台中市')
















