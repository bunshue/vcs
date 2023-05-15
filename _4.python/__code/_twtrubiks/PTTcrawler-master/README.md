# PTTcrawler (PTT文章爬蟲) for Windows and Linux
A crawler for web PTT  (PTT文章爬蟲)  json格式 on python
* [Demo Video](https://youtu.be/13l3ZGaH4Zo)  - Linux

<b> 2019/1/11 改為 python 3.6.6，並使用 oop 的方式 refactor，如需使用 Python 2.7.3 請回到 ccc054c8976fe6443436d368c9877da5e1a4139d </b>

## 特色
* 抓取PTT文章並輸出 json 格式，包含文章作者 , 標題 , 日期 , IP , 內文 , 推噓文 以及 推噓文總數

## 輸出格式 ( JSON )

    "a_ID": 編號,
    "b_作者": 作者名,
    "c_標題": 標題,
    "d_日期": 發文時間,
    "e_ip": 發文ip,
    "f_內文": 內文,
    "g_推文": {
        "推文編號": {
            "狀態": 推 or 噓 or →,
            "留言內容": 留言內容,
            "留言時間": 留言時間,
            "留言者": 留言者
        }
    },
    "h_推文總數": {
        "all": 推文數目,
        "b": 噓數,
        "g": 推數,
        "n": →數
    }
    
## 使用方法
```
python app.py [板名]  [抓取頁數]
```

## 執行範例
爬 PTT Gossiping 版 10頁 文章內容
```
python app.py  Gossiping  10
```
假設總共有100頁，則會爬取 <br>
https://www.ptt.cc/bbs/Gossiping/index100.html 至 https://www.ptt.cc/bbs/Gossiping/index109.html 之間的內容。

## 執行畫面 
![alt tag](http://i.imgur.com/M1mCln6.jpg)
![alt tag](http://i.imgur.com/n2bGJ3F.jpg)

可使用觀看 JSON 的工具，例如  [jsoneditoronline](http://www.jsoneditoronline.org/) <br><br>
![alt tag](http://i.imgur.com/XVr0dCz.jpg)
  
## Environment
* Python 3.6.6

## License
MIT license

