def convert_to_f(celsius):
    """
    將攝氏溫度轉換成華氏溫度
    :param celsius: float, 攝氏溫度
    :return: float, 轉換成的華氏溫度
    """
    fahrenheit = (9.0 * celsius) / 5.0 + 32.0  # 計算華氏溫度
    return fahrenheit


# 呼叫convert_to_f()函數並印出結果
print(convert_to_f(100))
