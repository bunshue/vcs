filename = 'my_secret_data.txt'

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
    with open(filename, 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

print('新增資料')
name = "new name"
pwd = "new password"

with open(filename, 'a') as f:
    f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

print('顯示資料')
view()


