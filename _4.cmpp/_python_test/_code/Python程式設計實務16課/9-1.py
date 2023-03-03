# _*_ coding: utf-8 _*_
# 程式 9-1  (Python 3 version)
from urllib.parse import urlparse

url = 'https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&filter_uid=none&listKeyword=&pageNum=2&pageSize=18&view_mode=listView&subSite=main&l=ch&tagUid='

uc = urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
    print(cmd)
