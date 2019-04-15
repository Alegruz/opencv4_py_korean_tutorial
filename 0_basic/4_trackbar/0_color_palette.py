import cv2 as cv
import numpy as np

# 배울 함수
# cv.createTrackbar() -> 트랙바 생성
# cv.getTrackbarPos() -> 트랙바의 현재 값 받기

def nothing(x):
    pass

# 검은 창 생성
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("image")

# 색 바꿔줄 트랙바 생성
# cv.createTrackbar(trackbarName, windowName, value, count, onChange)
# trackbarName = 트랙바 이름
# windowName = 트랙바 생성해줄 창 이름
# value, count -> 트랙바 최소값에서 최대값
# onChange -> 얜 뭔지 잘 ㅎㅎ
cv.createTrackbar('R', "image", 0, 255, nothing)
cv.createTrackbar('G', "image", 0, 255, nothing)
cv.createTrackbar('B', "image", 0, 255, nothing)

# 스위치 온/오프 기능 추가
switch = "0 : OFF \n1 : ON"
cv.createTrackbar(switch, "image", 0, 1, nothing)

while (True):
    cv.imshow("image", img)
    
    if (cv.waitKey(1) & 0xFF == 27):
        break
    
    # 트랙바들의 값 확인
    # cv.getTrackbarPos(trackbarname, winname)
    # trackbarname = 값을 가져올 트랙바 이름
    # winname = 해당 창 이름
    r = cv.getTrackbarPos('R', "image")    # 즉, 만약 'R'의 트랙바를 사용자가 100으로 옮기면 r의 값은 100이 됨
    g = cv.getTrackbarPos('G', "image")
    b = cv.getTrackbarPos('B', "image")
    s = cv.getTrackbarPos(switch, "image")

    # 스위치 여부에 따라 사진 변경
    if (s == 0):            # 스위치 OFF
        img[:] = 0          # 사진은 검은색으로 유지. img 행렬의 모든 원소, 즉 사진의 모든 픽셀의 색을 0으로 만들어서 검은색으로 만들어준다
    else:                   # 스위치 ON
        img[:] = [b, g, r]  # img 행렬의 모든 벡터들, 즉 모든 픽셀의 색을 BGR(RGB)대로 지정해주어 트랙바에 따라 사진의 색이 바뀌게 만들어줌
                            # 만약 s가 1, R G B 가 순서대로 255 0 255라면 사진의 색은 보라색이 될 것이다

cv.destroyAllWindows()