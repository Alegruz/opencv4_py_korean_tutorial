import cv2 as cv
import numpy as np

# 배울 것
# 사진의 속성을 알려주는 사진 오브젝트의 변수들

img = cv.imread("1_core/0_basic_operation/barracks.jpg")
cv.namedWindow("image", cv.WINDOW_NORMAL)

# img.shape -> 사진의 행렬의 각 차원의 스칼라의 개수. 512x512짜리 흑백 사진이면 (512, 512), 색사진이면 (512, 512, 3)
# img의 형태를 알고 싶을 때 사용
print(img.shape)

# img.size -> 총 픽셀의 개수
print(img.size)

# img.dtype -> 행렬의 스칼라의 데이터 타입
# OpenCV의 많은 에러가 dtype이 달라서 발생하는 경우임. 상당히 중요한 속성변수.
print(img.dtype)

cv.imshow("image", img)

if (cv.waitKey(0) & 0xFF == 27):
    cv.destroyAllWindows()