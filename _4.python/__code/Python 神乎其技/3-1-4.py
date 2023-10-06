# 3-1-4 函式的一級物件特性: 函式可構成巢狀結構 (1)

def speak(text):
    
    def whisper(t):
        return t.lower() + '...'
    
    return whisper(text)


print(speak('Hello, World'))
