# ch21_16.py
import pygal.maps.world

worldMap = pygal.maps.world.World()                         # 建立世界地圖物件
worldMap.title = ' Asia, Europe, Africa, and North America' # 世界地圖標題
worldMap.add('Asia',['cn', 'jp', 'th'])                     # 標記Asia
worldMap.add('Europe',['fr', 'de', 'it'])                   # 標記Europe
worldMap.add('Africa',['eg', 'ug', 'ng'])                   # 標記Africa
worldMap.add('North America',['ca', 'us', 'mx'])            # 標記北美洲
worldMap.render_to_file('out21_16.svg')                     # 儲存地圖檔案


