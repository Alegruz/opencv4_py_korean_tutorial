import cv2 as cv
import numpy as np

img = cv.imread('2_image_processing/2_image_threshold/bimodal_image.png', 0)
blur = cv.GaussianBlur(img, (5, 5), 0)

# 정규화된 히스토그램과 히스토그램의 누적 분포 함수를 생성한다
# cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist
# 행렬의 값을 통해 히스토그램을 생성한다.
# images. 입력 행렬들. 모두 반드시 같은 차원, 크기와 타입을 가져야한다.
# channels. 히스토그램을 계산할 때 사용할 채널 목록.
# mask. 필수는 아님. 만약 사용할거면 사용할 행렬 image[i]와 갖은 크기를 갖는 8비트 행렬이어야한다.
# histSize. 각 차원별 히스토그램의 크기를 원소로 갖는 행렬
# ranges. 각 차원의 히스토그램의 bin boundaries의 차원행렬들의 행렬.
# hist. 출력 히스토그램.
hist = cv.calcHist([blur], [0], None, [256], [0, 256])
print(type(hist))
# ndarray.ravel()
# 다차원 행렬을 1-D 행렬로 바꾼다.
# ndarray.max()
# 행렬의 최대값을 출력한다
hist_norm = hist.ravel() / hist.max()   # 히스토그램의 각 원소에 히스토그램의 최대값으로 나눠준다
# ndarray.cumsum()
# 해당 행렬의 누적합 행렬을 출력한다.
# 예) [1 2 3 4 5 6].cumsum() == [1 3 6 10 15 21]
Q = hist_norm.cumsum()

bins = np.arange(256)

# numpy.inf
# 상수. 무한이라는 뜻
fn_min = np.inf
thresh = -1

for i in range(1, 256):
    # numpy.hsplit(ary, indices_or_sections)
    # ary. 나뉘어질 행렬
    # indices_or_sections.
    p1, p2 = np.hsplit(hist_norm,[i]) # 확률
    q1, q2 = Q[i], Q[255] - Q[i] # 클래스의 누적합
    b1, b2 = np.hsplit(bins, [i]) # 무게
    
    # 평균과 변화량 찾기
    m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
    v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
    
    # 최소함수 계산하기
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# OpenCV 함수로 Otsu 임계점 찾기
ret, otsu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print( "{} {}".format(thresh, ret) )