# Learn-Tensorflow-Keras-Note
TensorFlow+Keras 深度學習人工智慧實務應用 書籍(作者:林大貴)學習筆記

![image](https://user-images.githubusercontent.com/55075639/100620861-e14da480-3359-11eb-9a5b-4bed09b3aa18.png)

# Code

- [Unit4 +Unit6 +Unit7 ](https://github.com/SweetornotspicyMarathon/Learn-Tensorflow-Keras-Note/blob/main/U4%2BU6%2BU7.ipynb) OK

  - Unit4 : 在colab 上使用 tensorflow 和 Keras
  
  - Unit5 : 在Linux 系統下安裝 jupyter notebook，因為暫時沒有用到先跳過
  
  - Unit6+Unit7 : 開始第一個練習，使用MNist 手寫數字資料庫，進行數字辨識
  
        1. 從匯入資料(查看資料型態)
        
        2. 資料前處理(資料 reshape 把他們壓扁、資料標準化 normalize、label 資料 one hot encodeing)
        
        3. 建立模型(這裡用多元感知器 Multilayer percertron ,MLP?)
        
         
          # 建立模型
          model = Sequential()

          # 建立輸入層和隱藏層
          model.add(Dense(units=256,input_dim=784,kernel_initializer='normal',activation='relu'))
          # 定義隱藏層神經元個數256
          # 輸入為28*28=784 個float 數字
          # 使用 normal distribution 常態分布的亂數，初始化 weight權重 bias 偏差
          # 定義激活函數為 relu


          # 建立輸出層
          model.add(Dense(units=10,kernel_initializer='normal',activation='softmax'))
          # 定義輸出層為10個 (數字0~9)
          # 也是使用常態分佈初始化
          # 定義激活函數是 softmax
          # 這裡建立的Dense 層，不用設定 input dim ，因為keras 會自動照上一層的256設定

          print(model.summary())
                  
         4. 模型compile訓練+紀錄訓練過程+訓練曲線視覺化(show train history)
         
         5. 測試(評估測試準確度、進行預測、計算正確率使用confusion table)
         
         7. 模型優化(方法有:增加神經元、加入 dropout 避免 oberfiting、增加隱藏層)
         
         8. 結論:多層感知器有其極限，提高準確度可以試試看 CNN

- [Unit8](https://github.com/SYkkk55/Learn-Tensorflow-Keras-Note/blob/main/U8.ipynb) 

- [Unit9+Unit10](https://github.com/SYkkk55/Learn-Tensorflow-Keras-Note/blob/main/U9%2BU10.ipynb) 

# Medium 
- [[Tesorflow Keras 學習筆記]新手一定要玩的MNIST手寫數字辨識](https://sweetornotspicymarathon.medium.com/tesorflow-keras-%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E6%96%B0%E6%89%8B%E4%B8%80%E5%AE%9A%E8%A6%81%E7%8E%A9%E7%9A%84mnist%E6%89%8B%E5%AF%AB%E6%95%B8%E5%AD%97%E8%BE%A8%E8%AD%98-9327366cc838) 
