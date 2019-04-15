import numpy as np
import cv2 as cv

# 배울 것
# cv.polylines() -> 다각형 그림
# numpy.array() -> 특정 행렬 생성
# numpy.ndarray.reshape() -> 행렬 변환

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
# numpy.array(오브젝트, 데이터타입)
# 오브젝트라함은 list, set, tuple 등을 받음을 의미함
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts는 numpy.ndarray 오브젝트
# pts는 4 x 2 2차원 행렬

# cv.polylines(사진, 점들, 닫힘여부, RGB색, [굵기=1, [선종류, [시프트=0]]])
img = cv.polylines(img, [pts], True, (0, 255, 255))
# (0, 255, 255) == 노란색
# cv.polylines()를 이용해서 여러 선들을 동시에 그릴 수 있다. cv.line()보다 훨씬 유용함

cv.imshow("geometry", img)

if (cv.waitKey(0) & 0xFF == 'q'):
    cv.destroyAllWindows()