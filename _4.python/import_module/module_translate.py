"""

翻譯功能

"""
print("------------------------------------------------------------")  # 60個

import translate

translator = translate.Translator(from_lang="zh-Hant", to_lang="en")

text = "豬頭"

translation = translator.translate(text)
print("翻譯結果：" + translation)

print("------------------------------------------------------------")  # 60個


import translate


"""
'en': '英文'
'ja': '日文'
'ko': '韓文'
'th': '泰文'
'vi': '越南文'
'fr': '法文'
"""

from_lang = "zh-Hant"
to_lang = "en"

text = "尋找一個資料夾下的所有檔案"

translator = translate.Translator(from_lang=from_lang, to_lang=to_lang)
translation = translator.translate(text)  # 進行翻譯
print(translation)


print("------------------------------------------------------------")  # 60個

import translate

print("英翻中")

trans = translate.Translator(from_lang="english", to_lang="chinese")

text = "Welcome to the United States and have a nice day."
print("Copied word : ", text)
translation = trans.translate(text)

print(translation)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
