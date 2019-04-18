import cv2 as cv
import numpy as np, sys

# load image with alpha channel.  use IMREAD_UNCHANGED to ensure loading of alpha channel
A = cv.imread('2_image_processing/7_image_pyramids/aperture.png', cv.IMREAD_UNCHANGED)
B = cv.imread('2_image_processing/7_image_pyramids/black_mesa.png', cv.IMREAD_UNCHANGED)    

# make mask of where the transparent bits are
trans_mask_A = A[:,:,3] == 0
trans_mask_B = B[:,:,3] == 0

# replace areas of transparency with white and not transparent
A[trans_mask_A] = [255, 255, 255, 255]
B[trans_mask_B] = [255, 255, 255, 255]

# new image without alpha channel...
A = cv.cvtColor(A, cv.COLOR_BGRA2BGR)
B = cv.cvtColor(B, cv.COLOR_BGRA2BGR)

# A의 가우스 피라미드를 생성한다
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

# B의 가우스 피라미드를 생성한다
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# A의 라플라스 피라미드를 생성한다
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)

# B의 라플라스 피라미드를 생성한다
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i - 1], GE)
    lpB.append(L)

# 각 층의 좌측절반과 우측절반을 더한다
LS = []
for la, lb in zip(lpA,lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:int(cols/2)], lb[:, int(cols/2):]))
    LS.append(ls)

# 재생성한다
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

# 둘을 연결한 이미지를 생성한다.
real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))

cv.imwrite('2_image_processing/7_image_pyramids/Pyramid_blending2.jpg', ls_)
cv.imwrite('2_image_processing/7_image_pyramids/Direct_blending.jpg', real)