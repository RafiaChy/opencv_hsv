import cv2
import numpy as np
def passfunction(x):
    pass
cv2.namedWindow('tracking')
cv2.createTrackbar('LH', 'tracking', 0,255, passfunction)
cv2.createTrackbar('UH', 'tracking', 255,255, passfunction)
cv2.createTrackbar('LS', 'tracking', 0,255, passfunction)
cv2.createTrackbar('US', 'tracking', 255,255, passfunction)
cv2.createTrackbar('LV', 'tracking', 0,255, passfunction)
cv2.createTrackbar('UV', 'tracking', 255,255, passfunction)
while True:
    frame = cv2.imread('hsv.png',1)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos('LH', 'tracking')
    uh = cv2.getTrackbarPos('UH', 'tracking')
    ls = cv2.getTrackbarPos('LS', 'tracking')
    us = cv2.getTrackbarPos('US', 'tracking')
    lv = cv2.getTrackbarPos('LV', 'tracking')
    uv = cv2.getTrackbarPos('UV', 'tracking')
    lower_region= np.array([lh,ls,lv])
    upper_region = np.array([uh,us,uv])
    mask = cv2.inRange(hsv, lower_region, upper_region)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    button = cv2.waitKey(1)& 0xff
    if button==ord('q'):
        break
cv2.destroyAllWindows()