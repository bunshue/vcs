# kaggle 鐵達尼預測生亡

## kaggle 網址: https://www.kaggle.com/c/titanic

## Data : https://www.kaggle.com/c/titanic/data

## 執行過程 log

### 2020-12-14
1. 資料掛上去 colab=>train.csv  test.csv submisstion.csv.
2. load 資料
3. 資料欄位 : PassengerId	Survived	Pclass	Name	Sex	Age	SibSp	Parch	Ticket	Fare	Cabin	Embarked (其中 Survived 是要預測的label 值)
4. 清理資料+資料特徵工程
    - 觀察到PassengerId 好像沒有幫助=>先刪除
    - 劃出個欄位和生存比率的關係
    - 有幾個變項是類別變項先不用處理
    - 有些是連續變項先處理他們
        - 處理 Name 這個欄位 (Braund, Mr. Owen Harris)
        - 先用逗號分割成兩個部分(Braund 和 Mr. Owen Harris)
        - 因為觀察到後半部(Mr. Owen Harris)大多有Mr 、Miss 等幾種
        - 所以再把後半部用. 分割=>並將分割的新增一個欄位 title 給他放
        - 那原本的Name欄位就放 Braund
        - 把 title 通通列出來=>發現有17種
        - 觀察這些 title 又和性別可以牽扯關係=>因此又把他們和性別一起比對，最後濃縮成種:Mr、Mrs、rare
        - 
      
