import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('2_image_processing/3_smoothing_images/lenna.png')

# cv.blur(src, ksize[, dst[, anchor[, borderType]]])->dst
# src. 입력 이미지.
# dst. 출력 이미지.
# ksize. 커널 크기
blur = cv.blur(img, (5, 5))

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()