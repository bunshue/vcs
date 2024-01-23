import unicodedata

text = "「全形１２．３」「全形Ａｂｃ！（＠）」「半形片假名」「圈圈數字①②③」「符號㏊」"

print("轉換前 :", text)
text = unicodedata.normalize("NFKC", text)
print("轉換後 :", text)
