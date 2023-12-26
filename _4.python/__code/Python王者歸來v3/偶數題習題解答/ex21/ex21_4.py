# ex21_4.py
import pygal.maps.world

worldMap = pygal.maps.world.World()                     # 建立世界地圖物件
worldMap.title = 'Populations in China/Japan/Thailand'  # 世界地圖標題
worldMap.add('Asia',{'cn':1262645000,
                     'jp':126870000,
                     'th':63155029})                    # 標記人口資訊
worldMap.add('Europe',{'fr':60762406,
                     'se':1011781,
                     'sz':7184798})                    # 標記人口資訊
worldMap.add('Africa',{'cd':49626496,
                     'eg':67649043,
                     'za':44000833})                    # 標記人口資訊
worldMap.add('North America',{'us':282162848,
                     'mx':99959895,
                     'ca':30770661})                    # 標記人口資訊
worldMap.render_to_file('out21_4.svg')                 # 儲存地圖檔案


