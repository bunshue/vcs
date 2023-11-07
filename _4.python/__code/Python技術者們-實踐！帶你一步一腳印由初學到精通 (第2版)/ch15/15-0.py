import speech_recognition as sr  # 匯入套件並命名為 sr


def bot_listen():
    recong = sr.Recognizer()            # 建立辨識物件
    with sr.Microphone() as source:     # 打開麥克風取得聲音
        audioData = recong.listen(source)       # 讓辨識物件聽到的聲音
    try:
        text = recong.recognize_google(
            audioData, language='zh-tw')     # 將聲音資料翻成文字
        return text
    except:
        return '聽不懂'


question = bot_listen()
print(question)
