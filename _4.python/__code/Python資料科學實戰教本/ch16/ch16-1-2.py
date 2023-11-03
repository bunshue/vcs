import pandas as pd
from sklearn import preprocessing, tree
from sklearn.model_selection import train_test_split

titanic = pd.read_csv("titanic.csv")
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic["PClass"])

X = pd.DataFrame([titanic["SexCode"],
                  encoded_class]).T
X.columns = ["SexCode", "PClass"]
y = titanic["Survived"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25,
                                                random_state=1)

dtree = tree.DecisionTreeClassifier()
dtree.fit(XTrain, yTrain)

print("準確率:", dtree.score(XTest, yTest))
print("---------------------------")
preds = dtree.predict_proba(X=XTest)
print(pd.crosstab(preds[:,0], columns=[XTest["PClass"],
                                       XTest["SexCode"]]))
pd.crosstab(preds[:,0], columns=[XTest["PClass"],
                                       XTest["SexCode"]]).to_html("ch16-1-2.html")
