import numpy as np
import cv2 as cv

# 이미지를 출력할 창을 생성하고 이미지를 저장하는 법을 배움

# 배울 함수들
# cv.namedWindow() -> 창을 먼저 만들어줌
# cv.imwrite() -> 사진을 저장함

# 흑백 사진 받기
img = cv.imread("0_basic/0_image/barracks.jpg", 0)

# 사진 출력하기 전에 창을 미리 만들어서 크기를 지정해줄 수 있음
# cv.namedWindow("창 이름", 사이즈)
# 사이즈의 default는 cv.WINDOW_AUTOSIZE. 말 그대로 사이즈는 자동.
# cv.WINDOW_NORMAL을 통해 사이즈를 지정해줄 수 있음.
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow('image', img)

# 입력 받기
# 이 함수의 리턴값은 입력받은 문자의 ASCII 값.
k = cv.waitKey(0) & 0xFF

# 사진 저장하기
# cv.imwrite("사진이름.확장자", 사진)
# esc를 입력하면 종료하고, s를 입력하면 사진을 저장하고 나서 종료
if (k == 27):
    cv.destroyAllWindows()
elif (k == ord('s')):
    cv.imwrite("0_basic/0_image/barracks_gray.png", img)
    cv.destroyAllWindows()