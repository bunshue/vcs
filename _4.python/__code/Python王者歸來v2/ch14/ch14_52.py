# ch14_52.py
import string

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-3]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串字串
encry_dict = dict(zip(subText, abc))    # 建立字典

fn = "zenofPython.txt"
with open(fn) as file_Obj:              # 開啟檔案
    msg = file_Obj.read()               # 讀取檔案
    
ciphertext = encrypt(msg, encry_dict)

print("原始字串")
print(msg)
print("加密字串")
print(ciphertext)








