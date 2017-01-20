import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    img_gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)

    img_edge = cv2.Canny(img_gray ,50 ,50)
    



    cv2.imshow( 'video' ,frame)
    cv2.imshow('Gray_Pic' ,img_gray)
    cv2.imshow('img_edge' ,img_edge)
#General Format    
    key = cv2.waitKey(3)
    if key == 32:  #space_key
        break

#General Format
cap.release()
cv2.destroyAllWindows()
