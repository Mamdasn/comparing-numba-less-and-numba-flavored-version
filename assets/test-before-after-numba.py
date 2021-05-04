from im2dhisteq import im2dhisteq
import numpy as np
import cv2
import time

img = cv2.imread('cloudy-day.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v = hsv[:, :, 2].copy()

for i in range(5):
    t0 = time.time()
    v = im2dhisteq(v)
    t1 = time.time()
    print(t1-t0)
