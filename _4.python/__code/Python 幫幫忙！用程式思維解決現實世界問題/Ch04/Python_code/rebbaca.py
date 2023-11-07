import sys
import os
import random 
from collections import defaultdict, Counter

def main(): 
    message = input("Enter plaintext or ciphertext: ") 
    process = input("Enter 'encrypt' or 'decrypt': ") 
    while process not in ('encrypt', 'decrypt'): 
        process = input("Invalid process. Enter 'encrypt' or 'decrypt': ") 
    shift = int(input("Shift value (1-366) = "))
    while not 1 <= shift <= 366: 
        shift = int(input("Invalid value. Enter digit from 1 to 366: ")) 
    infile = input("Enter filename with extension: ") 
    if not os.path.exists(infile): 
        print("File {} not found. Terminating.".format(infile), file=sys.stderr) 
        sys.exit(1) 
    text = load_file(infile) 
    char_dict = make_dict(text, shift) 

    if process == 'encrypt':
        ciphertext = encrypt(message, char_dict) 
        if check_for_fail(ciphertext): 
            print("\nProblem finding unique keys.", file=sys.stderr) 
            print("Try again, change message, or change code book.\n", file=sys.stderr) 
            sys.exit() 
        print("\nCharacter and number of occurrences in char_dict: \n") 
        print("{: >10}{: >10}{: >10}".format('Character', 'Unicode', 'Count')) 
        for key in sorted(char_dict.keys()):                   
            print('{:>10}{:>10}{:>10}'.format(repr(key)[1:-1],str(ord(key)),len(char_dict[key]))) 
        print('\nNumber of distinct characters: {}'.format(len(char_dict))) 
        print("Total number of characters: {:,}\n".format(len(text))) 
        print("encrypted ciphertext = \n {}\n".format(ciphertext)) 
        print("decrypted plaintext = ")

        for i in ciphertext:
            print(text[i - shift], end='', flush=True) 

    elif process == 'decrypt': 
        plaintext = decrypt(message, text, shift) 
        print("\ndecrypted plaintext = \n {}".format(plaintext))

def load_file(infile): 
    """載入文字檔並以小寫字串傳回""" 
    with open(infile) as f:
        loaded_string = f.read().lower()
    return loaded_string 

def make_dict(text, shift): 
    """傳回字元字典及已偏移的索引""" 
    char_dict = defaultdict(list)
    for index, char in enumerate(text):
        char_dict[char].append(index + shift) 
    return char_dict
def encrypt(message, char_dict):
    """將訊息中的字元代換成索引值後傳回 (list)"""
    encrypted = []
    for char in message.lower():
        if len(char_dict[char]) > 1:  # 從眾多索引選一個
            index = random.choice(char_dict[char])
        elif len(char_dict[char]) == 1:  # 若只有單一選項，不能使用 random.choice
            index = char_dict[char][0]
        elif len(char_dict[char]) == 0:  # 無該字元，找不到其索引 
            print("\nCharacter {} not in dictionary.".format(char), file=sys.stderr)
            continue
        encrypted.append(index)
    return encrypted

def decrypt(message, text, shift): 
    """將密文 list 解密並傳回明文字""" 
    plaintext = '' 
    indexes = [s.replace(',', '').replace('[', '').replace(']', '') 
               for s in message.split()] 
    for i in indexes: 
        plaintext += text[int(i) - shift] 
    return plaintext

def check_for_fail(ciphertext): 
    """若密文中含重複密鑰，就傳回 True""" 
    check = [k for k, v in Counter(ciphertext).items() if v > 1] 
    if len(check) > 0: 
        return True

if __name__ == '__main__': 
    main()
