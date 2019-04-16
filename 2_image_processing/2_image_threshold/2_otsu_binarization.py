import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 전역임계처리(==단순임계처리)에선 사용자가 임의로 정한 임계점을 사용
# Otsu 임계처리에선 자동으로 임계점을 설정함

# 서로 다른 이미지값을 갖는 이미지(이중모드 이미지)가 있다고 가정해보자
# 이 이미지의 히스토그램은 두 개의 극대점을 가질 것이다.
# 여기서 임계점을 설정한다면, 이 두 개의 극대점 사이의 값일 것이다.
# 이러한 방식으로 임계점을 결정하는 것이 Otsu 임계처리

# 우선 cv.thresh 함수에서 type을 cv.THRESH_OTSU을 추가적으로 설정해준다.
# threshold 값은 임의로 설정해줘도 좋다.
# 이를 통해 임계점은 Otsu 임계처리 알고리즘에 의해 결정된다.

img = cv.imread('1_core/1_arithmetic_operation/ubuntu.png',0)

# 단순임계처리 (전역임계처리)
ret1,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# Otsu 임계처리
ret2,th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# Gaussian 필터링을 해준 다음 Otsu 임계처리
blur = cv.GaussianBlur(img,(5, 5), 0)
ret3,th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# 생성한 이미지들을 출력해줌
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()