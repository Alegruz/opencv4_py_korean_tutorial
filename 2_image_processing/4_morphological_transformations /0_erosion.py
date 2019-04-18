import cv2 as cv
import numpy as np

img = cv.imread('2_image_processing/3_smoothing_images/lenna.png', 0)
ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

# cv.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])->dst
# src. 입력 이미지.
# dst. src와 같은 크기와 타입을 갖는 이미지.
# kernel. erosion에 사용된 structuring element.
# iterations. erosion이 발생한 횟수. 기본값은 1이다.
erosion = cv.erode(thresh, kernel, iterations = 1)

cv.imshow("Original", thresh)
cv.imshow("Eroded", erosion)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()