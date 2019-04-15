import numpy as np
import cv2 as cv

# 텍스트를 출력함

# 배울 것
# cv.putText() -> 글을 그림

# 검은 사진 생성
img = np.zeros((512, 512, 3), np.uint8)

# 선 그리기
img = cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 직사각형 그리기
img = cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 원 그리기
img = cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 타원 그리기
img = cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# 다각형 그리기
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
img = cv.polylines(img, [pts], True, (0, 255, 255))

# 텍스트 그리기
# 폰트 지정해주기
font = cv.FONT_HERSHEY_SIMPLEX

# cv.putText(그릴 사진, "텍스트", 텍스트 시작할 좌하단 좌표, 폰트, 폰트크기, 색깔, [굵기=1, [선종류, [시프트=0]]])
cv.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
# OpenCV라고 적힐 cv.FONT_HERSHEY_SIMPLEX 폰트를 갖고 크기는 4짜리, 굵기는 2짜리 검은색 텍스트가 좌표 (10, 500)에 cv.LINE_AA 타입의 선으로 출력됨

cv.imshow("geometry", img)

if (cv.waitKey(0) & 0xFF == 'q'):
    cv.destroyAllWindows()