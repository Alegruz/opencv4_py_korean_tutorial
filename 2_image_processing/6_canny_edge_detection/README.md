# 6 단원. 케니 테두리 탐지

### 목표

1. 케니 테두리 탐지의 개념

2. cv.Canny() 함수

### 이론

케니 테두리 탐지는 매우 유명한 테두리 탐지 알고리즘이다. John F. Canny가 개발했다.

1. 케니 테두리 탐지는 여러 단계에 걸친 알고리즘이다.

2. 노이즈 감소

테두리 탐지는 이미지의 노이즈에 민감하므로, 언제나 첫번째 단계로 5x5 가우스 필터를 이용해 노이즈를 제거해준다.<br>
제거하는 방법은 이미 이전 단원에서 공부했다.

3. 이미지에서 grandient의 intensity 찾기

이미지를 다듬은 다음에 Sobel 커널을 수직 수평 둘 다 필터처리해주어 수평 수직 방향의 일계도함수 (Gx, Gy)를 구한다.<br>
이 두 이미지를 기반으로 edge gradient와 각 픽셀의 방향을 구해줄 수 있다.<br>
<code>
edge_gradient(G) = sqrt(Gx^2 + Gy^2)
</code><br>
<code>
Angle(θ) = tan^−1(Gy / Gx)
</code><br>
Gradient direction은 언제나 모서리에 수직이다. 그 뒤 수직, 수평, 그리고 두 대각선, 총 네 개의 선 중 하나로 반올림 시킨다.

4. Non-maximum Suppression

gradient magnitude와 direction을 구한 다음, 모서리의 일부가 아닌 불필요한 픽셀을 제거하기 위해 이미지를 전체적으로 스캔한다.<br>
이를 하려면 모든 픽셀을 검사해야되는데, 이 때 픽셀이 gradient의 방향에 있는 근처 픽셀들 중에서 가장 큰 값인지를 확인한다.<br>
![](nms.jpg)<br>
점 A는 모서리 위에 있다(수직 방향으로).<br>
Gradient direction은 모서리에 수직이다.<br>
점 B와 점 C는 gradient direction에 있는 점들이다.<br>
즉, 점 A가 점 B와 점 C보다 가장 큰 값을 갖는지 확인한다.<br>
만약 점 A가 최대값을 갖는다면, 다음 단계로 넘어가고, 아니라면, 값이 압축된다. (값이 0이 된다)<br><br>
간단히 말해, "얇은 테두리"를 가진 이진 이미지를 얻는다.

5. 히스테리시스 임계처리법

이 단계에선 어떤 모서리가 진짜 테두리인지를 판별한다. 이를 위해선 두 가지 임계점이 필요하다. minVal과 maxVal이다.<br>
maxVal보다 큰 intensity gradient를 갖는 모서리는 확실한 테두리고,<br>
minVal보다 작은 모서리는 테두리가 아니므로, 삭제한다.<br>
이 두 값 사이에 있는 모서리들은 연결성에 따라 테두리인지 아닌지 판별한다.<br>
만약 확실한 테두리와 연결되어있다면, 테두리의 일부로 인정하고, 아니라면 마찬가지로 삭제한다. 다음 사진을 보라:<br>
![](hysteresis.jpg)
모서리 A는 maxVal보다 크므로 확실한 테두리이다.<br>
모서리 C는 maxVal보다 작다 하더라도, 모서리 A과 연결되어있으므로 테두리로 인정되어 C 부분의 곡선은 테두리로 인정한다.<br>
모서리 B는 minVal보다 크고, 모서리 C와 같은 공간에 있지만 확실한 테두리와 연결되어있지 않기 때문에 삭제된다.<br>
이렇기 때문에 minVal과 maxVal의 값은 신중하게 정해주어야한다.<br><br>
이 단계에서는 테두리를 마치 긴 선처럼 취급하기 때문에 작은 픽셀 노이즈들을 없애주기도 한다.

모든 단계를 마친 다음 나온 결과는 이미지의 테두리이다.

### OpenCV에서 케니 테두리 탐지

OpenCV는 위의 단계를 단 하나의 함수로 제공한다. 바로 cv.Canny()다.<br>
<code>
cv.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])->edges
</code><br>
image: 입력 이미지<br>
threshold1, threshold2: minVal와 maxVal<br>
apertureSize: aperture의 크기. 즉, 이미지의 gradient를 찾는데 사용될 Sobel 커널의 크기. 기본값은 3이다.<br>
L2gradient: gradient magnitude를 찾는데 사용되는 연산. 만약 값이 True면 위에 3번에서 소개한 정교한 방식의 연산을 한다. 만약 False라면 함수 Edge_Gradient(G)=|Gx|+|Gy|를 사용한다. 기본값은 False다.