# 5 단원. Image Gradients

### 목표

1. image gradient, 모서리 등을 찾는 방법을 배움

2. cv.Sobel(), cv.Scharr(), cv.Laplacian() 등과 같은 함수를 배움

### 이론

OpenCV는 세 가지 gradient 필터, 혹은 HPF를 제공한다. 바로 Sobel, Scharr, 그리고 Laplacian이다.


#### Sobel과 Scharr 도함수

Sobel 연산자는 가우스 smoothing과 미분방정식이 합쳐진 연산이다. 그렇기 때문에 좀 더 노이즈를 잘 처리한다.<br>
도함수의 방향을 수직 혹은 수평으로 정해줄 수 있다. (argument인 yorder과 xorder을 통해 각각 수직과 수평을 처리해준다)<br>
또한 ksize를 통해 커널의 크기를 지정해줄 수 있다.<br>
ksize = -1이라면 3x3 Scharr 필터가 3x3 Sobel 필터보다 더 좋은 결과를 보여준다.

#### Laplacian 도함수

이미지를 관계식 Δsrc = ((∂^2) * src) / ∂x^2 + ((∂^2)src) / ∂y^2을 통해 이미지의 라플라스를 구한다.<br>
여기서 각 도함수는 Sobel 도함수를 이용해 구한 함수다.<br>
만약 ksize = 1이라면 필터에 다음 커널이 사용된다. 
<pre><code>
kernel = ⎡0  1 0⎤
         ⎢1 -4 1⎥
         ⎣0  1 0⎦
</pre></code>