import cv2 as cv
import numpy as np

# BGR에서의 색은 알겠는데, HSV에서는 모르겠다면?
# 우선 BGR에서의 색을 갖는 행렬을 만든다
blue = np.uint8([[[255, 0, 0]]])
green = np.uint8([[[0, 255, 0]]])
red = np.uint8([[[0, 0, 255]]])

# 그 행렬을 색변환해준다
hsv_blue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
hsv_red = cv.cvtColor(red, cv.COLOR_BGR2HSV)

# HSV 색 얻었다!
print(hsv_blue)
print(hsv_green)
print(hsv_red)