"""讀取文字檔並以字串形式傳回"""

def text_to_string(filename):
    strings = []
    with open(filename, encoding='utf-8', errors='ignore') as f:
        strings.append(f.read())
    return '\n'.join(strings)
