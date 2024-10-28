"""
cryptography


"""

import cryptography.fernet

print("------------------------------------------------------------")  # 60個

key_filename = "data/key.key"
filename = "my_secret_data.txt"

"""
def write_key():
    key = cryptography.fernet.Fernet.generate_key()
    with open(key_filename, "wb") as key_file:
        key_file.write(key)"""


def load_key():
    file = open(key_filename, "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = cryptography.fernet.Fernet(key)

print("新增一筆資料")
name = "david"
pwd = "0123456789"

with open(filename, "a") as f:
    f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

print("顯示所有資料")

with open(filename, "r") as f:
    for line in f.readlines():
        data = line.rstrip()
        user, passw = data.split("|")
        print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
