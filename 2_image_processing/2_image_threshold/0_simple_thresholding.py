import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 단순 임계처리는 매우 간단하다.
# 모든 픽셀에 같은 임계점 값이 적용된다.
# 픽셀의 값이 임계점보다 작으면 0, 크면 최대값으로 적용된다.

img = cv.imread("1_core/1_arithmetic_operation/macbook.png", 0)

# 임계처리는 cv.threshold 함수로 처리한다.
# cv.threshold(src, thresh, maxval, type[, dst])
# src. 반드시 gray scale인 흑백 이미지
# thresh. 픽셀 값을 분류하는데 사용될 임계점
# maxval. 픽셀이 임계점보다 클 때 픽셀에 할당할 값
# type. 임계처리하는 방식. 여기서 단순 임계처리는 cv.THRESH_BINARY이다.
# 단순 임계처리의 타입들
# cv.THRESH_BINARY
# cv.THRESH_BINARY_INV
# cv.THRESH_TRUNC
# cv.THRESH_TOZERO
# cv.THRESH_TOZERO_INV
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()