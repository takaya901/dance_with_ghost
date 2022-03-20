from audioop import add
import cv2
import numpy as np

base_img = cv2.imread('imgs/base.png')
add_img = cv2.imread('imgs/add.png')

alpha = 0.6
dst = cv2.addWeighted(base_img, alpha, add_img, 1-alpha, 0)

# cv2.imshow("base", base_img)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()