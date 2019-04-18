import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('1_core/1_arithmetic_operation/macbook.png')

# numpy.ones(shape, dtype=None, order='C)->ndarray
# shape. 새로 만들 행렬의 형태
# dtype. 행렬의 원소들의 데이터타입
kernel = np.ones((5, 5), np.float32) / 25   # 평균필터커널. 모든 원소의 값이 1인 5x5 행렬을 5^2로 나누어줌

# cv.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
# src. 입력 이미지
# ddepth. 출력 이미지의 depth. 입력 이미지와 같은 depth를 같게 해주려면 -1를 입력해주면 된다
# kernel. convolution kernel. 단일채널 float 행렬.
dst = cv.filter2D(img, -1, kernel)          # 해당 필터를 img에 적용함

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst),  plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()