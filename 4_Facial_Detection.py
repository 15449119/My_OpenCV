import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'E:\OpenCV\haar\front_face.xml')
while True :
    ret ,frame = cap.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(img_gray, 3, 5)
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w,  y+h), (255, 0,0), 1)
        

    #print(face)     >>>>>result will be things like:[252, 229, 160, 160]>>a rectangle
    #cv2.imshow('gray', img_gray)
    cv2.imshow('original' ,frame)

    key = cv2.waitKey(3)
    if key == 32:
        break

cap.release()
cv2.destroyAllWindows()
