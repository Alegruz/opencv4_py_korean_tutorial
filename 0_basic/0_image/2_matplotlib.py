import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt    # Matplotlib. 창 만들어줄 때 유용한 UI 제공

# matplotlib을 통해 창 UI를 생성함

# 배울 함수들
# plt.imread() -> 사진을 입력받음
# plt.show() -> 사진을 출력함

# 흑백 사진 받기
img = cv.imread("0_basic/0_image/barracks.jpg", 0)

# 사진 입력받기
# plt.imshow(사진 오브젝트, cmap, interpolation)
plt.imshow(img, cmap = "gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([]) # X Y 좌표 가리기

# 사진 출력하기
# plt.show()
plt.show()