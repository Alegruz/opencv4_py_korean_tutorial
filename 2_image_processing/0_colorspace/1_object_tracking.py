import cv2 as cv
import numpy as np

# HSV는 BGR보다 색을 표현하기에 더 적합하다.
# 이를 통해 파란색을 띠는 물체를 추적해보겠다.

# 비디오 캡쳐 받기 
cap = cv.VideoCapture(0)

while (True):
    # 프레임을 받는다
    _, frame = cap.read()

    # BGR을 HSV로 변환함
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # HSV에서 파란색의 범위를 지정해줌
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # HSV 이미지의 마스크를 만들어 파란색만을 출력하도록 함
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # 프레임과 마스크를 통해 bitwise-and 연산을 함
    res = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    k = cv.waitKey(5) & 0xFF
    if (k == 27):
        break

cv.destroyAllWindows()