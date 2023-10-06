# 3-1-4 函式的一級物件特性: 函式可構成巢狀結構 (2)

def get_speak_func(volume):
    
    def whisper(text):
        return text.lower() + '...'
    
    def yell(text):
        return text.upper() + '!'
    
    if volume > 0.5:
        return yell
    else:
        return whisper


print(get_speak_func(0.3))
print(get_speak_func(0.7))

speak_func = get_speak_func(0.7)
print(speak_func('Hello'))