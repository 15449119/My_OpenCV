import cv2
import numpy as np

img = cv2.imread(r'c:/Users/wangyiguang/Desktop/son.jpg')

img = cv2.resize(img, (2,4))
img_grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

print('color image :' ,img.shape)
print('-------------')
print(img)
print("----Gray image-------")
print(img_grey)
print('------gray shape----')
print(img_grey.shape)