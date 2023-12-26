# ex13_11.py
import string
import random

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串

def decrypt(cipher, decryDict):         # 解密文件
    text = []
    for i in cipher:                    # 執行每個字元解密
        v = decryDict[i]                # 加密
        text.append(v)                  # 解密結果
    return ''.join(text)                # 將串列轉成字串
   
abc = string.printable[:-5]             # 取消不可列印字元
newAbc = abc[:]                         # 產生新字串拷貝
abclist = list(newAbc)                  # 轉成串列
random.shuffle(abclist)                 # 打亂串列順序
subText = ''.join(abclist)              # 轉成字串
encry_dict = dict(zip(subText, abc))    # 建立加密字典
decry_dict = dict(zip(abc, subText))    # 建立解密字典
print("列印解碼字典\n", decry_dict)     # 列印解碼字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)
print("原始字串 ", msg)
print("加密字串 ", ciphertext)
decryMsg = decrypt(ciphertext, decry_dict)
print("解密字串 ", decryMsg)







