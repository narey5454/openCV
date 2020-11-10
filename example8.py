"""
컨투어를 활용한 도형 검출
"""

import cv2 as cv

img_color = cv.imread('triangle.PNG',cv.IMREAD_COLOR)
cv.imshow('result', img_color)
cv.waitKey(0)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imshow('result', img_gray)
cv.waitKey(0)

ret, img_binary = cv.threshold(img_gray, 127,255, cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
cv.imshow('result', img_binary)
cv.waitKey(0)

contours, hierarachy = cv.findContours(img_binary, cv.RETR_EXTERNAL
                                       , cv.CHAIN_APPROX_SIMPLE) #외곽의 contour 검출
#contour를 구성하는 성분의 개수 출력
for cnt in contours:
    size = len(cnt)
    print(size)

    epsilon = 0.005 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    #직선으로 근사화
    size = len(approx)
    print(size)

    cv.line(img_color, tuple(approx[0][0]), tuple(approx[size-1][0]), (0,255,0), 3)
    for k in range(size-1):
        cv.line(img_color, tuple(approx[k][0]), tuple(approx[k+1][0]), (0,255,0), 3)
    #근사화한 컨투어를 그려줌

    cv.putText(img_color, str(size), (50,50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, 8)

cv.imshow('result', img_color)
cv.waitKey(0)
#컨투어 성분의 개수가 193개에서 3개로 줄어듬
#이를 바탕으로 도형을 판정함