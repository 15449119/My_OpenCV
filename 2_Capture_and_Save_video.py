#load video source
import cv2
import numpy as ny

cap = cv2.VideoCapture(0)

'''
>>>Below codes are for recording and saving video to local<<<
fourcc=cv2.VideoWriter_fourcc(*'DIVX') 
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps=cap.get(cv2.CAP_PROP_FPS)----cannot work ,seems get None value
out = cv2.VideoWriter(r'E:\guang.avi', fourcc, 16, size )  #Get image flow, so called video
'''

while  (cap.isOpened()):
    
    ret, frame = cap.read()
    cv2.imshow("ME" ,frame)

    key=cv2.waitKey(3)
    if (key == 32):
        break

#    out.write(frame)
cap.release()
#out.release()
cv2.destroyAllWindows()

'''
while displaying theimage , it wait for 3 millseconds for any Key input.
if now key pressed, then go to next while loop to display next frame
 if the specified key pressed , exexute the "break" to exit the loop.
'''
