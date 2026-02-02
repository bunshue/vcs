# ch1_18.py
import pygal.maps.world

worldMap = pygal.maps.world.World()         # 建立世界地圖物件
worldMap.title = 'China/Japan/Thailand'     # 世界地圖標題
worldMap.add('Asia',['cn', 'jp', 'th'])     # 標記Asia
worldMap.render_to_file('out1_18.svg')      # 儲存地圖檔案





