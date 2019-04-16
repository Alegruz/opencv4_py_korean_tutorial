# 1 단원. 이미지의 기하학적 변환

### 목표

1. 이미지에 평행이동, 회전, 아핀 변환 등을 적용해보는 방법을 배울 것이다.

2. cv.getPerspectiveTransform 함수를 배울 것이다.


### 변환

OpenCV는 두 가지 변환 함수를 제공한다.

1. cv.warpAffine<br>
2x3 변환행렬

2. cv.warpPerspective<br>
3x3 변환행렬
