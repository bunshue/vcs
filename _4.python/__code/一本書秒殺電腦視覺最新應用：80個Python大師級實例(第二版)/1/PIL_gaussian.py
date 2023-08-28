from PIL import Image
from pylab import *
from scipy.ndimage import filters
import numpy

def imx(im, sigma):
    imgx = zeros(im.shape)
    filters.gaussian_filter(im, sigma, (0, 1), imgx)
    return imgx
def imy(im, sigma):
    imgy = zeros(im.shape)
    filters.gaussian_filter(im, sigma, (1, 0), imgy)
    return imgy
def mag(im, sigma):
    # 还有gaussian_gradient_magnitude()
    imgmag = 255 - numpy.sqrt(imgx ** 2 + imgy ** 2)
    return imgmag

im = array(Image.open('castle3.jpg').convert('L'))
figure()
gray()
sigma = [2, 5, 10]
for i in  sigma:
    subplot(3, 4, 4*(sigma.index(i))+1)
    axis('off')
    imshow(im)
    imgx=imx(im, i)
    subplot(3, 4, 4*(sigma.index(i))+2)
    axis('off')
    imshow(imgx)
    imgy=imy(im, i)
    subplot(3, 4, 4*(sigma.index(i))+3)
    axis('off')
    imshow(imgy)
    imgmag=mag(im, i)
    subplot(3, 4, 4*(sigma.index(i))+4)
    axis('off')
    imshow(imgmag)
show()
