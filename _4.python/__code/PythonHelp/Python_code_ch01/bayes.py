import sys
import random
import numpy as np

import cv2

map_filename = 'cape_python.png'

SA1_CORNERS = (130, 265, 180, 315)  #(左上-X，左上-Y，右下-X，右下-Y)
SA2_CORNERS = (80, 255, 130, 305)
SA3_CORNERS = (105, 205, 155, 255)


class Search():
    """貝氏搜尋與具有 3 個搜尋區域的救援遊戲"""

    def __init__(self, name):
        self.name = name
        self.img = cv2.imread(map_filename, cv2.IMREAD_COLOR)
        if self.img is None:
            print('Could not load map file {}'.format(map_filename),
                  file=sys.stderr)
            sys.exit(1)
        print(self.img.shape)
        #建立 2 個屬性用來表示找到漁夫時的所在位置
        self.area_actual = 0
        self.sailor_actual = [0, 0]

        #由影像陣列建立搜尋區域的子陣列
        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3],
                            SA1_CORNERS[0] : SA1_CORNERS[2]]

        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3],
                            SA2_CORNERS[0] : SA2_CORNERS[2]]

        self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3], 
                            SA3_CORNERS[0] : SA3_CORNERS[2]]

        # 預設每個區域找到漁夫的機率值
        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        # 預設搜索效率
        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

    def draw_map(self, last_known):

        print(self.img.shape)
        cv2.rectangle(self.img, (2, 2),
                     (self.img.shape[1]-4, self.img.shape[0]-4), (0, 0, 255), 4)
        
        """顯示底層的地圖，以及比例尺、目前已知的最後 xy 位置、搜尋區域"""

        # 畫出並標示出搜索區域
        cv2.rectangle(self.img, (SA1_CORNERS[0], SA1_CORNERS[1]),
                     (SA1_CORNERS[2], SA1_CORNERS[3]), (0, 0, 255), 1)
        cv2.putText(self.img, '1 R',
                   (SA1_CORNERS[0] + 3, SA1_CORNERS[1] + 15),
                   cv2.FONT_HERSHEY_PLAIN, 1, 0)

        cv2.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]),
                     (SA2_CORNERS[2], SA2_CORNERS[3]), (0, 255, 0), 1)
        cv2.putText(self.img, '2 G',
                   (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15),
                   cv2.FONT_HERSHEY_PLAIN, 1, 0)

        cv2.rectangle(self.img, (SA3_CORNERS[0], SA3_CORNERS[1]),
                     (SA3_CORNERS[2], SA3_CORNERS[3]), (255, 0, 0), 1)
        cv2.putText(self.img, '3 B',
                   (SA3_CORNERS[0] + 3, SA3_CORNERS[1] + 15),
                   cv2.FONT_HERSHEY_PLAIN, 1, 0)

        # 顯示視窗
        cv2.imshow('Search Area', self.img)

        print('移動視窗位置')
        #cv2.moveWindow('Search Area', 750, 10)
        cv2.moveWindow('Search Area', 0, 0)

        print('5秒鐘後 關閉視窗')
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

    
       
app = Search('Cape_Python')
app.draw_map(last_known=(160, 290))
#app.draw_map(last_known=(200, 200))

print("P1 = {:.3f}, P2 = {:.3f}, P3 = {:.3f}".format(app.p1, app.p2, app.p3))
print("P1 = {:.3f}, P2 = {:.3f}, P3 = {:.3f}".format(app.sep1, app.sep2, app.sep3))

