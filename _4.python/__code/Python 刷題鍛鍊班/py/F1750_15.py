# F1750 練習 15

def record_rainfall():
    rainfall = {}
    while True:
        city_name = input('輸入城市: ')
        if not city_name:
            break
        rain_mm = input('輸入雨量 (mm): ')
        if not rain_mm:
            rain_mm = 0
 
        rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)
 
    for city, rain in rainfall.items():
        print(f'{city}: {rain} mm')

record_rainfall()
