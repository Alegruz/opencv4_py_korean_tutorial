import cv2 as cv
import numpy as np

img = cv.imread('2_image_processing/3_smoothing_images/lenna.png', 0)
ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

# cv.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])->dst
# src. 입력 이미지.
# dst. 출력 이미지. src와 크기와 타입이 같음.
# op. 형태변환의 종류.
# kernel. structuring element.
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)

cv.imshow("Original", thresh)
cv.imshow("Opening", opening)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()