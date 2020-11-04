import cv2

img_color = cv2.imread('IU.png', cv2.IMREAD_COLOR)

cv2.namedWindow('show image') #툴바 붙일때 사용
cv2.imshow('show image', img_color) #(윈도우 식별자, 이미지)

cv2.waitKey(0) #0은 무한히 키보드 입력 기다림
cv2.destroyAllWindows() #윈도우 자원 해제

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY) #gray로 변환

cv2.imshow('show image', img_gray)
cv2.waitKey(0)

cv2.imwrite('saveimage.jpg', img_gray)

cv2.destroyAllWindows() #윈도우 자원 해제