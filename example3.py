"""
color를 gray로 바꾸고 이
진화를 통해서 물체검출하기
"""

import cv2

def nothing(x):
    pass

cv2.namedWindow('binary')
cv2.createTrackbar('threshold', 'binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'binary', 85)

img_color = cv2.imread('redball.PNG', cv2.IMREAD_COLOR)

cv2.imshow('Color', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', img_gray)
cv2.waitKey(0)

while(True):
    low= cv2.getTrackbarPos('threshold', 'binary')
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY_INV)
    #이진화할 gray이미지, threshold값,
    # cv2.THRESH_BINARY일경우 threshold보다 큰 값을 255로 변환
    cv2.imshow('binary', img_binary )

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    cv2.imshow('result', img_result)

    if cv2.waitKey(1)&0xFF == 27:
        break
        #ESC누르면 loop 끝내기


cv2.destroyAllWindows()