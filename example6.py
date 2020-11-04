"""
canny edge detector
1.노이즈 제거 (gaussian blur)
2.에지 그레디언트 계산
3.non-maximum suppression
4.htsteresis thresholding
"""

import cv2

def nothing():
    pass

img_gray = cv2.imread('example6.PNG', cv2.IMREAD_GRAYSCALE)


cv2.namedWindow("Canny Edge")
cv2.createTrackbar('low threshold', 'Canny Edge', 0, 1000, nothing)
cv2.createTrackbar('high threshold', 'Canny Edge', 0, 1000, nothing)

cv2.setTrackbarPos('low threshold', 'Canny Edge', 50)
cv2.setTrackbarPos('high threshold', 'Canny Edge', 150)

cv2.imshow("Original", img_gray)

while True:

    low = cv2.getTrackbarPos('low threshold', 'Canny Edge')
    high = cv2.getTrackbarPos('high threshold', 'Canny Edge')

    img_canny = cv2.Canny(img_gray, low, high)
    cv2.imshow("Canny Edge", img_canny)

    if cv2.waitKey(1)&0xFF == 27:
        break

cv2.destroyAllWindows()