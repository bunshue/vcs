from sklearn.datasets import fetch_20newsgroups

news = fetch_20newsgroups(data_home="data", subset="all")
print("目標值：")
print(news.target)
print("目標名稱：")
print(news.target_names)
print("第一篇新聞內容：")
print(news.data[0])
