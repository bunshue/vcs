# ch16_34.py
import re

def validate_and_format_credit_card(number):
    # 定義Visa信用卡號碼的正則表達式, Visa卡號以4開頭, 並有16位數字
    pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?)$"  

    # 使用match方法檢查提供的卡號是否符合正則表達式模式。
    match = re.match(pattern, number)
    if match:
        # 如果匹配成功，使用findall方法分組每四位數字
        # 然後用join方法將這些組用 "-" 連接成一個格式化的字串
        formatted = "-".join(re.findall(r"....", number))
        return True, formatted  # 返回一個元組和驗證成功格式化的卡號
    return False, None          # 如果匹配不成功, 返回False和None

# 測試卡號
card_number = "4111111111111111"
is_valid, formatted = validate_and_format_credit_card(card_number)
print(is_valid, formatted)      # 輸出結果應該為True和格式化後的卡號






