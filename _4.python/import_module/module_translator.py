"""
各種翻譯功能

常见的Python翻译插件
插件名称 	功能描述
googletrans 	使用Google Translate API来进行翻译
translate 	提供多种翻译服务选项
goslate 	通过谷歌翻译进行文本翻译
textblob 	提供自然语言处理功能，包括翻译
"""
import sys

print("------------------------------------------------------------")  # 60個

# 1. 使用googletrans库进行翻译

"""
# 必需版本
pip install googletrans==4.0.0-rc1
"""

# 查看文字翻譯可用語言
import googletrans

cc = googletrans.LANGCODES
print("翻譯語系列表")
# print(cc)

from googletrans import Translator


def translate_text(text, dest="en"):
    translator = Translator()
    result = translator.translate(text, dest).text
    return result


result1 = translate_text(text="水之呼吸", dest="en")
result2 = translate_text("水之呼吸", dest="ja")
result3 = translate_text("水之呼吸", "ko")
print(result1)
print(result2)
print(result3)


from googletrans import Translator

# 创建翻译器对象
translator = Translator()

# 待翻译文本
text = "Hello, how are you?"

# 进行中文翻译
translated = translator.translate(text, dest="zh-cn")

print(f"原文: {text}")
print(f"翻译: {translated.text}")


print(translated)

print("------------------------------------------------------------")  # 60個

# 2. 使用translate库

# pip install translate
from translate import Translator

# 创建翻译器对象，指定目标语言为中文
translator = Translator(to_lang="zh")

# 待翻译文本
text = "Python is a popular programming language."

# 进行翻译
translated = translator.translate(text)

print(f"原文: {text}")
print(f"翻译: {translated}")

print("------------------------------------------------------------")  # 60個

# 3. 使用TextBlob进行翻译
# TextBlob是一个用于处理文本数据的Python库，其功能也包括翻译。首先安装该库：
# pip install textblob

from textblob import TextBlob

# 待翻译文本
text = "Where is the nearest subway station?"

# 创建TextBlob对象
blob = TextBlob(text)

""" NG
# 进行翻译
translated = blob.translate(to='fr')

print(f"原文: {text}")
print(f"翻译: {translated}")
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from google_trans_new import google_translator

translator = google_translator()
translate_text = translator.translate("สวัสดีจีน", lang_tgt="en")
print(translate_text)

from google_trans_new import google_translator

translator = google_translator()

text = "今天天氣很好"

word = translator.translate(text, lang_src="zh-TW", lang_tgt="ja", pronounce=True)
# print(word)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 3030
print("------------------------------")  # 30個


"""
google_trans_new：文字翻譯
pip install google_trans_new

"""


"""fail
from google_trans_new import google_translator
translator = google_translator()
text="今天天氣很好"
word = translator.translate(text, lang_src="zh-TW", lang_tgt="ja", pronounce=True)
print(word)

from google_trans_new import google_translator
translator = google_translator()
print(translator.translate("今日の天気は良いです"))

lang = translator.detect("今日の天気は良いです")
print(lang)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# !pip install google_trans_new


# from google_trans_new import google_translator
# from google_trans_new import google_translator


translator = google_translator()
ret = translator.translate(content, lang_tgt="zh-TW")
print("找到文字 :", ret)
