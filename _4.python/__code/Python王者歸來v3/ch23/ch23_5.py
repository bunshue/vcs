# ch23_5.py
import requests
import re

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("請輸入欲搜尋的字串 : ")    # 讀取字串
# 使用方法1
    if pattern in htmlfile.text:                # 方法1
        print(f"搜尋 {pattern} 成功")
    else:
        print(f"搜尋 {pattern} 失敗")
    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, htmlfile.text)   # 方法2
    if name:
        print(f"{pattern} 出現 {len(name)} 次")
    else:
        print(f"{pattern} 出現 0 次")
else:
    print("網頁下載失敗")


