import requests
url = 'https://cdn.heweather.com/china-city-list.txt'
response = requests.get(url)
response.encoding='utf8'
data = response.text
data_1 = data.split('\r')
print(data_1)
for i in range(3):
    data_1.remove(data_1[0])
for item in data_1:
    print(item[0:11])