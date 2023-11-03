import pandas as pd
from sklearn import preprocessing, linear_model

titanic = pd.read_csv("titanic.csv")
print(titanic.info())
print("---------------------------")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([encoded_class, 
                  titanic["SexCode"]]).T
y = titanic["Survived"]

logistic = linear_model.LogisticRegression()
logistic.fit(X, y)
print("迴歸係數:", logistic.coef_)
print("截距:", logistic.intercept_ )
print("---------------------------")
preds = logistic.predict(X)
print(pd.crosstab(preds, titanic["Survived"]))
pd.crosstab(preds, titanic["Survived"]).to_html("ch15-4-2b.html")
print("---------------------------")
print((840+222)/(840+222+23+228))
print(logistic.score(X, y))
