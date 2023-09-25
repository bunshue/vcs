from translate import Translator

translator = Translator(from_lang='zh-Hant', to_lang='en')
while True:
    text = input('輸入要翻譯的中文文句 (直接按 ENTER 鍵結束)：')
    if text == '':
        break
    translation = translator.translate(text)
    print('翻譯結果：' + translation)
    