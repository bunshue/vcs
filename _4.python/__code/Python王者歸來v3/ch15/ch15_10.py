# ch15_10.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except Exception:
        print(f"Exception找不到 {fn} 檔案")
    else:
        wordList = data.split()     # 將文章轉成串列
        print(f"{fn} 文章的字數是 {len(wordList)}")   # 文章字數

files = ['data1.txt', 'data2.txt', 'data3.txt']       # 檔案串列
for file in files:
    wordsNum(file)



