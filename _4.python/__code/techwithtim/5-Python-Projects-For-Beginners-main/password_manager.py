import time
import cryptography.fernet

'''
def write_key():
    key = cryptography.fernet.Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = cryptography.fernet.Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

print('顯示資料')
view()

print('新增資料')
string_data1 = 'aaaa_' + time.strftime("%Y%m%d_%H%M%S", time.localtime())
string_data2 = 'bbbb_' + time.strftime("%Y%m%d_%H%M%S", time.localtime())

name = string_data1
pwd = string_data2

with open('passwords.txt', 'a') as f:
    f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


