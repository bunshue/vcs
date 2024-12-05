print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing


def show():
    return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

"""
#【資料分析】python資料處理-類別欄位轉換基礎操作語法彙整

#在進行資料分析時，有時需要將類別欄位轉換為數值欄位，以便進行數值計算和機器學習模型訓練等操作。
由於模型是基於數學模型設計的方法，必須要輸入資料將類別欄位轉換為數值欄位模型才能讀得懂。
例如，某個欄位的取值為「男」和「女」，可以將其轉換為數值欄位，例如「0」表示男性，「1」表示女性。
這樣可以讓機器學習模型更容易理解和處理資料。

方法選擇重點
Label Encoding 適用於有順序的類別數據且類別數量較少的數據
One-Hot Encoding 適用於無順序且類別數量較少的數據
Binary Encoding 適用於無順序且類別數量較多的數據
Target Encoding 適用於回歸問題，類別變量與目標變量有較強的相關性
Frequency Encoding 適用於類別數量較多且類別出現的頻率與目標變量相關性較弱的數據

Labelencoding (標籤編碼)
基本概念
Label Encoding 是一種將類別變量轉換為數值變量的技術。
具體來說，標籤編碼將每個類別值映射到一個唯一的整數。
例如，如果有三個類別值 "red"、"green" 和 "blue"，標籤編碼可能會將它們分別映射為 0、1 和 2。
"""

data = {"size": ["small", "medium", "large", "medium", "small"]}
df = pd.DataFrame(data)

# 初始化標籤編碼器
le = preprocessing.LabelEncoder()

# 將 'size' 欄位進行標籤編碼
df["size_encoded"] = le.fit_transform(df["size"])
print(df)

"""
     size  size_encoded
0   small             2
1  medium             1
2   large             0
3  medium             1
4   small             2
"""

"""
※ Label Encoding 並沒有內建的機制來識別或維持類別的順序。
標籤編碼器會按照字母順序（alphabetical order）或數字順序來分配標籤。
因此，在處理有序類別數據時，需要確保在編碼之前已經按照正確的順序來指定標籤。
"""

# 創建一個範例數據集
data = {"size": ["small", "medium", "large", "medium", "small"]}
df = pd.DataFrame(data)

# 指定有序類別的順序
size_mapping = {"small": 0, "medium": 1, "large": 2}

# 使用映射進行編碼
df["size_encoded"] = df["size"].map(size_mapping)
print(df)

"""
     size  size_encoded
0   small             0
1  medium             1
2   large             2
3  medium             1
4   small             0
"""

"""

優點與缺點

優點

簡單易用：實現和理解都非常簡單。
對有序類別有效：如果類別值具有自然的順序，標籤編碼能夠很好地表達這一順序。
缺點

引入虛假順序關係：對於無序的類別數據，標籤編碼引入的整數表示可能會使模型誤解不同類別之間存在順序關係。
對一些模型不友好：某些模型（例如線性回歸）可能會受到這種虛假順序關係的影響。


適用場景
有序類別數據：當類別數據有自然順序（例如 "低"、"中"、"高"）時，標籤編碼是很好的選擇。
小型數據集：標籤編碼在類別數量較少的情況下非常有效。
"""

"""

One-Hot Encoding (獨熱編碼)
基本概念
One-Hot Encoding 是將分類數據轉換為二進位變量的過程。對於每個類別變量，會創建一個新的二進位變量。
每個變量都表示是否存在某個特定的類別。這意味著，對於每一個觀測值，僅有一個二進位變量為1，其餘為0。

"""

# 創建一個範例數據集
data = {"color": ["red", "blue", "green", "blue", "red"]}
df = pd.DataFrame(data)

# 使用pd.get_dummies() 進行One-Hot Encoding
df_one_hot = pd.get_dummies(df, columns=["color"])
print(df_one_hot)

"""
   color_blue  color_green  color_red
0           0            0          1
1           1            0          0
2           0            1          0
3           1            0          0
4           0            0          1
"""

# 創建範例數據集
data = {
    "color": ["red", "blue", "green", "blue", "red"],
    "city": ["New York", "Paris", "London", "Berlin", "Paris"],
}
df = pd.DataFrame(data)

