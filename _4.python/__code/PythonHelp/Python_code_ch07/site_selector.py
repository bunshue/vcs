import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2 as cv

# 使用者輸入的常數:
IMG_GRAY = cv.imread('mola_1024x501.png', cv.IMREAD_GRAYSCALE)
IMG_COLOR = cv.imread('mola_color_1024x506.png')
RECT_WIDTH_KM = 670  # 設定矩形寬度尺寸
RECT_HT_KM = 335  # 設定矩形高度尺寸
MAX_ELEV_LIMIT = 55  # 設定地形高度最大值
NUM_CANDIDATES = 20  # 設定矩形區域數量
MARS_CIRCUM = 21344  # 設定火星的周長

#------------------------------------------------------------------------------

# 衍生常數:
IMG_HT, IMG_WIDTH = IMG_GRAY.shape
PIXELS_PER_KM = IMG_WIDTH / MARS_CIRCUM
RECT_WIDTH = int(PIXELS_PER_KM * RECT_WIDTH_KM)
RECT_HT = int(PIXELS_PER_KM * RECT_HT_KM)
LAT_30_N = int(IMG_HT / 3)
LAT_30_S = LAT_30_N * 2
STEP_X = int(RECT_WIDTH / 2)
STEP_Y = int(RECT_HT / 2)

screen = tk.Tk()
canvas = tk.Canvas(screen, width=IMG_WIDTH, height=IMG_HT + 130)


