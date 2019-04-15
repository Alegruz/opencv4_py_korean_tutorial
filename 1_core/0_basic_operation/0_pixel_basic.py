import cv2 as cv
import numpy as np

# 배울 것
# 사진의 특정 픽셀 참조 및 편집

img = cv.imread("1_core/0_basic_operation/barracks.jpg")

cv.namedWindow("image", cv.WINDOW_NORMAL)

# 픽셀 참조하기
px = img[100, 100]

# 픽셀의 B 색깔 참조하기
blue = img[100, 100, 0]

# 픽셀 편집하기 (색 바꾸기)
px = [255, 255, 255]
print(px)

cv.imshow("image", img)

if (cv.waitKey(0) & 0xFF == 27):
    cv.destroyAllWindows()