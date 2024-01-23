import re

text = "這個是、那個是、那個是、哪個是"
word1 = "這.是"
word2 = ".個是"

pattern = re.compile(word1)
count = len(re.findall(pattern, text))
print(word1, ":", count, "個")

pattern = re.compile(word2)
count = len(re.findall(pattern, text))
print(word2, ":", count, "個")


import re

text = "這個是測試資料。"
word1 = ".個是"
word2 = "那個是"

print("置換前 :", text)
pattern = re.compile(word1)
text = re.sub(pattern, word2, text)
print("置換後 :", text)


