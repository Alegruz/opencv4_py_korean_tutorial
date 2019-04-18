import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('2_image_processing/5_image_gradients/sudoku.jpg', 0)

# cv.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])->dst
# src. 원본 이미지
# dst. src와 같은 크기, 같은 채널 수를 갖는 출력 이미지
# ddepth. dst의 희망 depth
laplacian = cv.Laplacian(img, cv.CV_64F)

# cv.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])->dst
# src. 입력 이미지
# dst. 출력 이미지. src와 같은 크기, 채널 수를 가짐
# ddepth. 출력 이미지의 depth
# dx. x 도함수의 순서
# dy. y 도함수의 순서
# ksize. 확장 Sobel 커널의 크기. 반드시 1, 3, 5, 7 중 하나여야함.
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize = 5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize = 5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()