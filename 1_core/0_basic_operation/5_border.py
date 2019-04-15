import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

# 배울 것
# cv2.copyMakeBorder() -> 테두리 만들기

img1 = cv2.imread("1_core/0_image/barracks.jpg")

# 테두리 만들기
# cv2.copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) -> dst
# src: 이미지 소스
# top, bottom, left, right: 상하좌우 테두리 픽셀 길이
# borderType: 테두리 방식. 아래와 같은 방식들이 있음
# cv2.BORDER_CONSTANT: 색이 있는 테두리. 색이 필요하기 때문에 뒤에 value=색 으로 추가적으로 argument 필요함
# cv2.BORDER_REFLECT: 테두리가 마치 거울처럼 됨. fedcba|abcdefgh|hgfedcb 이렇게 됨
# cv2.BORDER_REFLECT_101 == cv2.BORDER_DEFAULT: BORDER_REFLECT랑 비슷함. gfedcb|abcdefgh|gfedcba
# cv2.BORDER_REPLICATE: 마지막 원소가 복제됨. aaaaaa|abcdefgh|hhhhhhh
# cv2.BORDER_WRAP: 패턴화시킴. cdefgh|abcdefgh|abcdefg
# value: cv2.BORDER_CONSTANT가 borderType일 때 색을 지정해줄 때 쓰임
replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, "gray"), plt.title("ORIGINAL")
plt.subplot(232), plt.imshow(replicate, "gray"), plt.title("REPLICATE")
plt.subplot(233), plt.imshow(reflect, "gray"), plt.title("REFLECT")
plt.subplot(234), plt.imshow(reflect101, "gray"), plt.title("REFLECT101")
plt.subplot(235), plt.imshow(constant, "gray"), plt.title("CONSTANT")

plt.show()