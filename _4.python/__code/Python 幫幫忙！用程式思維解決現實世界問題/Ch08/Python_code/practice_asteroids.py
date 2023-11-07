import random
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

STAR_RADIUS = 165
BLACK_IMG = np.zeros((400, 500, 1), dtype="uint8")
NUM_ASTEROIDS = 15
NUM_LOOPS = 170

class Asteroid():
    """建立小行星物件"""
    def __init__(self, number):
        self.radius = random.choice((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3))
        self.x = random.randint(-30, 60)
        self.y = random.randint(220, 230)
        self.dx = 3  

    def move_asteroid(self, image):
        """畫出並移動小行星物件"""
        cv.circle(image, (self.x, self.y), self.radius, 0, -1)
        self.x += self.dx
        

def record_transit(start_image):
    """畫出行星淩日過程並傳回記錄亮度值的 list"""
    asteroid_list = []
    intensity_samples = []
    
    for i in range(NUM_ASTEROIDS):
        asteroid_list.append(Asteroid(i))
        
    for _ in range(NUM_LOOPS):
        temp_img = start_image.copy()
        # 畫出恆星  
        cv.circle(temp_img, (250, 200), STAR_RADIUS, 255, -1)
        for ast in asteroid_list:
            ast.move_asteroid(temp_img)
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
