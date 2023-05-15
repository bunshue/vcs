# 如何在Windows安裝OpenCV Python設定

How Install OpenCV in  on Windows for Python

* [Demo Video](https://www.youtube.com/watch?v=cDI8j8Udq68) - Windows

## 安裝  numpy

先下載numpy

到 [numpy](https://pypi.python.org/pypi/numpy)

下載對應的NumPy版本

我在這裡是下載 numpy-1.11.0-cp27-none-win_amd64.whl (64位元)

接著使用cmd (命令提示字元) 輸入

```cmd
pip install numpy-1.11.0-cp27-none-win_amd64.whl
```

如果沒出現錯誤訊息，則會正常安裝

可再用下面指令檢查是否安裝成功

使用IDLE (Python GUI) 輸入

```python
import numpy
numpy.__version__
```

如安裝成功，則會顯示安裝的版本

'1.11.0'

如下圖

![alt tag](http://i.imgur.com/77S8vj2.jpg)

## 如何安裝OpenCV

下載OpenCV

到官網下載[OpenCV](http://opencv.org/downloads.html)

我在這裡下載的版本是 OpenCV 2.4.12 Windows Pre-built

將OpenCV解壓縮到任一地方，例如C:\，解壓後會多出一個名稱為opencv的資料夾

再到opencv資料夾搜尋 **cv2.pyd** ，尋找自己對應的的位元

**cv2.pyd** 的資料夾路徑為

C:\opencv\build\python\2.7\x86  (32位元)

C:\opencv\build\python\2.7\x64  (64位元)

將 **cv2.pyd** 複製到 C:\Python27\Lib\site-packages 路徑下

可再用下面指令檢查是否安裝成功

使用IDLE (Python GUI) 輸入

```python
import cv2
print cv2.__version__
```

如安裝成功，則會顯示安裝的版本

'2.4.12'

如下圖

![alt tag](http://i.imgur.com/Njp1IUk.jpg)

## Environment

* Windows 8.1
* Python 2.7.3
* OpenCV 2.4.12
* numpy 1.11.0
