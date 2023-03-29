import requests
from bs4 import BeautifulSoup
url = 'https://newcar.u-car.com.tw/newcar'
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
models = soup.select('#modelselect > option')
cars = list()
for model in models:
    if model['value'] != '0':
        car = dict()
        car['id'] = int(model['value'])
        car['make'] = int(model['data-make'])
        car['name'] = model.text
        cars.append(car)
print(cars)