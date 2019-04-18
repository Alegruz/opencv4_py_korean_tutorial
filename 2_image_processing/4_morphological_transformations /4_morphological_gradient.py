import cv2 as cv
import numpy as np

img = cv.imread('2_image_processing/3_smoothing_images/lenna.png', 0)
ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
morphGrad = cv.morphologyEx(thresh, cv.MORPH_GRADIENT, kernel)

cv.imshow("Original", thresh)
cv.imshow("Morphological Gradient", morphGrad)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()