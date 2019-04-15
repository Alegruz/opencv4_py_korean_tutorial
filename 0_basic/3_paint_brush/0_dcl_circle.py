import cv2 as cv
import numpy as np

# 마우스 입력을 받음

# 배울 함수
# cv.setMouseCallback() -> 마우스 입력 받기

# 마우스 입력 받기
# event: 마우스 입력받은 이벤트.
# x, y: 마우스 이벤트가 발생한 좌표
# flags: 마우스 입력이 무엇인지. 0이면 아무것도 아님. 1이면 좌클릭. 2면 우클릭. 4면 휠클릭. 엄청 큰 양/음 정수면 휠 돌리기
# param: 얜 뭘까? 나도 모르겠당 ㅎㅎ
# event와 flags의 차이점. flags는 단순히 클릭받은 것이 무엇이느냐?의 느낌이라면, event는 어떤 방식의 클릭이느냐.
# flags는 더블클릭을 인식할 수 없지만, event는 인식가능.
def draw_circle(event, x, y, flags, param):
    if (event == cv.EVENT_LBUTTONDBLCLK):              # 만약 입력 이벤트가 마우스 좌더블클릭이라면
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)   # 입력받은 좌표에 반지름 100, 파란색인 안이 꽉찬 원 생성

# 검은 색 창 띄우기
img = np.zeros((512, 512, 3), np.uint8)     # 검은 색 512x512 사진 생성
cv.namedWindow("image")                    # "image"라는 이름의 창 생성

# cv.setMouseCallback(windowName, onMouse[, param]) -> None
# windowName 위에서 마우스가 작동할 때, 작동하는 이벤트에 따라 onMouse 함수에 argument들을 제공한다
# 제공하는 argument들
# 1. 발생한 이벤트
# 2. 좌표 x
# 3. 좌표 y
# 4. 마우스 버튼
# 5. 이건 모르겠다 ㅎㅎ 
cv.setMouseCallback("image", draw_circle)  # 이 창에서 마우스 입력 받으면 draw_circle 함수 실행

while (True):
    cv.imshow("image", img)            # 이미지 출력
    if (cv.waitKey(20) & 0xFF == 27):  # esc 누르면 창 종료
        break
cv.destroyAllWindows()