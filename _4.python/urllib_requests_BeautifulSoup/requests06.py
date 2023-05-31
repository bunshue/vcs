print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')


import pprint as pp
import time, requests

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

pp.pprint(pages)
print()
print(pages)

for page in pages:
    html = requests.get(page).text
    pp.pprint(html)
    time.sleep(3)
    print("=========================")


print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')

import pprint as pp
import time, requests

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

pp.pprint(pages)
print()
print(pages)

for pg_no, page in enumerate(pages, 1):
    html = requests.get(page).text
    filename = "page-{}.txt".format(pg_no)
    with open(filename, "wt") as fp:
        fp.write(html)
    print(filename, "儲存完成！")
    time.sleep(3)
    print("=========================")


