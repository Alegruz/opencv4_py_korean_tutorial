import cv2 as cv
import numpy as np

# 배울 것
# 사진의 특정 픽셀 함수로 참조 및 편집

img = cv.imread("1_core/0_basic_operation/barracks.jpg")

cv.namedWindow("image", cv.WINDOW_NORMAL)

# 픽셀 참조하기
# img.item(좌표) -> 해당 좌표 스칼라값
red = img.item(10, 10, 2)

# 픽셀 수정하기
# img.itemset(좌표, 수정할 스칼라값) -> 해당 좌표의 스칼라값을 주어진 수정할 스칼라값으로 바꿈
img.itemset((10, 10, 2), 100)

cv.imshow("image", img)

if (cv.waitKey(0) & 0xFF == 27):
    cv.destroyAllWindows()