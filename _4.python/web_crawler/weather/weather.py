import requests

# openweathermap_key.txt

API_KEY = "xxxx"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = "Hsinchu"
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("天氣 :", weather)
    print("溫度 :", temperature, " 度C")

    print("main :", data['weather'][0]['main'])
    print("main :", data['weather'][0]['description'])
    print("temp :", data['main']['temp'])
    print("feels_like :", data['main']['feels_like'])
    print("min :", data['main']['temp_min'])
    print("max :", data['main']['temp_max'])
    print("pressure :", data['main']['pressure'])
    print("humidity :", data['main']['humidity'])
    print("max :", data['main']['temp_max'])
    print("max :", data['main']['temp_max'])

else:
    print("找不到無資料")

