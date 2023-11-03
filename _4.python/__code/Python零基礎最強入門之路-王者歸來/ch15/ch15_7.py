# ch15_7.py
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

file = 'ch15_6.txt'                 # 設定欲開啟的檔案
wordsNum(file)



