import numpy as np
import cv2 as cv

# 평행이동이란 물체의 위치를 옮기는 것이다.
# (x, y) 좌표가 어떻게 옮길지에 대한 정보 (tx, ty)가 있다면
# 평행이동 변환행렬 M은 [[1 0 tx], [0 1 ty]] 과 같다
# v = (x, y) 라 할 때, tx, ty만큼 평행이동한 새로운 벡터 vt는
# vt = v x M = (x + tx, y + ty)

img = cv.imread("1_core/1_arithmetic_operation/apple.jpg")
rows, cols = img.shape[:2]  # 이미지의 행과 열의 개수 = 이미지의 크기

# x로 100만큼, y로 50만큼 평행이동
M = np.float32([[1, 0, 100], [0, 1, 50]])

# cv.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])->dst
# src 변환할 이미지
# M 변환행렬 (float32 이거나 float64)
# dsize 행렬의 크기. 순서는 반드시 너비(열), 높이(행)이다.
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("img", dst)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()