import cv2
import numpy as np
import time
cap = cv2.VideoCapture( 0 )
bgst = cv2.createBackgroundSubtractorMOG2()

num = 100
fourcc=cv2.VideoWriter_fourcc(*'DIVX') 
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
path = r'E:\OpenCV\Moment_Detect_Record\%d.avi' %num
out = cv2.VideoWriter( path, fourcc, 16, size )

while True:
    ret, frame = cap.read()
    dst = bgst.apply(frame)
    dst = np.array(dst, np.int8)

    if np.count_nonzero(dst)<3000:  # use this value to adjust the "Sensitivity“
        
        print("No movement Detected")
        out.release()
    else:
        print('somethign is moving %s' %(time.ctime())) # You can customize your own ALARM here
        out.write(frame)
        global num
        num=num+1 
        

    
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(dst, 'Movement Tracing', (130, 30), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('dst' ,dst)


    
    key = cv2.waitKey(1)
    if key == 32:
        break 

cap.release()
cv2.destroyAllWindows()
    

