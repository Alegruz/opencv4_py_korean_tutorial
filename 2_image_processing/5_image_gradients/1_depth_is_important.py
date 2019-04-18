import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 보통 출력 dtype은 cv.CV_8U, 혹은 np.uint8로 설정해주었다.
# 헌데 여기에는 약간의 문제가 있다.
# 흑백 전환은 기울기가 양수지만, 백흑 전환은 기울기가 음수다.
# 그렇기 때문에 데이터를 np.uint8로 전환할 때 모든 음수인 기울기는 값이 0으로 치환되버린다.
# 즉, 그 모서리는 없어지는 것이다.

# 만약 모서리 두 개 다 인지하고 싶다면, 우선 cv.CV_8U보다는 더 나은 dtype을 사용해준다.
# 예를 들어 cv.CV_16S, cv.CV_64F 등이 있다.
# 그 다음 그 값들을 전부 절대값을 씌워 양수로 만든 다음, cv.CV_8U로 치환해준다.
# 아래 코드에서 직접 이 과정을 수평 Sobel 필터에 적용해보자

img = cv.imread('2_image_processing/5_image_gradients/rectangle.png', 0)

# 출력 dtype = cv.CV_8U
sobelx8u = cv.Sobel(img, cv.CV_8U, 1, 0, ksize = 5)

# 출력 dtype = cv.CV_64F. 절대값 받아서 cv.CV_8U로 치환
sobelx64f = cv.Sobel(img, cv.CV_64F, 1, 0, ksize = 5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1, 3, 1), plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()