# 使用pd.get_dummies進行One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=["color", "city"])

print(df_encoded)

"""
   color_blue  color_green  color_red  city_Berlin  city_London  city_New York  city_Paris
0           0            0          1            0            0              1           0
1           1            0          0            0            0              0           1
2           0            1          0            0            1              0           0
3           1            0          0            1            0              0           0
4           0            0          1            0            0              0           1
"""

"""
優點與缺點

優點：

不引入順序關係：One-Hot Encoding 不會引入類別之間的順序，因此非常適合無序類別數據。
避免虛假關聯：能夠避免因數值關聯而產生的虛假關聯，適合用於大部分機器學習算法。
缺點：

維度爆炸：如果類別數據的類別數量很多，One-Hot Encoding 會導致數據集的維度劇增，這對內存和計算資源有較大需求。
非稀疏數據處理困難：部分機器學習算法在處理高維稀疏矩陣時效率較低。

適用場景
無序類別數據：適合用於沒有順序關係的類別數據，如顏色、城市等。
機器學習算法：在很多機器學習算法中，如決策樹、隨機森林、神經網絡中，One-Hot Encoding 是處理類別數據的常見方法。
避免引入虛假關聯：在數據分析和預測中，避免數值關聯導致的錯誤解釋和結果。
"""

"""
Binary Encoding (二值編碼)
基本概念
Binary Encoding 是將類別數據轉換為二進位數據的一種方法。
它先將類別轉換為數值，然後再將這些數值轉換為二進位碼。
每個類別用二進位碼表示，並將每個二進位碼的位數拆分成不同的列。
"""
# pip install --upgrade category_encoders
import category_encoders as ce

# 創建範例數據集
data = {
    "product_id": ["A123", "B234", "C345", "A123", "B234"],
    "customer_id": ["C1", "C2", "C3", "C4", "C5"],
}
df = pd.DataFrame(data)

# 使用 Binary Encoder 進行二進位編碼
encoder = ce.BinaryEncoder(cols=["product_id", "customer_id"])
df_encoded = encoder.fit_transform(df)
print(df_encoded)

"""
   product_id_0  product_id_1  product_id_2  customer_id_0  customer_id_1  customer_id_2
0             1             0             0              1              0              0
1             0             1             0              0              1              0
2             1             1             0              1              1              0
3             1             0             0              0              0              1
4             0             1             0              0              1              1
"""

"""
優點與缺點

優點：

減少維度：相比 One-Hot Encoding，Binary Encoding 可以有效地減少高基數類別的特徵維度。
保留部分順序信息：適度保留了類別之間的順序信息，有助於某些需要順序信息的模型。
缺點：

可解釋性較低：相比 One-Hot Encoding，Binary Encoding 生成的特徵對於人類而言不太直觀和易解釋。
引入少量順序信息：對於無序類別數據，引入的順序信息可能在某些情況下不利於模型表現。

適用場景
高基數類別數據：適用於類別數量很多的情況，如產品ID、用戶ID等。
需要減少維度的情況：適用於在減少維度的同時保留部分數據信息的情況。
機器學習算法：適用於大多數機器學習算法，特別是那些對維度敏感但對數值變量有良好支持的算法。
在需要保留部分順序信息但又不希望完全轉化為數值變量的情況下。
"""

"""
Target Encoding (目標編碼)
基本概念
Target Encoding 是一種將類別變量轉換為數值變量的方法。
其基本思想是用目標變量的平均值（或其他統計量）來替換類別變量的值。
這通常是通過計算每個類別的目標變量的平均值來完成的。
"""

import category_encoders as ce

# 創建一個範例數據集
data = pd.DataFrame(
    {
        "city": [
            "New York",
            "Los Angeles",
            "New York",
            "Chicago",
            "Los Angeles",
            "Chicago",
            "New York",
            "Chicago",
        ],
        "house_type": [
            "Apartment",
            "House",
            "House",
            "Apartment",
            "House",
            "House",
            "Apartment",
            "Apartment",
        ],
        "price": [500000, 450000, 600000, 350000, 400000, 300000, 700000, 250000],
    }
)

