import numpy as np                      # numpy. 사진을 처리하는데 행렬(배열)이 필요하기 때문에 사용하는 모듈.
import cv2                              # opencv.

# 배울 함수들
# cv2.imread() -> 사진을 입력받음
# cv2.imshow() -> 사진을 출력함

# 흑백 사진 받기
# cv2.imread("사진이름.확장자", 두번째 argument)
# cv2.imread() 함수의 두번째 argument
# cv2.IMREAD_COLOR -> 색 사진으로 입력함. 투명도 설정 X (1)
# cv2.IMREAD_GRAYSCALE -> 흑백 사진 (0)
# cv2.IMREAD_UNCHANGED -> 알파 채널 추가 (-1)
# 이렇게 세 가지 대신 그냥 순서대로 정수 1, 0, -1으로 입력해줘도 가능
img = cv2.imread("0_basic/0_image/barracks.jpg", 0)
# img 오브젝트의 타입은 numpy.ndarray, 즉 행렬임.
# barracks.jpg라는 사진은 width가 3243 px, height이 2208 px
# img는 흑백이기 때문에 3243x2208 행렬에 흑백 정도치를 갖고 있을 것.

# 사진 출력하기
# cv2.imshow("창 이름", 사진)
# cv2.imshow('image', img)
cv2.imshow('image', img)

# 입력 받기
# cv2.waitKey(n 밀리세컨드)
# n 밀리세컨드 동안 주기적으로 키보드 입력이 있는지 확인함. 특정 키보드 입력으로 한정해줄 수도 있음.
# n == 0 이면 계속해서 키보드 입력을 기다리는 상태
# 64 비트 기기에선 뒤에 & 0xFF 추가해줘야됨
cv2.waitKey(0) & 0xFF

# 창 종료하기
# cv2.destroyAllWindows()
# 걍 존재하는 모든 창 없애버림
# cv2.destroyWindow("창 이름")
# 특정 창을 없앰
cv2.destroyAllWindows()