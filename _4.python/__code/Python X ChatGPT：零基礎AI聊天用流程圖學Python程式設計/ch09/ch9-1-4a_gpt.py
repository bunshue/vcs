def clean_string(s):
    """
    刪除字符串中的 '\n', '\r' 和前後的空白

    :param s: str，待處理的字符串
    :return: str，刪除後的字符串
    """
    # 刪除 '\n' 和 '\r'
    s = s.replace('\n', '').replace('\r', '')
    # 刪除前後空白
    s = s.strip()
    return s

str1 = "  Python is a \nprogramming language.\n\r   "
cleaned_str = clean_string(str1)
print(cleaned_str)  # "Python is a programming language."

