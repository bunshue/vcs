# ch21_14.py
import pygal.maps.world

worldMap = pygal.maps.world.World()         # 建立世界地圖物件
worldMap.title = 'China in the Map'         # 世界地圖標題
worldMap.add('China',['cn'])                # 標記中國
worldMap.render_to_file('out21_14.svg')     # 儲存地圖檔案


