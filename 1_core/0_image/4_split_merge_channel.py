import cv2
import numpy as np

# 배울 것
# cv2.split() -> 사진 여러 채널로 나누기
# cv2.merge() -> 여러 채널 한 사진으로 합치기

img = cv2.imread("1_core/0_image/barracks.jpg")
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# 함수를 이용한 방법

# 사진 여러 채널로 나누기
# cv2.split(m[, mv]) -> mv
# m: 입력받는 다중채널 행렬
# mv: 행렬의 결과 벡터. (나도 뭔지 몰라용 홍홍)
# 상당히 메모리를 많이 잡아먹는 작업이다.
b, g, r = cv2.split(img)

# 여러 채널 한 사진으로 합치기
# cv2.merge(mv[, dst]) -> dst
# mv: 한 행렬로 합칠 여러 벡터들
# dst: mv[0]과 같은 깊이와 크기를 갖는 행렬.
img = cv2.merge((b, g, r))

# 슬라이스를 이용한 방법
# cv2.split()보다 메모리를 덜 잡아먹기에 이게 더 낫다
b = img[:,:, 0]
g = img[:,:, 1]
r = img[:,:, 2]

# 채널 수정
img[:,:, 2] = 0

cv2.imshow("image", img)

if (cv2.waitKey(0) & 0xFF == 27):
    cv2.destroyAllWindows()