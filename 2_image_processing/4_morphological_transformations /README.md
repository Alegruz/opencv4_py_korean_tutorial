# 4 단원. 형태변환

### 목표

1. erosion, dilation, opening, closing과 같은 형태변환들을 배울 것

2. cv.erode(), cv.dilate(), cv.morphologyEx()와 같은 함수들을 배울 것

### 이론

형태변환이란 이미지의 형태에 따른 간단한 작업이다.<br>
보통 이진 이미지에 사용한다.<br>
두 가지 입력을 받는데, 첫번째는 원본 이미지이고, 두번째는 구조원소, 혹은 작업의 특성을 결정하는 커널이다.<br>
기본적인 형태연산자로는 erosion침식과 dilation확장 두 가지가 있다.

#### Erosion

erosion은 간단히 얘기하자면 마치 토사유출과 같은 말이다.<br>
이미지의 중요한 전경의 테두리를 침식시킨다. (전경 부분은 최대한 하얀색으로 유지하라)<br>
그래서 그게 무슨 작업을 한다는 뜻인가?<br>
커널이 이미지에 2d convolution 작업을 쭉 할 것이다.<br>
이 때 원본 이미지의 픽셀(1이거나 0)은 커널 밑의 픽셀들이 전부 1이면 1이 될 것이다. 그게 아니라면 침식될 것이다.(값이 0이 될 것이다)<br><br>
즉, 테두리 근처의 모든 픽셀은 커널의 사이즈에 따라 값이 0이 될 것이다.<br>
전경에 있는 물체의 굵기나 크기는 줄어든다. 간단히 얘기하면 이미지의 하얀 부분이 줄어든다는 소리다.<br>
이는 작은 하얀색 노이즈를 없애거나 붙어있는 두 물체를 떼어내는 데에 유용하다.<br>
함수 cv.erode()를 사용한다

#### Dilation

erosion의 반대말이다.<br>
커널 밑의 픽셀 중 하나라도 1이면 중간 픽셀 원소는 1이다.<br>
그렇기 때문에 이미지의 하얀 부분이나 전경 오브젝트의 크기를 키운다.<br>
보통 노이즈를 지우는 경우에 erosion을 한 다음 dilation을 해준다.<br>
erosion은 화이트 노이즈를 지워주지만, 그 과정에서 물체를 줄이기 때문에 dilation을 통해 물체를 다시 키워야한다.<br>
어차피 erosion에 의해 노이즈는 지워졌으므로 하얀색이 다시 커질 염려는 없다.<br>
오브젝트에서 구분된 부분을 다시 잇는데에도 사용된다.<br>
함수 cv.dilate()을 사용한다.

#### Opening

opening은 erosion 이후에 dilation을 사용하는 작업의 동의어다.<br>
위에서 설명했듯이 노이즈를 지우는데 효과적이다.<br>
함수 cv.morphologyEx(img, cv.MORPH_OPEN, kernel)를 사용한다.

#### Closing

closing은 opening의  반대말이다. dilation 이후에 erosion을 해주는 것이다.<br>
전경에 작은 구멍을 닫아주거나 검은색 점을 만드는데 매우 유용하다.<br>
함수 cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)를 사용한다.

#### Morphological Gradient

dilation한 이미지와 erosion한 이미지를 뺀 이미지다.<br>
물체의 테두리를 출력할 것이다.<br>
함수는 cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)를 사용한다.

#### Top Hat

입력 이미지와 opening한 이미지를 뺀 이미지다.<br>
함수는 cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)를 사용한다.

#### Black Hat

closing한 입력 이미지와 입력 이미지를 뺀 이미지다.<br>
함수는 cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)를 사용한다.

### Structuring Element 원소 구조화

우리는 numpy를 이용해 예제를 통해 stucturing element를 직접 구현해보았다.<br>
직사각형 모습이지만, 타원/원형 커널이 필요할 때도 있다.<br>
이런 경우에 OpenCV의 함수 중 cv.getStructuringElement()를 사용해주면 된다.<br>
커널의 shape과 size를 패스해주면 원하는 커널을 얻을 수 있다.