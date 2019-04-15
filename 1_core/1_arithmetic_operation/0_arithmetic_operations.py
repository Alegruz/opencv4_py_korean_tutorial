import cv2 as cv
import numpy as np

# 이미지 두 개를 더하는 방법

# 배울 것
# cv.add() / + operator -> shape과 dtype이 같은 두 이미지를 더함

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x, y))    # 250 + 10 = 260 => 255 (dtype == uint8이므로 unsigned int 8비트 최대값은 2^8 - 1 = 255)

print(x + y)    # 250 + 10 = 260, 260 % 256 = 4

cv.namedWindow("image")

while (True):
    cv.imshow("image", x)

    k = cv.waitKey(1) & 0xFF
    if (k == ord('a')):
        x = x + y
    elif (k == ord('b')):
        x = cv.add(x, y)
    elif (k == 27):
        break

cv.destroyAllWindows()