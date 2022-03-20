import cv2
from collections import deque
import time
from icecream import ic

ghosts_num = 5
delay = 0.5
buffer_idx = 0
alpha = 0.8

# 遅れて表示するためのバッファ
frame_queues = []
for i in range(ghosts_num):
    frame_queues.append(deque())
ic(range(1, ghosts_num))

cap = cv2.VideoCapture(0)

start_time = time.perf_counter()

while(True):
    ret, frame = cap.read()

    for i in range(ghosts_num):
        #delay秒経過したらアルファブレンド開始
        now = time.perf_counter()
        if(now - start_time < delay * i):
            continue

        if(i == 0):
            frame_queues[i].append(frame)
        else:
            current_frame = frame_queues[i-1].popleft()
            frame_queues[i].append(current_frame)
            frame = cv2.addWeighted(frame, alpha, current_frame, 1-alpha, 0)
            
        cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()