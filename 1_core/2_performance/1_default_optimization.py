import cv2 as cv
import numpy as np

# 왜 최적화가 필요한가? 이미지처리에는 엄청나게 많은 연산이 진행되기 때문
# 배울 것
# cv.getTickCount
# cv.getTickFrequency

img = cv.imread("../1_arithmetic_operation/apple.jpg")
cv.setUseOptimized(True)    # 기본 최적화 기능 on

for i in range(0, 2):
    e1 = cv.getTickCount()                                                      # 코드 실행 시간
    for i in range(5, 49, 2):
        img = cv.medianBlur(img, i)
    e2 = cv.getTickCount()                                                      # 코드 실행 종료 시간
    t = (e2 - e1) * 1000 / cv.getTickFrequency()                                # 총 코드 실행 시간
    print("Default OpenCV Optimization:", cv.useOptimized(), "\t", t, "ms")
    cv.setUseOptimized(False)                                                   # 기본 최적화 기능 off