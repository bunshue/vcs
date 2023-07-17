from sklearn.feature_extraction.text import TfidfVectorizer
import jieba

t1 = list(jieba.cut('今天台北天氣晴朗，風景區擠滿了人潮。'))
t2 = list(jieba.cut('台北的天氣常常下雨。'))
c1 = ' '.join(t1)
c2 = ' '.join(t2)

tf = TfidfVectorizer()
data = tf.fit_transform([c1, c2])
print('one-hot編碼：')
print(data.toarray())
print('特徵名稱：')
print(tf.get_feature_names())