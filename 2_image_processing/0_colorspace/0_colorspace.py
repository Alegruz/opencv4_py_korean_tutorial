import cv2 as cv
import numpy as np

# 이미지의 색공간 바꾸는 방법.

# 기존의 튜토리얼 0_basic/1_video/0_video_capture.py에서 색변환을 할 때 cv.cvtColor(src, code)라는 함수를 사용했음.
# 여기서 code가 바로 색변환을 할 때 사용한 flag.
# 예를 들어 src 이미지 흑백사진으로 변환할 때 cv.COLOR_BGR2GRAY를 사용해주었음.

flags = [ i for i in dir(cv) if i.startswith("COLOR_")] # OpenCV에서 이미지를 색변환할 때 사용하는 flag들 전부
print(flags)

# 예를 들어 BGR을 Gray로 색변환하려면 cv.COLOR_BGR2GRAY를 사용함
# BGR을 HSV로 변환하려면 cv.COLOR_BGR2HSV를 사용함.
# BGR은 Blue, Green, Red이고 HSV는 Hue(색), Saturation(암도), Value(선명도)를 의미함