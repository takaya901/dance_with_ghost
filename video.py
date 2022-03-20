import cv2
from collections import deque
import time
from icecream import ic

start_time = time.perf_counter()

# 遅れて表示するためのバッファ
frame_queue = deque()
buffer_time = 2
buffer_idx = 0
alpha = 0.6

cap1 = cv2.VideoCapture(0)

while(True):
    ret1, frame1 = cap1.read()
    frame_queue.append(frame1)
    # cv2.imshow('frame1',frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #buffer_time経過したらアルファブレンド開始
    now = time.perf_counter()
    if(now - start_time < buffer_time):
        continue

    dst = cv2.addWeighted(frame1, alpha, frame_queue.popleft(), 1-alpha, 0)
    cv2.imshow('frame2',dst)
    buffer_idx += 1

cap1.release()
cv2.destroyAllWindows()