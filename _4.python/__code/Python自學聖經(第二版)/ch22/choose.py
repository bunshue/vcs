from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold

mm = MinMaxScaler()
data = mm.fit_transform([[3,2,61,10000], 
                         [3,8,54,12000], 
                         [3,4,60,10500], 
                         [3,1,58,11000]])
print('原始特徵：')
print(data)
vari = VarianceThreshold(threshold=0.0)
#vari = VarianceThreshold(threshold=0.14)
data2 = vari.fit_transform(data)
print('特徵選擇後：')
print(data2)