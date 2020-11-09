"""
harris corner detection
"""

import cv2 as cv
import numpy as np
import time


img_color = cv.imread('chessboard.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

"""
void Sobel(InputArray src, OutputArray dst, int ddepth, int dx, int dy, int ksize=3, double scale=1, double delta=0, int borderType=BORDER_DEFAULT )
src - 입력 이미지
dst - 목적 이미지
ddepth - output image depth
xorder - x에 대한 미분 차수
yorder - y에 대한 미분 차수
ksize - Sobel 커널의 사이즈. 1, 3, 5, 7만 가능.
scale - optional scale factor for the computed derivative values.
delta - optional delta value that is added to the results prior to storing them in dst.
borderType - 픽셀 외삽 방법.
"""

img_sobel_x = cv.Sobel(img_gray, cv.CV_32F, 1, 0) #가로 경계선 구하기
img_sobel_y = cv.Sobel(img_gray, cv.CV_32F, 0, 1) #세로 경계선 구하기


IxIx = img_sobel_x * img_sobel_x
IyIy = img_sobel_y * img_sobel_y
IxIy = img_sobel_x * img_sobel_y


height, width = img_color.shape[:2]

window_size = 5
offset = int(window_size/2)

r = np.zeros(img_gray.shape)

start = time.clock()
for y in range(offset, height-offset):
    for x in range(offset, width-offset):
        window_IxIx = IxIx[y-offset:y+offset+1, x-offset:x+offset+1]
        window_IyIy = IyIy[y-offset:y+offset+1, x-offset:x+offset+1]
        window_IxIy = IxIy[y-offset:y+offset+1, x-offset:x+offset+1]

        Mxx = window_IxIx.sum()
        Myy = window_IyIy.sum()
        Mxy = window_IxIy.sum()


        det = Mxx*Myy - Mxy*Mxy
        trace = Mxx + Myy

        r[y,x] = det - 0.04 * (trace ** 2)


cv.normalize(r,r,0.0,1.0,cv.NORM_MINMAX)

for y in range(offset, height-offset):
    for x in range(offset, width-offset):
        if r[y, x] > 0.4:
            img_color.itemset((y, x, 0), 0)
            img_color.itemset((y, x, 1), 0)
            img_color.itemset((y, x, 2), 255)


end = time.clock()
print(end-start)


cv.imshow("original", img_color)
cv.waitKey(0)