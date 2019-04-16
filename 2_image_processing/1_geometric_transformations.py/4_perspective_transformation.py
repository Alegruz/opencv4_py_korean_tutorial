import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 시점변환은 3x3 행렬에 의해 이루어진다.
# 시점변환을 하기 위해선 기존 이미지에서 네 개의 벡터와 변환 이후에 그 벡터들이다. 이 중 세 개 이상이 일차종속 관계여선 안된다.
# 시점변환은 cv.getPerspectiveTransform 함수를 통해 얻는다
# 얻은 변환행렬을 cv.warpPerspective 함수를 통해 적용한다.

img = cv.imread("1_core/1_arithmetic_operation/macbook.png")
rows, cols = img.shape[:2]

pts1 = np.float32([[105, 539], [784, 539], [67, 648], [823, 648]])
pts2 = np.float32([[0, 0], [640, 0], [0, 400], [640, 400]])

# cv.getPerspectiveTransform(src, dst[, solveMethod]) -> retval
# src 변환할 이미지에서 추출한 벡터들
# dst 변환 이후의 벡터값
M = cv.getPerspectiveTransform(pts1, pts2)

# cv.warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst
# cv.warpAffine과 비슷함
dst = cv.warpPerspective(img, M, (640, 400))

plt.subplot(121), plt.imshow(img), plt.title("Input")
plt.subplot(122), plt.imshow(dst), plt.title("Output")
plt.show()