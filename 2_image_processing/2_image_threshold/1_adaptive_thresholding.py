import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 단순임계처리에선 모든 픽셀마다 단 하나의 임계점만을 부여했음.
# 근데 만약 이미지에서 여러 부분이 각기 다른 방식으로 조명이 쏘아지고 있다면 임계점이 상수면 좋지 않은 결과를 얻을 수 있음
# 그렇기 때문에 근처 상황에 따라 임계점을 설정하는 알고리즘을 사용해야함
# 그것이 적응임계처리.

img = cv.imread('1_core/1_arithmetic_operation/macbook.png',0)

# cv.medianBlur(src, ksize[, dst]) -> dst
# 미디언 필터를 이용해 이미지를 블러처리하여 이미지를 부드럽게 만들어줌
# src. 1 / 3 / 4 채널 이미지. ksize가 3이거나 5면 이미지의 차원은 uint8 / uint16 / float32이어야함. aperture 값이 크면 uint8 밖에 안됨
# ksize. aperture linear size. 1보다 큰 홀수
img = cv.medianBlur(img, 5)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

# cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
# src. 8비트 단일채널 이미지
# maxValue. 조건에 따라 픽셀에 부여할 0이 아닌 값
# adaptiveMethod. 사용할 적응임계처리 알고리즘
# thresholdType.
# blockSize. 픽셀의 임계점을 계산할 때 사용할 구역의 크기: 3, 5, 7, 등등
# C. 평균 혹은 평균무게에서 뺄 상수. 주로 양수지만 0이나 음수도 가능
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()