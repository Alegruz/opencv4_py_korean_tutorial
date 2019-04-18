import cv2 as cv
import numpy as np

img = cv.imread('2_image_processing/3_smoothing_images/lenna.png', 0)
ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

# cv.dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])->dst
# src. 입력 이미지.
# dst. 출력 이미지. src와 크기와 타입이 같음.
# kernel. dilation에 사용될 structuring element.
# iterations. dilation이 적용되는 회수. 기본값은 1.
dilation = cv.dilate(thresh, kernel, iterations = 1)

cv.imshow("Original", thresh)
cv.imshow("Dilated", dilation)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()