# 使用 Target Encoder 進行目標編碼
encoder = ce.TargetEncoder(cols=["city", "house_type"])
data_encoded = encoder.fit_transform(data[["city", "house_type"]], data["price"])

# 合併編碼後的數據
data_encoded["price"] = data["price"]
print(data_encoded)

"""
            city     house_type   price
0  467885.197669  444799.885093  500000
1  441090.292533  442700.114907  450000
2  467885.197669  442700.114907  600000
3  421545.618144  444799.885093  350000
4  441090.292533  442700.114907  400000
5  421545.618144  442700.114907  300000
6  467885.197669  444799.885093  700000
7  421545.618144  444799.885093  250000
"""

"""
city 和 house_type 這兩個類別型欄位被轉換成了數值型欄位，這些數值是根據 price 的平均值計算出來的。
這樣做的好處是，可以將類別型資料轉換成數值型資料，以便在機器學習模型中使用。
"""

"""
優點與缺點

優點：

捕捉目標信息：它利用了目標變量的信息，能夠提高模型的預測能力。
減少維度：相比 One-Hot Encoding，Target Encoding 不會增加數據集的維度，這對於高基數類別變量尤為重要。
適用於高基數變量：特別適合於高基數類別變量，避免了稀疏矩陣的問題。
缺點：

過擬合風險：由於使用了目標變量的信息，可能導致模型過擬合，尤其是在訓練數據中某些類別出現頻率較低時。
數據泄露：需要謹慎處理，避免數據泄露，應該在交叉驗證的過程中進行編碼。

適用場景
高基數類別變量：特別適合於類別數量很多的情況，如用戶ID、產品ID等，根據用戶ID或產品ID來預測用戶的行為或產品的受歡迎程度。
預測任務：適合於回歸和分類預測任務，能夠利用目標變量的信息提高模型性能。
樹模型：在樹模型（如隨機森林、梯度提升樹）中，Target Encoding 通常比 One-Hot Encoding 更有效。
在廣告點擊率預測中，根據廣告ID來預測點擊率。
在銷售預測中，根據產品類別來預測銷售額。
"""

"""
Frequency Encoding (頻率編碼)
基本概念
Frequency Encoding 是一種將類別型資料轉換為數值型資料的編碼方法。這種方法基於每個類別出現的頻率，
即每個類別在資料集中出現的次數。具體來說，頻率編碼會將每個類別替換為該類別在資料集中出現的次數。
"""

# 創建一個範例數據集
data = pd.DataFrame(
    {
        "user_id": [
            "user_1",
            "user_2",
            "user_3",
            "user_1",
            "user_4",
            "user_2",
            "user_3",
            "user_1",
        ],
        "visit_count": [10, 15, 10, 20, 5, 25, 10, 30],
    }
)

# 計算每個用戶ID出現的頻率
frequency_encoding = data["user_id"].value_counts(normalize=True)

# 將頻率映射回原數據集
data["user_id_freq"] = data["user_id"].map(frequency_encoding)
print(data)

"""
   user_id  visit_count  user_id_freq
0   user_1           10          0.375
1   user_2           15          0.250
2   user_3           10          0.250
3   user_1           20          0.375
4   user_4            5          0.125
5   user_2           25          0.250
6   user_3           10          0.250
7   user_1           30          0.375
"""

