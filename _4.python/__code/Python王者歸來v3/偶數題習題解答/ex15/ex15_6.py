# ex15_6.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % fn)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數
        return len(wordList)

def lenWord(fn):
    """檢查檔案長度必須是10到35個字元"""
    wdlen = wordsNum(fn)                              # 檔案長度
    if wdlen < 10:                                    # 檔案長度不足            
        raise Exception('檔案長度不足')
    if wdlen > 35:                                    # 檔案長度太長
        raise Exception('檔案長度太長')
    print('檔案長度正確')

for file in ("d1.txt","d2.txt","d3.txt","d4.txt","d5.txt"):  # 測試系列檔案
    try:
        lenWord(file)
    except Exception as err:
        print("檔案長度檢查異常發生: ", str(err))


