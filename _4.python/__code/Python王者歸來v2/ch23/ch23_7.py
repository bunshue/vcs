# ch23_7.py
import requests
import re

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("請輸入欲搜尋的字串 : ")    # pattern存放欲搜尋的字串
# 使用方法1
    if pattern in htmlfile.text:                # 方法1
        print(f"搜尋 {pattern} 成功")
    else:
        print("搜尋 %s 失敗" % pattern)
    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, htmlfile.text)   # 方法2
    if name != None:
        print(f"{pattern} 出現 {len(name)} 次")
    else:
        print(f"{pattern} 出現 0 次")
else:
    print("網頁下載失敗")


