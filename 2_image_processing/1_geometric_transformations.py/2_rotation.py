import numpy as np
import cv2 as cv
import math

# 이미지를 특정 각도 theta에 따라 회전시키려면 다음과 같은 변환행렬을 사용해주면 된다
# M = [[cosA -sinA], [sinA cosA]]
# OpenCV에선 단순 회전 뿐만 아니라 회전이 되는 기준을 설정해줄 수 있다. 이를 포함한 회전변환은 다음과 같다
# [[a b (1 - a) * center.x - b * center.y] [-b a b * center.x + (1 - a) * center.y]]
# a = scale * cosA, b = scale * sinA
# 회전 변환은 cv.getRotationMatrix2D 함수를 사용한다.

img = cv.imread("1_core/1_arithmetic_operation/macbook.png")
rows, cols = img.shape[:2]

# cols - 1과 rows - 1가 각각 y와 x 좌표의 최대값이다.
# cv.getRotationMatrix2D(center, angle, scale) -> retval
# center 회전 기준
# angle 회전 정도
# scale 회전의 등방인수 (나도 뭔 말인지 모름. 아무튼 사진 확대 시켜 줌)
M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("img", dst)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()