"""
contour

contour approximation method simple과 none의 차이
simple은 직선일 경우 시작점과 끝점만, none은 전부

contour retrieval mode
tree는 contour가 계층 구조로 이루어짐
list는 모든 contour가 동등한 리스트형태로
external는 외곽쪽의 contour만
ccomp는 모든 contour를 두개의 계층으로 만듬

영역 크기, 근사화, 무게중심, 경계사각형, convex hull, convexity defects를
contour를 사용하여 구할수 있다
"""

import cv2 as cv

img_color = cv.imread('test.PNG')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)
# contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST
#                                       ,cv.CHAIN_APPROX_SIMPLE)

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST
                                      ,cv.CHAIN_APPROX_NONE)


# cv.drawContours(img_color, contours, -1, (0,255, 0), 3)
# cv.drawContours(img_color, contours, 0, (255, 0, 0), 3)

for cnt in contours:
    for p in cnt:
        cv.circle(img_color, (p[0][0], p[0][1]), 10, (255,0,0), -1)

cv.imshow('result', img_color)
cv.waitKey(0)