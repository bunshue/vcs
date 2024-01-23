from pathlib import Path

infile = "test.txt"                 #要載入的檔案名稱
try:
    p = Path(infile)                #文字檔案的
    text = p.read_text(encoding="UTF-8")    #載入文字
    print(text)                     #顯示
except:
    print("程式執行失敗。")          #出現錯誤時