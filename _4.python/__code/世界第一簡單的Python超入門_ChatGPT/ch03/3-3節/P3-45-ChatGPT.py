def washing_machine(mode):
    if mode == 'gentle':
        return '輕柔清洗'
    elif mode == 'strong':
        return '強力清洗'
    else:  # 如果 mode 不是 'gentle' 或 'strong'，則預設為 'normal'
        return '一般清洗'

# 測試函式
print(washing_machine('gentle'))  # 輸出: 輕柔清洗
print(washing_machine('strong'))  # 輸出: 強力清洗
print(washing_machine('normal'))  # 輸出: 一般清洗
print(washing_machine('other'))  # 輸出: 一般清洗





