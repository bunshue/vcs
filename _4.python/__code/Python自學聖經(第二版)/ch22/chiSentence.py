from sklearn.feature_extraction.text import CountVectorizer
import jieba

t1 = list(jieba.cut('今天台北天氣晴朗，風景區擠滿了人潮。'))
t2 = list(jieba.cut('台北的天氣常常下雨。'))
c1 = ' '.join(t1)
print('第一句分詞： {}'.format(c1))
c2 = ' '.join(t2)
print('第二句分詞： {}'.format(c2))

cv = CountVectorizer()
data = cv.fit_transform([c1, c2])
print('one-hot編碼：')
print(data.toarray())
print('特徵名稱：')
print(cv.get_feature_names())