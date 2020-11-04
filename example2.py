import cv2

cap = cv2.VideoCapture('video.mp4')

while(True):
    ret, img_color = cap.read()

    if ret == False:
        break

    cv2.imshow('color', img_color)
    if cv2.waitKey(1)&0xFF == 27:
        break

cap.release()