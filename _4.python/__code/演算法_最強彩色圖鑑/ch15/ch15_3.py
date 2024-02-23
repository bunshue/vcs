# ch15_3.py                 
def greedy(radios, cities):
    ''' 貪婪演算法 '''
    greedy_radios = set()                           # 最終電台的選擇
    while cities:                                   # 還有城市沒有覆蓋迴圈繼續
        greedy_choose = None                        # 最初化選擇
        city_cover = set()                          # 暫存
        for radio, area in radios.items():          # 檢查每一個電台
            cover = cities & area                   # 選擇可以覆蓋城市
            if len(cover) > len(city_cover):        # 如果可以覆蓋更多則取代
                greedy_choose = radio               # 目前所選電台
                city_cover = cover
        cities -= city_cover                        # 將被覆蓋城市從集合刪除
        greedy_radios.add(greedy_choose)            # 將所選電台加入
    return greedy_radios                            # 傳回電台

cities = set(['台北', '基隆', '桃園', '新竹',       # 期待廣播覆蓋區域
              '台中', '嘉義', '台南', '高雄']
            )

radios = {}
radios['電台 1'] = set(['新竹', '台中', '嘉義'])
radios['電台 2'] = set(['基隆', '新竹', '台北'])
radios['電台 3'] = set(['桃園', '台中', '台南'])
radios['電台 4'] = set(['台中', '嘉義'])
radios['電台 5'] = set(['台南', '高雄'])

print(greedy(radios, cities))                       # 電台, 城市


   















