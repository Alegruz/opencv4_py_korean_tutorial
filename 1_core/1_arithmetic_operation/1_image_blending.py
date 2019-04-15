import cv2 as cv
import numpy as np
import time         # 딜레이 설정
import math         # 이미지 페이드 인아웃 속도 조절

# 이미지 두 개를 섞어서 전환하는 방법

# 배울 것
# cv.addWeighted() -> f(x) = (1 - a)g(x) + ah(x) 이 식을 통해 페이드 인 아웃 설정. a의 값이 지속적으로 증가한다고 가정

img1 = cv.imread("1_core/1_arithmetic_operation/apple.jpg")    # 1번 사진
img2 = cv.imread("1_core/1_arithmetic_operation/ubuntu.png")   # 2번 사진. 1번에서 2번으로 페이드 인아웃 할 것
i = 0.00            # 페이드 정도
direction = True    # 페이드 방향

while (True):
    # cv.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
    # src1, src2 두 이미지
    # alpha src1의 정도
    # beta src2의 정도
    # gamma 여기에 추가할 추가상수
    dst = cv.addWeighted(img1, math.cos(math.pi * i / 2), img2, 1 - math.cos(math.pi * i / 2), 0)
    cv.imshow("dst", dst)

    k = cv.waitKey(1) & 0xFF
    if (k == ord('r')): # 페이드 방향 전환
        direction = not direction
    elif (k == 27):
        break
    
    if (direction == True):                     # apple -> ubuntu
        if (0 <= math.trunc(i * 100) < 100):
            i += 0.01
    else:                                       # ubuntu -> apple
        if (0 < math.trunc(i * 100) <= 100):
            i -= 0.01

    time.sleep(1 / 60)   # 프레임수 fps 60

cv.destroyAllWindows()