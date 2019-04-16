import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 어파인 변환이란 이미지의 축을 변환하는 것이다.
# 어파인 변환행렬은 이미지의 내의 세 벡터와 변환 이후 벡터들의 위치에 따라 결정된다.
# 이후 cv.getAffineTransform 함수를 통해 cv.warpAffine에서 사용할 2x3 행렬을 생성한다

img = cv.imread("1_core/1_arithmetic_operation/macbook.png")
rows, cols = img.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# cv.getAffineTransform(src, dst) -> retval
# src 변환할 이미지에서 추출한 벡터들
# dst 변환 이후의 벡터값
M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title("Input")
plt.subplot(122), plt.imshow(dst), plt.title("Output")
plt.show()