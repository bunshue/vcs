# 3-1-6 函式的一級物件特性: 內部函式可記住父函式的參數狀態 (1)

def get_speak_func(text, volume):
    
    def whisper():
        return text.lower() + '...'
    
    def yell():
        return text.upper() + '!'
    
    if volume > 0.5:
        return yell
    else:
        return whisper


func = get_speak_func('Hello, World', 0.7)
print(func())
