import cv2
import matplotlib.pyplot as plt
import  numpy as np
img=cv2.imread("D:\car.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("car",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("D:\car_gray.png",img)
