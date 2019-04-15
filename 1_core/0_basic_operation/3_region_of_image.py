import cv2 as cv
import numpy as np

# 배울 것
# ROI (region of image)

img = cv.imread("1_core/0_basic_operation/barracks.jpg")
cv.namedWindow("image", cv.WINDOW_NORMAL)

# ROI 사용
eighth_army = img[81:570, 2415:3045]    # (2415, 81) ~ (3045, 570) 사이의 직사각형 부분 복사
img[985:1474, 2470:3100] = eighth_army  # (2470, 985) ~ (3100, 1474) 같은 크기의 다른 부분에 복사한 부분 붙여넣기

cv.imshow("image", img)

if (cv.waitKey(0) & 0xFF == 27):
    cv.destroyAllWindows()