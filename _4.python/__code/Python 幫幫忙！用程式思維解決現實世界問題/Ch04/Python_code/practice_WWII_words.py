import sys
import os
import random
import string
from collections import defaultdict, Counter

def main():
    message = input("Enter plaintext or ciphertext: ") 
    process = input("Enter 'encrypt' or 'decrypt': ")  
    shift = int(input("Shift value (1-365) = "))
    infile = input("Enter filename with extension: ")
    
    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.exit(1)        
    word_list = load_file(infile)
    word_dict = make_dict(word_list, shift)
    letter_dict = make_letter_dict(word_list)

    if process == 'encrypt':
        ciphertext = encrypt(message, word_dict, letter_dict)          
        count = Counter(ciphertext)        
        encryptedWordList = []
        for number in ciphertext:
            encryptedWordList.append(word_list[number - shift])
        
        print("\nencrypted word list = \n {} \n"
              .format(' '.join(encryptedWordList)))           
        print("encrypted ciphertext = \n {}\n".format(ciphertext))
        
        # 透過解密密文來確認加密是否成功
        print("decrypted plaintext = ")
        singleFirstCheck = False
        for cnt, i in enumerate(ciphertext):
            if word_list[ciphertext[cnt]-shift] == 'a' and \
               word_list[ciphertext[cnt+1]-shift] == 'a':
                continue
            if word_list[ciphertext[cnt]-shift] == 'a' and \
               word_list[ciphertext[cnt-1]-shift] == 'a':
                singleFirstCheck = True
                continue
            if singleFirstCheck == True and cnt<len(ciphertext)-1 and \
               word_list[ciphertext[cnt]-shift] == 'the' and \
                             word_list[ciphertext[cnt+1]-shift] == 'the':
                continue
            if singleFirstCheck == True and \
               word_list[ciphertext[cnt]-shift] == 'the' and \
                             word_list[ciphertext[cnt-1]-shift] == 'the':
                singleFirstCheck = False
                print(' ', end='', flush=True)
                continue
            if singleFirstCheck == True:
                print(word_list[i - shift][0], end = '', flush=True)
            if singleFirstCheck == False:
                print(word_list[i - shift], end=' ', flush=True)

    elif process == 'decrypt':
        plaintext = decrypt(message, word_list, shift)
        print("\ndecrypted plaintext = \n {}".format(plaintext))

def load_file(infile):
    """載入文字檔並以小寫字串傳回"""
    with open(infile, encoding='utf-8') as file:
        words = [word.lower() for line in file for word in line.split()]
        words_no_punct = ["".join(char for char in word if char not in \
                                 string.punctuation) for word in words]
    return words_no_punct

def make_dict(word_list, shift):
    """傳回字元字典及已偏移的索引"""
    word_dict = defaultdict(list)
    for index, word in enumerate(word_list):
        word_dict[word].append(index + shift)
    return word_dict

def make_letter_dict(word_list):
    firstLetterDict = defaultdict(list)
    for word in word_list:
        if len(word) > 0:
            if word[0].isalpha():
                firstLetterDict[word[0]].append(word)
    return firstLetterDict

def encrypt(message, word_dict, letter_dict):
    """將訊息中的字元代換成索引值後傳回 (list)"""
    encrypted = []
    # 從訊息中移除標點符號
    messageWords = message.lower().split()
    messageWordsNoPunct = ["".join(char for char in word if char not in \
                                 string.punctuation) for word in messageWords]    
    for word in messageWordsNoPunct:
        if len(word_dict[word]) > 1:  # 從眾多索引選一個
            index = random.choice(word_dict[word])
        elif len(word_dict[word]) == 1:  # 若只有1個選項，Random.choice 無法使用
            index = word_dict[word][0]
        elif len(word_dict[word]) == 0:  # 無該字元，找不到其索引 
            encrypted.append(random.choice(word_dict['a']))
            encrypted.append(random.choice(word_dict['a']))

            for letter in word:
                if letter not in letter_dict.keys():
                    print('\nLetter {} not in letter-to-word dictionary.'
                          .format(letter), file=sys.stderr)
                    continue
                if len(letter_dict[letter])>1:
                    newWord =random.choice(letter_dict[letter])
                else:
                    newWord = letter_dict[letter][0]
                if len(word_dict[newWord])>1:
                    index = random.choice(word_dict[newWord])
                else:
                    index = word_dict[newWord][0]
                encrypted.append(index)
                
            encrypted.append(random.choice(word_dict['the']))
            encrypted.append(random.choice(word_dict['the']))
            continue
        encrypted.append(index)
    return encrypted

def decrypt(message, word_list, shift):
    """將密文 list 解密並傳回明文字"""
    plaintextList = []
    indexes = [s.replace(',', '').replace('[', '').replace(']', '')
               for s in message.split()]
    for count, i in enumerate(indexes):
        plaintextList.append(word_list[int(i) - shift])
    return ' '.join(plaintextList)

def check_for_fail(ciphertext):
    """若密文中含重複密鑰，就傳回 True"""
    check = [k for k, v in Counter(ciphertext).items() if v > 1]
    if len(check) > 0:
        print(check)
        return True

if __name__ == '__main__':
    main()