class Search():
    """讀取影像並依輸入的條件找出矩形著陸區"""
    def __init__(self, name):
        self.name = name
        self.rect_coords = {}
        self.rect_means = {}
        self.rect_ptps = {}
        self.rect_stds = {}
        self.ptp_filtered = []
        self.std_filtered = []
        self.high_graded_rects = []
        
    def run_rect_stats(self):
        """定義矩形搜尋區域並計算各區的相關數據"""
        ul_x, ul_y = 0, LAT_30_N 
        lr_x, lr_y = RECT_WIDTH, LAT_30_N + RECT_HT
        rect_num = 1
     
        while True:
            rect_img = IMG_GRAY[ul_y : lr_y, ul_x : lr_x]
            self.rect_coords[rect_num] = [ul_x, ul_y, lr_x, lr_y]
            if np.mean(rect_img) <= MAX_ELEV_LIMIT:
                self.rect_means[rect_num] = np.mean(rect_img)
                self.rect_ptps[rect_num] = np.ptp(rect_img)
                self.rect_stds[rect_num] = np.std(rect_img)
            rect_num += 1
            ul_x += STEP_X
            lr_x = ul_x + RECT_WIDTH
            if lr_x > IMG_WIDTH:
                ul_x = 0
                ul_y += STEP_Y
                lr_x = RECT_WIDTH
                lr_y += STEP_Y
            if lr_y > LAT_30_S + STEP_Y:
                break

    def draw_qc_rects(self):
        """在影像上畫出重疊的矩形以供檢查"""
        img_copy = IMG_GRAY.copy()
        rects_sorted = sorted(self.rect_coords.items(), key=lambda x: x[0])
        print("\nRect Number and Corner Coordinates (ul_x, ul_y, lr_x,\
        lr_y):")
        for k, v in rects_sorted:
            print("rect: {}, coords: {}".format(k, v))
            cv.rectangle(img_copy,
                         (self.rect_coords[k][0], self.rect_coords[k][1]),
                         (self.rect_coords[k][2], self.rect_coords[k][3]),
                         (255, 0, 0), 1)
        cv.imshow('QC Rects {}'.format(self.name), img_copy)
        cv.waitKey(3000)
        cv.destroyAllWindows()    

    def sort_stats(self):  
        """依字典值將字典排序，並用前幾名的鍵建立 list"""
        ptp_sorted = (sorted(self.rect_ptps.items(), key=lambda x: x[1]))
        self.ptp_filtered = [x[0] for x in ptp_sorted[:NUM_CANDIDATES]]
        std_sorted = (sorted(self.rect_stds.items(), key=lambda x: x[1]))
        self.std_filtered = [x[0] for x in std_sorted[:NUM_CANDIDATES]]
        
        # 取得兩個 list 的共同數字編號
        for rect in self.std_filtered:
            if rect in self.ptp_filtered:
                self.high_graded_rects.append(rect)   

    def draw_filtered_rects(self, image, filtered_rect_list):
        """在影像上畫出在 list 中的矩形並傳回影像"""
        img_copy = image.copy()
        for k in filtered_rect_list: 
            cv.rectangle(img_copy,
                         (self.rect_coords[k][0], self.rect_coords[k][1]),
                         (self.rect_coords[k][2], self.rect_coords[k][3]),
                         (255, 0, 0), 1)
            cv.putText(img_copy, str(k),
                       (self.rect_coords[k][0] + 1, self.rect_coords[k][3]- 1),
                       cv.FONT_HERSHEY_PLAIN, 0.65, (255, 0, 0), 1)
            
        # 畫出緯度線並標示文字
        cv.putText(img_copy, '30 N', (10, LAT_30_N - 7),
                   cv.FONT_HERSHEY_PLAIN, 1, 255)
        cv.line(img_copy, (0, LAT_30_N), (IMG_WIDTH, LAT_30_N),
                (255, 0, 0), 1)
        cv.line(img_copy, (0, LAT_30_S), (IMG_WIDTH, LAT_30_S),
                (255, 0, 0), 1)
        cv.putText(img_copy, '30 S', (10, LAT_30_S + 16),
                   cv.FONT_HERSHEY_PLAIN, 1, 255)

        return img_copy

    def make_final_display(self):
        """用 Tk 顯示含候選區域的地圖並輸出其統計資訊"""
        screen.title('Sites by MOLA Gray STD & PTP {} Rect'.format(self.name))
        # 畫出有標上候選矩形區域和緯度線的彩色影像        
        img_color_rects = self.draw_filtered_rects(IMG_COLOR,
                                                   self.high_graded_rects)
        # 轉換影像顏色格式 (BGR->RGG)
        img_converted = cv.cvtColor(img_color_rects,
                                    cv.COLOR_BGR2RGB)
        img_converted = ImageTk.PhotoImage(Image.fromarray
                                           (img_converted))    
        canvas.create_image(0, 0, image=img_converted, anchor=tk.NW)
        
        txt_x = 5
        txt_y = IMG_HT + 20
        for k in self.high_graded_rects:
            # 將文字放到畫布上
            canvas.create_text(txt_x, txt_y, anchor='w', font=None,
                               text="rect={}\
  mean elev={:.1f}  std={:.2f}  ptp={}"
                               .format(k, self.rect_means[k], self.rect_stds[k],
                                       self.rect_ptps[k]))
            txt_y += 15
            if txt_y >= int(canvas.cget('height')) - 10:
                txt_x += 300
                txt_y = IMG_HT + 20                
        canvas.pack()
        screen.mainloop()

        
def main():
    app = Search('670x335 km')
    app.run_rect_stats()
    app.draw_qc_rects()
    app.sort_stats()
    ptp_img = app.draw_filtered_rects(IMG_GRAY, app.ptp_filtered)
    std_img = app.draw_filtered_rects(IMG_GRAY, app.std_filtered)

    # 顯示含有峰-谷值最佳候選矩形區域的影像
    cv.imshow('Sorted by ptp for {} rect'.format(app.name), ptp_img)
    cv.waitKey(3000)
    # 顯示含有標準差最佳候選矩形區域的影像
    cv.imshow('Sorted by std for {} rect'.format(app.name), std_img)
    cv.waitKey(3000)

    app.make_final_display()  # 內含對 mainloop() 的呼叫

if __name__ == '__main__':
    main()
