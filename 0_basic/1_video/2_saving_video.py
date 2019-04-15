import numpy as np
import cv2 as cv

# 영상을 저장함

# 배울 것들
# cv.VideoWriter 오브젝트
# FourCC 코드 -> 4바이트(4글자) 영상 코덱 식별자 (fourcc.org에서 리스트 확인할 수 있음)

# 코덱 지정해주기
# 리눅스: DIVX, XVID, MJPG, X264, WMV1, WMV2 (우분투는 MJPG 쓰세용)
# 윈도우: DIVX
# 코덱 = cv.VideoWriter_fourcc('4', '바', '이', '트')
# 코덱 = cv.VideoWriter_fourcc(*'4바이트')
fourcc = cv.VideoWriter_fourcc(*"MJPG")

# VideoWriter 오브젝트를 생성
# cv.VideoWriter("저장파일이름.확장자", 코덱, 프레임수(fps), 프레임사이즈, isColor)
# isColor이 참이면 색있는 영상. 아니면 흑백
out = cv.VideoWriter("0_basic/1_video/output.avi", fourcc, 20.0, (640, 480))

# 카메라 입력 받기
cap = cv.VideoCapture(0)

while(cap.isOpened()):
    # 프레임 입력 받기
    ret, frame = cap.read()

    # 입력 받았는지 확인
    if (ret == True):
        # 프레임 상하반전
        # cv.flip(프레임, 반전식별자)
        # 반전식별자 == False면 상하. True면 좌우
        frame = cv.flip(frame, 0)

        # 프레임을 저장
        out.write(frame)

        # 최종 프레임 출력
        cv.imshow("frame", frame)
        if (cv.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break

# 작업이 전부 끝나면 모든 작업 종료
cap.release()
out.release()
cv.destroyAllWindows()