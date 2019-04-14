import cv2
import numpy as np

# 배울 것들
# EVENT_LBUTTONDOWN -> 마우스 좌클릭 됐는지
# EVENT_MOUSEMOVE   -> 마우스 움직였는지
# EVENT_LBUTTONUP   -> 마우스 좌클릭 뗏는지

drawing = False # 마우스 버튼이 입력되면 True
mode = True     # 만약 True면 직사각형을 그림. 'm' 누르면 원 모드로 바뀜
ix, iy = -1, -1 # 마우스 좌표

# 마우스 입력 받기
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode    # 전역변수 선언
    
    # 그림 그리기 시작
    if (event == cv2.EVENT_LBUTTONDOWN):    # 마우스 좌클릭시
        drawing = True                      # 그림 그리기 활성화
        ix, iy = x, y
    
    # 그림 그리는 중
    elif (event == cv2.EVENT_MOUSEMOVE):    # 마우스 움직일 때
        if (drawing == True):               # 그림 그리는 중이라면
            if (mode == True):                                          # 직사각형 모드면
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)   # 직사각형 그리고
            else:                                                       # 아니면
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)             # 원을 그린다
        
    # 그림 그리기 끝
    elif (event ==  cv2.EVENT_LBUTTONUP):                           # 마우스 좌클릭 떼면
        drawing = False                                             # 그림 그리기 비활성화
        if (mode == True):                                          # 직사각형 모드면
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)   # 직사각형 그리고
        else:                                                       # 아니면
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)             # 원 그린다

img = np.zeros((512, 512, 3), np.uint8)     # 검은 색 사진
cv2.namedWindow("image")                    # 창 만들고
cv2.setMouseCallback("image", draw_circle)  # 마우스 입력 받을 준비 완료

while(True):
    cv2.imshow("image", img)                    # 창 띄우고
    
    # 키보드 명령어 받기
    k = cv2.waitKey(1) & 0xFF
    if (k == ord('m')):                         # 모드 바꾸기
        mode = not mode
    elif (k == ord('c')):                       # 그림 그린 부분 초기화
        img[:] = 0
    elif (k == 27):                             # 종료
        break

cv2.destroyAllWindows()
    