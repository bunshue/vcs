# FaceDetect

臉部偵測 use Python

Python OpenCV Tutorial

* [Demo Video](https://youtu.be/OahDm1tFuQY) - Windows - 2017/4/27 update
* [Demo Video](https://youtu.be/TnnSfnjw6js) - Windows

## 特色

* 圖片、影片 臉部偵測

## 建立環境

**Python 3.5.2 + OpenCV 3.1.0**   (建議用這個，更簡單)
請參考

[如何安裝 OpenCV3 - 使用 Anaconda](https://github.com/twtrubiks/FaceDetect/tree/master/How%20Easy%20Install%20OpenCV%20%20for%20Python%20use%20Anaconda)

**Python 2.7.3 + OpenCV 2.4.12**
請參考

可參考 [如何在Windows安裝OpenCV Python設定](https://github.com/twtrubiks/FaceDetect/tree/master/How%20Install%20OpenCV%20in%20on%20Windows%20for%20Python)

## 執行範例

Python 3.5.2 + OpenCV 3.1.0

```cmd
python face_detect_python3.py
```

程式執行後，會自動跳出偵測臉部的圖片

![alt tag](http://i.imgur.com/u8m9lUf.jpg)

透過 camera 偵測人臉

```cmd
python face_detect_camera.py
```

圖片會輸出到 camera 資料夾裡，會存 10 張。

![alt tag](http://i.imgur.com/YEcaMRg.jpg)

Python 2.7.3 + OpenCV 2.4.12

```cmd
python face_detect_python2.py test1.jpg haarcascade_frontalface_alt.xml
```

## 輸出

目錄底下會多出一張名稱為 face_detection.jpg 的圖片

![alt tag](http://i.imgur.com/evl398U.jpg)

## 備註

更多的 **haarcascade** 可到 **opencv** 路徑裡 **opencv\sources\data\haarcascades** 取得，

路徑底下還有 **haarcascade_eye.xml** 偵測眼睛之類的，大家可以自行摸索。

最後，請注意，這是 **臉部偵測** ，並不是 **臉部辨識**

## 其他

更多的資訊可參考原作者

Run the code like this:

```python
python face_detect.py abba.png haarcascade_frontalface_default.xml
```

If you want to understand how the code works, the details are here:

```url
https://realpython.com/blog/python/face-recognition-with-python/
```

## 後記

本篇文章所介紹的是 **臉部偵測 ( Face Detection )**，並不是 **臉部辨識 ( Face Recognize)**

如果要辦到 **臉部辨識 ( Face Recognize)**，OpenCV 其實也可以辦到，可以透過OpenCV官網提供的演算法來完成，

OpenCV 官方有提供三種 Face Recognition 演算法，分別為

EigenFaceRecognizer、FisherFaceRecognizer、 LBPHFaceRecognizer。

最後我選擇 LBPHFaceRecognizer，為什麼不選 EigenFaceRecognizer 或 FisherFaceRecognizer 呢?

因為 LBPHFaceRecognizer 有幾個優點：

* 訓練和比對的圖片大小可以不一致。
* 比較不會受到光線以及角度的影響 ( 辨識率 )。
* 可以直接更新訓練資料庫，不用全部重新訓練。

流程大致上是
收集人臉 --> 訓練  --> 得到一個 dataSet
然後透過這個 dataSet  下去辨識。

我認為使用 OpenCV 提供的 Face Recognition 演算法效果沒有非常好，

或許可以考慮用目前最紅的深度學習 ( Deep learning ) 處理精準度的問題，

之前有稍微接觸深度學習結合人臉辨識，可以參考 [face-recognition-notes](https://github.com/twtrubiks/face-recognition-notes)

## 執行環境

* Windows 10
* Python 3.5.2
* OpenCV 3.1.0

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
