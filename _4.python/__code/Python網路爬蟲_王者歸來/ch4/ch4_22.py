# ch4_22.py
import requests

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
try:
    htmlfile = requests.get(url)                        # 將檔案下載至htmlfile
    print('下載成功')
except Exception as err:
    print('下載失敗')

fn = 'iris.csv'                                         # 未來儲存鳶尾花的檔案
with open(fn, 'wb') as fileobj:                         # 開啟iris.csv
    for diskstorage in htmlfile.iter_content(10240):
        size = fileobj.write(diskstorage)               # 寫入














