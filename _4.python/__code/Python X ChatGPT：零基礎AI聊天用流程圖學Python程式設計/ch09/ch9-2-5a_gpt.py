def concatenate_strings(lst1):
    """
    從lst1中抽出是字串的項目，並連接成一個字串回傳。

    :param lst1: 一個含有多個項目的串列
    :type lst1: list
    :return: 連接所有字串項目後的字串
    :rtype: str
    """

    str_lst = [item for item in lst1 if isinstance(item, str)]
    return ''.join(str_lst)

my_list = ['Hello', 42, 'World', True, 'Python']
result = concatenate_strings(my_list)
print(result)  # 輸出：HelloWorldPython

