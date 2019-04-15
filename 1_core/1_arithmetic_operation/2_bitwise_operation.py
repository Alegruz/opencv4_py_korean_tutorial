import cv2 as cv
import numpy as np

# 배울 것
# cv.threshold() -> 마스크 생성
# cv.bitwise_not() -> 반대 비트로 전환
# cv.bitwise_and() -> 두 이미지 간 교집합을 마스크에 맞춰 반환

# 이미지 두 개 받는다
img1 = cv.imread('1_core/1_arithmetic_operation/macbook.png')
img2 = cv.imread('1_core/1_arithmetic_operation/opencv_logo.png')

# ROI를 통해 이미지를 좌상단에 놓을 수 있도록 한다
rows,cols,channels = img2.shape # OpenCV 로고의 크기를 받는다
roi = img1[0:rows, 0:cols ]     # 맥북 이미지의 좌상단에 로고 크기만큼의 공간을 받는다

# OpenCV 로고의 마스크를 만들고, 반대색의 마스크도 만든다
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)                # 애플 로고의 흑백 버전

# cv.threshold(src, thresh, maxval, type[, dst]) -> retval, dst
# src 수정할 이미지
# thresh 한계점 값
# maxval 한계점 타입을 사용할 최대값
# type 한계점 타입
ret, mask = cv.threshold(img2gray, 254, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# 이제 ROI에서 로고가 아닌 부분을 제거한다
img1_bg = cv.bitwise_and(roi, roi, mask = mask)

# 로고 이미지에서 로고 부분만 떼어낸다
img2_fg = cv.bitwise_and(img2, img2, mask = mask_inv)

# # ROI에 로고를 넣고 이미지를 수정한다
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols ] = dst

cv.imshow('res', img1)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
