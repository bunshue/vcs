"""

翻譯功能

"""

import sys

print("------------------------------------------------------------")  # 60個

import translate

translator = translate.Translator(from_lang="zh-Hant", to_lang="en")

text = "豬頭"
text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

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

from deep_translator import GoogleTranslator

# 要翻譯的文本
text = "早安"
text = "名偵探柯南是根據日本漫畫家青山剛昌著名原作推理漫畫名偵探柯南改編的動畫作品。"

# 翻譯成英文
translator = GoogleTranslator(source="auto", target="en")
translation_en = translator.translate(text)
print("英文:", translation_en)

# 翻譯成日文, 另一種寫法
translation_ja = GoogleTranslator(source="auto", target="ja").translate(text)
print("日文:", translation_ja)

# 翻譯成韓文
translation_ko = GoogleTranslator(source="auto", target="ko").translate(text)
print("韓文:", translation_ko)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