"""
在這個範例中，用戶ID被轉換為其在數據集中出現的頻率。這些頻率可以用來分析不同用戶群體的訪問頻率。例如，頻繁訪問網站的用戶可能是忠實用戶，可以針對這些用戶進行特別的營銷活動。
機器學習模型：在構建機器學習模型時，可以使用用戶ID的頻率作為特徵，這些頻率可以幫助模型更好地理解用戶行為模式。
網站優化：頻率編碼後的數據可以幫助了解哪些用戶群體更活躍，從而幫助網站管理者優化網站內容和結構，提升用戶體驗。

優點與缺點

優點：

簡單直觀，易於實現。
對於類別數據具有明顯的頻率特徵時，效果不錯。
缺點：

當類別分佈不均衡時，可能會引入偏差。
不適用於所有情況，特別是類別型資料與目標變量之間沒有明顯關聯時。

適用場景
缺少標籤數據：當標籤數據不足時，Frequency Encoding 不依賴於目標變量，可以在僅有特徵數據的情況下使用。
初步數據探索：在初步數據探索中，可以快速獲取每個類別的頻率，幫助理解數據分佈情況。
簡單模型：在構建簡單模型時，使用 Frequency Encoding 可以降低模型的複雜性，而不需要考慮目標變量的影響。
在構建電子商務推薦系統時，可以通過產品類別的頻率來優化推薦策略。頻繁出現的產品類別可能是熱門類別，可以優先推薦給用戶。
在客戶細分時，可以通過用戶行為類別的頻率來進行細分。例如，可以根據用戶購買頻率將用戶分為高頻購買者和低頻購買者，從而制定不同的營銷策略。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 機器學習算法處理缺失值
# 機器學習算法可以用於填充 Missing Value，例如 K-Nearest Neighbor（KNN）算法。
# KNN 算法可以根據與缺失值最接近的 k 個樣本的值來填充缺失值。

from sklearn.impute import KNNImputer

data = pd.DataFrame(
    {"col1": [5, 12, 8, np.nan], "col2": [16, 9, np.nan, 4], "col3": [11, 3, 7, 20]}
)

# 使用 KNN 算法填充缺失值
imputer = KNNImputer(n_neighbors=2)
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

"""
KNN 算法基本概念
KNN 算法的基本原理是基於相似性假設，即相似樣本具有相似的特徵或標籤。
因此，KNN 算法在處理缺失值時，會利用數據集中與缺失值樣本最相似的 K 個樣本來進行填補。

KNN 算法會給定一個數據點，找到與其最接近的 K 個數據點，並使用這些鄰近數據點的信息來進行分類或回歸，
實際應用在缺失值填補時，具體步驟如下：

標準化數據：由於不同特徵的取值範圍可能不同，標準化數據可以確保距離計算的合理性。
計算距離：對於包含缺失值的樣本，計算其與其他樣本的距離。只考慮非缺失值特徵。
選擇 K 個最近鄰居：根據計算出的距離，選擇 K 個與缺失樣本最接近的鄰居。
填補缺失值：對於數值型特徵，使用 K 個鄰居的平均值或中位數填補缺失值；
對於類別型特徵，使用 K 個鄰居中最常見的類別填補缺失值。
"""

print("------------------------------------------------------------")  # 60個

"""
基礎 KNN 應用範例

整體流程：

對於每一個缺失值樣本，找到最接近的 2 個樣本（即距離最近的鄰居）。
使用這些鄰居的值來填補缺失值，這樣使得填補後的數據保留了原數據的局部相似性。
將填補後的數據轉換為 pandas DataFrame 格式，並保留原數據框的列名。

"""

from sklearn.impute import KNNImputer

data = pd.DataFrame(
    {"col1": [5, 12, 8, np.nan], "col2": [16, 9, np.nan, 4], "col3": [11, 3, 7, 20]}
)

# 使用 KNN 算法填充缺失值
imputer = KNNImputer(n_neighbors=2)
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

print("------------------------------------------------------------")  # 60個

"""
KNNImputer是 scikit-learn 中用於缺失值插補的類。
n_neighbors=2 指定了 KNN 算法中使用的鄰居數量為 2。
也就是說，對於每個缺失值，KNN 算法會找到與之最相似的 2 個鄰居，並使用這些鄰居的值來填補缺失值。
imputer.fit_transform(data)：這個方法對數據 data 進行填充。
fit_transform 是 scikit-learn 中的常用方法，它會先擬合（fit）模型然後轉換（transform）數據。
對於 KNNImputer，這意味著它會計算所有非缺失值之間的距離，然後對每個缺失值進行填補。
pd.DataFrame(imputer.fit_transform(data),columns=data.columns)：將填充後的數據轉換為 pandas 的 DataFrame 格式，並保留原數據框的列名。
imputer.fit_transform(data) 返回的是一個 NumPy 的數組，我們將其轉換為 DataFrame 並設置列名為 data.columns 以保持與原數據框一致的結構。
"""

print("------------------------------------------------------------")  # 60個

"""
KNN 算法的優點和缺點

