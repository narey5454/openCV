"""
HSV 색공간에서 특정색 검출하기
"""

import numpy as np
import cv2

color = [255, 0, 0] #파란색
pixel = np.uint8([[color]]) #한픽셀로 구성된 이지미로 바꿈

hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV) #BGR을 HSV로 변환
hsv = hsv[0][0] #pixel값만 가져옴

print("bgr: ", color) #255,0,0
print("hsv: ", hsv) #120,255,255

img_color = cv2.imread('img_color.PNG')
height, width = img_color.shape[:2]

img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

lower_blue = (120-10, 30, 30) #30,30은 너무 흰색, 너무 검은색을 검출하지 않기 위해
upper_blue = (120+10, 255,255)
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
#range안에 있는것은 흰색, 아닌것은 검은 색으로

img_result = cv2.bitwise_and(img_color,img_color, mask=img_mask)

cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()