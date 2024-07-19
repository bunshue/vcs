import webbrowser

print("------------------------------------------------------------")  # 60個

webbrowser.open("http://xkcd.com/353/")

print("------------------------------------------------------------")  # 60個

import webbrowser

address = "花蓮市中正路"
webbrowser.open("http://www.google.com.tw/maps/place/" + address)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import webbrowser

print("用預設的瀏覽器開啟網頁")
url = "https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"
print(url)
webbrowser.open(url)


"""
print('用預設瀏覽器開啟網頁')
import webbrowser
filename = 'C:/_git/vcs/_1.data/______test_files1/beautifulsoup_data.html'
webbrowser.open(filename)
"""


print("webbrowser")
import webbrowser

url = "http://www.mcut.edu.tw"
webbrowser.open(url)

print("------------------------------------------------------------")  # 60個

print("webbrowser")
# address = input("請輸入地址 : ")
address = "新竹市東區榮光里中華路二段445號"

url = "http://www.google.com.tw/maps/place/" + address

webbrowser.open(url)

# re 使用

# 明志科技大學
url = "http://www.mcut.edu.tw"
response = requests.get(url)
if response.status_code == requests.codes.ok:
    print("欲搜尋的字串")
    pattern = "英文"

    # 使用方法1
    if pattern in response.text:  # 方法1
        print(f"搜尋 {pattern} 成功")
    else:
        print(f"搜尋 {pattern} 失敗")

    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, response.text)  # 方法2
    if name:
        print(f"{pattern} 出現 {len(name)} 次")
    else:
        print(f"{pattern} 出現 0 次")
else:
    print("網頁下載失敗")

print("------------------------------------------------------------")  # 60個

import webbrowser

# 使用默認瀏覽器打開 html 文件
webbrowser.open("tmp_導出圖表.html", new=1)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
