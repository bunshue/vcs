## Visual C# & Python by bunshue

網路爬蟲（英語：web crawler）

高	網路類：request、bs4
	影像類：opencv、PIL、webcam、
	數據類：scipy、scikit-learn、、、、、、、、

中	tk、matplotlib、numpy、pandas、資料庫、各種套件(sys、os、random、time、serial、)、、、、、
	(turtle、pygame、、、)

基	開發環境、IO、資料型態、容器DSLT、流程控制、函數(內建、自訂)、類別、檔案讀寫、、、

下面這張圖來自於[菜鳥教程](http://www.runoob.com)網站，它展示瞭如果根據應用程序的需要來設置操作模式。

![](./res/file-open-mode.png)



# Info

本 repo 是 **《Python 投資停看聽：運用 Open data 打造自動化燈號，學會金融分析精準投資法》** 的輔助資源，裡面包含了程式碼，以及一些勘誤的內容。

## 關於本書

* 作者： 吳東霖  
* 出版社：博碩  
* 出版日期：2022/04/29
* 語言：繁體中文
* ISBN：9786263330863
* 規格：平裝 / 288頁 / 17 x 23 x 1.44 cm / 普通級 / 單色印刷 / 初版
* 出版地：台灣
* 本書分類：電腦資訊> 程式設計/APP開發> Python

## 勘誤與補充

### Ch2

* 勘誤 p.30：最後一行「print(x) # 答案為：2」，正確為「print(x) # 答案為：6」並非「2」。
* 勘誤 p.36：在`len()`的範例中，`list1 = [list1, list1, list1, list1]`為錯誤的變數名稱，應該是為`list2`，也就是：`list2 = [list1, list1, list1, list1]`。

### Ch3

* 補充 p.113～p.117 的程式碼補充與勘誤，包含「把歷史資料放入資料庫」（[stock_history.py](ch3/../code/ch3/stock_history.py)）、「每日市場資料放入資料庫」（[get_market_info.py](ch3/../code/ch3/get_market_info.py)）。

### Ch4

* 補充 p.128 中 Windows 安裝 TA-Lib 的方法：流程寫在[install_ta-lib.md](code/ch4/install_ta-lib.md)
* 勘誤 p.131：`c.plot()`應為`c_5.plot()`。

### Ch5

* 補充 p.203：範例的變動率為「0」，當有資訊後會呈現為：

```
* 外資臺指期貨留倉是多單: False
* 外資臺指期貨留倉數變動率: -0.23807307423784035
* 自營商臺指期貨留倉是多單: True
* 自營商臺指期貨留倉數變動率: 0.24743646901471245
* 投信臺指期貨留倉是多單: False
* 投信臺指期貨留倉數變動率: -0.007489917418859228
```

### Ch6

* 勘誤 p.235：〈Azure Database for MySQL〉一節中的`試用於`，應為`適用於`。

# 聯繫

如果對於本書或是內容有疑問，歡迎在這邊提出，或是用email聯繫：`eyelash.94500@gmail.com`
