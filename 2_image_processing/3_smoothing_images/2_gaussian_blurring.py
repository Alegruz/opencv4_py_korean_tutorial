import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('2_image_processing/3_smoothing_images/lenna.png')

blur = cv.GaussianBlur(img, (5, 5), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()