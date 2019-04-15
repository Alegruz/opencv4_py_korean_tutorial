import cv2
import numpy as np

# 배울 것
# cv2.add() / + operator -> shape과 dtype이 같은 두 이미지를 더함

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))    # 250 + 10 = 260 => 255 (dtype == uint8이므로 unsigned int 8비트 최대값은 2^8 - 1 = 255)

print(x + y)    # 250 + 10 = 260, 260 % 256 = 4