import numpy as np
import cv2 as cv

# 영상 파일을 입력받아 출력함

# 배울 함수들
# cv.VideoCapture.isOpened() -> cap이 제대로 초기화 되었는지 확인한다.

# 영상 입력 받기
# cv.VideoCapture("영상제목.확장자")
# 굳이 카메라 입력만 받을 수 있는 것이 아니다.
cap = cv.VideoCapture("vtest.avi")

# cap이 제대로 초기화가 안되었을 수도 있다. 그런 경우에 아래 코드는 에러가 발생함
# cap.open()
# cap을 초기화한다.
while(cap.isOpened()):
    # 프레임 입력 받기
    ret, frame = cap.read()

    # 프레임 사진 흑백으로 만들기
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 최종 프레임 출력
    cv.imshow("frame", gray)
    if (cv.waitKey(1) & 0xFF == ord('q')):
        break

# 작업이 전부 끝나면 캡쳐 종료
cap.release()
cv.destroyAllWindows()