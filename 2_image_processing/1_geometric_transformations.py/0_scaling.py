import cv2 as cv
import numpy as np

# scaling은 단순히 이미지의 크기를 조절하는 것이다.
# cv.resize()라는 함수를 사용한다.
# 이미지의 크기를 직접 지정해주거나, 조절 정도를 지정해줄 수 있다.
# 조절 방법에는 여러 가지 방법이 있다.
# 주로는 cv.INTER_AREA를 통해 줄이고, cv.INTER_CUBIC이나 cv.INTER_LINEAR을 통해 확대를 한다.
# 기본 설정으로 줄일 땐 cv.INTER_LINEAR이 사용된다.

img = cv.imread("1_core/1_arithmetic_operation/apple.jpg")

# cv.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst
# src 사이즈 조정할 이미지
# dsize 조정할 크기. 만약 dsize가 None이라면 fx와 fy의 값을 사용한다
# fx, fy 조정할 크기. 만약 fx와 fy가 None이라면 dsize의 값을 사용한다
# interpolation 조정 방식
res = cv.resize(img, None, fx = 2, fy = 2, interpolation = cv.INTER_CUBIC)

# 혹은

height, width = img.shape[:2]

res = cv.resize(img, (2 * width, 2 * height), interpolation = cv.INTER_CUBIC)

cv.imshow("image", img)
cv.imshow("resized image", res)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()