優點
考慮了數據的局部相似性：
KNN 算法利用相似的樣本來填補缺失值，因此能夠保留數據的局部模式和結構，這比簡單地使用平均值或中位數更能反映實際情況。
適用於多種數據類型：
KNN 可以應用於連續數據和分類數據，適應性較強。
不需要對數據進行嚴格假設：
KNN 算法是一種非參數方法，不需要對數據的分佈進行假設，這使得它在處理各種類型的數據時更加靈活。
有效利用數據中的信息：
KNN 算法能充分利用數據中現有的樣本信息進行填補，從而可能提高模型的預測準確性。


缺點
計算量大：
對於大型數據集，KNN 的計算開銷會非常大，因為需要計算每個樣本與其他樣本之間的距離。
這會導致填補缺失值的過程非常耗時。
受數據稀疏性的影響：
如果數據中缺失值較多，找到足夠的鄰居來填補缺失值會變得困難，這會影響填補的效果。
對異常值敏感：
KNN 算法會受到異常值（outliers）的影響，因為異常值會影響鄰居的選擇，從而導致填補結果不準確。
需要選擇適當的 k 值：
k 值（即鄰居數量）的選擇對填補結果有較大影響。如果 k 值過小，填補結果可能過於依賴單個鄰居；
如果 k 值過大，填補結果可能過於平滑，無法反映數據的真實結構。
資料標準化的需求：
在使用 KNN 算法之前，通常需要對數據進行標準化（Normalization），
以確保不同特徵之間的距離具有可比性。這增加了數據預處理的複雜性。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "data/labelencoder_data.csv"
df = pd.read_csv(filename)
print(df)

label_encoder = preprocessing.LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 載入資料集
# 鐵達尼號資料集是一個CSV檔案：titanic_data.csv，我們可以建立DataFrame物件來載入資料集

"""
資料前處理

在檢視資料集的描述資料後，我們知道目前需要處理的工作，如下所示：

PassengerId欄位是否是流水號，如果是，我們可以將此欄位改為索引欄位。
Sex欄位需要處理分類資料轉換成數值的0和1（1是女；0是男）。
PClass欄位需要處理分類資料轉換成數值的1、2和3（1是1st；2是2nd；3是3rd）。
Age欄位有很多遺漏值，我們準備使用Age欄位的平均值來補值。
"""
filename = "data/titanic_data.csv"
titanic = pd.read_csv(filename)

print("資料shape")
print(titanic.shape)

print("size")
print(np.unique(titanic["PassengerId"].values).size)

titanic.set_index(["PassengerId"], inplace=True)
print(titanic.head())

titanic["SexCode"] = np.where(titanic["Sex"] == "female", 1, 0)
print(titanic.head())

print("------------------------------")  # 30個

label_encoder = preprocessing.LabelEncoder()
titanic["PClass"] = label_encoder.fit_transform(titanic["PClass"])
print(titanic)

print("isnull().sum()")
print(titanic.isnull().sum())

print("age.isnull()")
print(sum(titanic["Age"].isnull()))

avg_age = titanic["Age"].mean()
print("average age =", avg_age)

titanic["Age"].fillna(avg_age, inplace=True)
print(sum(titanic["Age"].isnull()))

print("1111")
print(titanic["Sex"].groupby(titanic["Sex"]).size())

print("2222")
print(titanic.groupby("Sex")["Age"].mean())

print("------------------------------")  # 30個

# 探索性資料分析

print("3333")
titanic["Died"] = np.where(titanic["Survived"] == 0, 1, 0)
print(titanic)

titanic["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 0]
df["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 1]
df["Age"].plot(kind="hist", bins=15)

show()

print("------------------------------")  # 30個

fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).sum()
df.plot(kind="bar", ax=axes[0])

df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).mean()
df.plot(kind="bar", ax=axes[1])

show()

print("------------------------------")  # 30個

df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).sum()
df.plot(kind="bar")

show()

print("------------------------------")  # 30個

df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).mean()
df.plot(kind="bar")

show()

print("------------------------------")  # 30個
"""
df = titanic.drop("Died", axis=1)
print("係數矩陣 :", df.corr())

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
