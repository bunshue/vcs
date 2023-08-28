import speech_recognition as sr

r = sr.Recognizer()        
r.energy_threshold = 4000   #設定聲音辨識的靈敏度
while True:           
    try:
        with sr.Microphone() as source:  # 打開麥克風
            print("請開始說話:")
            audio = r.listen(source) #等待語音輸入        
            listen_text = r.recognize_google(audio, language="zh-TW")
            print(listen_text + "\n")
            if listen_text=="結束":
                break
    except:
        print("語音無法辨識\n")
        