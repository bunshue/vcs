# ch1_20.py
import pygal.maps.world

worldMap = pygal.maps.world.World()                     # 建立世界地圖物件
worldMap.title = 'Populations in China/Japan/Thailand'  # 世界地圖標題
worldMap.add('Asia',{'cn':1262645000,
                     'jp':126870000,
                     'th':63155029})                    # 標記人口資訊
worldMap.render_to_file('out1_20.svg')                  # 儲存地圖檔案


