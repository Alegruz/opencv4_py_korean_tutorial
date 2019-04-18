import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('2_image_processing/3_smoothing_images/lenna_noise.png')

median = cv.medianBlur(img, 5)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()