import numpy as np
import cv2 as cv

# 카메라 입력을 받아 출력함

# 배울 함수들
# cv.VideoCapture() -> 카메라로부터 영상을 입력받음

# 카메라 입력 받기
# cv.VideoCapture(카메라 번호)
# 통상적으로 내장 카메라는 0이다
cap = cv.VideoCapture(0)
# cap은 cv.VideoCapture 오브젝트

while(True):
    # 프레임 입력 받기
    # cap.read() -> 프레임이 잘 읽히면 True를 리턴함
    ret, frame = cap.read()
    # 여기서 cap.read()는 tuple을 반환한다
    # ret이 위에서 말한 프레임 읽힌 여부 (bool)
    # frame이 읽힌 프레임의 사진 정보 (numpy.ndarray)

    # 프레임 사진 흑백으로 만들기
    # cv.cvtColor(프레임, 작업내용) -> convert color. 사진을 바꿔줌
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.COLOR_BGR2GRAY 는 이름에서 드러나듯이 색깔을 BGR(혹은 RGB)에서 흑백(GRAY)로 전환해줌

    # 최종 프레임 출력
    cv.imshow("frame", gray)
    if (cv.waitKey(1) & 0xFF == ord('q')):
        break

# 작업이 전부 끝나면 캡쳐 종료
cap.release()
cv.destroyAllWindows()

# cap.get(propId)
# 영상의 특정 정보를 뽑아낸다
# 예를 들어 propId가 3번, CV_CAP_PROP_FRAME_WIDTH이라면 영상의 프레임의 너비를 알 수 있다.
# cap.get(3) / cap.get(4) -> 프레임의 너비 / 높이