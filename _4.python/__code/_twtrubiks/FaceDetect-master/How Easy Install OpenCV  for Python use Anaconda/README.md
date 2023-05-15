# 如何安裝 OpenCV3 - 使用 Anaconda

How Easy Install OpenCV3 for Python use Anaconda

* [Demo Video](https://youtu.be/u90KaU6svc4) - Use Anaconda

大約一年前寫過一篇 [如何在Windows安裝OpenCV Python設定](https://github.com/twtrubiks/FaceDetect/blob/master/How%20Install%20OpenCV%20in%20on%20Windows%20for%20Python/README.md) ，那時候安裝OpenCV比較麻煩，

環境要弄很久，現在我們可以透過 [Anaconda](https://www.continuum.io/downloads)  ，讓安裝 OpenCV 變得更容易。

## 安裝  Anaconda

請先依照自己的系統OS下載對應的 [Anaconda](https://www.continuum.io/downloads)  版本，

基本上一直下一步無腦安裝即可順利安裝。

安裝完後，我們先來確認是否順利安裝，

使用cmd (命令提示字元) 輸入
> conda --version

如安裝成功，則會顯示安裝的版本 ( 如下圖 )

![alt tag](http://i.imgur.com/d9iXTL3.jpg)

## 使用 Anaconda 建立 Python 環境

先建立一個 python 3.5.2 的虛擬環境

使用 cmd (命令提示字元) 輸入

> conda create -n venv_demo python=3.5.2

![alt tag](http://i.imgur.com/CHVv9zf.jpg)

接著我們啟動這個虛擬環境，使用cmd (命令提示字元) 輸入
> activate venv_demo

或是

> source activate venv_demo

![alt tag](http://i.imgur.com/cR5wsM8.jpg)

再教大家一個很方便的指令，

查看目前所以的 envs

> conda info --envs

![alt tag](https://i.imgur.com/On8ljWU.png)

雖然也可以直接到資料夾去查看，但使用指令的方式更快更方便 :blush:

移除 env 指令

> conda remove --name myenv --all

或

> conda env remove --name myenv

上面兩個指令都可以移除 env，myenv 就是你的 env_name

## 如何安裝 OpenCV3

使用cmd (命令提示字元) 輸入
> conda install -c `https://conda.anaconda.org/menpo opencv3`

![alt tag](http://i.imgur.com/LgSeS2z.jpg)

最後確認是否成功安裝 opencv3，使用cmd (命令提示字元) 輸入

> python

```python
import cv2
cv2.__version__
```

如安裝成功，則會顯示安裝的版本 ( 如下圖 )

![alt tag](http://i.imgur.com/iZ6zdmM.jpg)

恭喜你~  安裝成功了

## Environment

* Windows 10
* Python 3.5.2
* OpenCV 3.1.0
