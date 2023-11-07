import random
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

STAR_RADIUS = 165
BLACK_IMG = np.zeros((400, 500, 1), dtype="uint8")
NUM_SHIPS = 5
NUM_LOOPS = 300

class Ship():
    """建立太空船物件"""
    def __init__(self, number):
        self.number = number
        self.shape = random.choice(['>>>|==H[X)',
                                    '>>|==H[XX}=))-',
                                    '>>|==H[XX]=(-'])
        self.size = random.choice([0.7, 0.8, 1])
        self.x = random.randint(-180, -80)
        self.y = random.randint(80, 350)
        self.dx = random.randint(2, 4)
        
    def move_ship(self, image):
        """畫出並移動太空船物件"""
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img=image, 
                   text=self.shape,
                   org=(self.x, self.y),
                   fontFace=font,
                   fontScale=self.size,
                   color=0,
                   thickness=5) 
        self.x += self.dx
        
def record_transit(start_image):
    """畫出行星淩日過程並傳回記錄亮度值的 list"""
    ship_list = []
    intensity_samples = []
    
    for i in range(NUM_SHIPS):
        ship_list.append(Ship(i))
        
    for _ in range(NUM_LOOPS):
        temp_img = start_image.copy()
        # 畫出恆星
        cv.circle(temp_img, (250, 200), STAR_RADIUS, 255, -1)
        for ship in ship_list:
            ship.move_ship(temp_img)
        intensity = temp_img.mean()
        cv.putText(temp_img, 'Mean Intensity = {}'.format(intensity),
                   (5, 390), cv.FONT_HERSHEY_PLAIN, 1, 255)
        cv.imshow('Transit', temp_img)
        intensity_samples.append(intensity)
        cv.waitKey(50)
    cv.destroyAllWindows()
    return intensity_samples


def calc_rel_brightness(image):
    """將亮度 list 中的值換算成相對亮度值並傳回"""
    rel_brightness = record_transit(image)
    max_brightness = max(rel_brightness)
    for i, j in enumerate(rel_brightness):
        rel_brightness[i] = j / max_brightness
    return rel_brightness

def plot_light_curve(rel_brightness):
    """畫出相對亮度隨時間變化的曲線"""
    plt.plot(rel_brightness, color='red', linestyle='dashed',
             linewidth=2, label='Relative Brightness')
    plt.legend(loc='upper center')
    plt.title('Relative Brightness vs. Time')
    plt.show()
    
relative_brightness = calc_rel_brightness(BLACK_IMG)
plot_light_curve(relative_brightness)
