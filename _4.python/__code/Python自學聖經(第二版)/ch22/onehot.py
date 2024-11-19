from sklearn.feature_extraction import DictVectorizer

dict = DictVectorizer(sparse=False)
data = dict.fit_transform([{'膚色':'黃','身高':176}, 
                           {'膚色':'白','身高':183}, 
                           {'膚色':'黑','身高':158}])
print('one-hot編碼：')
print(data)
print('特徵名稱：')
print(dict.get_feature_names_out())
