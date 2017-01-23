import cv2
import numpy as np

#读取为灰度图
path = r'-----------------------'
img= cv2.imread(path, 0) 

#处理序列
equ = cv2.equalizeHist(img) #
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
close_equ = cv2.morphologyEx(equ, cv2.MORPH_CLOSE, kernel)
gau_img = cv2.GaussianBlur(close_equ, (5,5),0)
edge = cv2.Canny(gau_img, 100,200)

#输出
dst = np.hstack((img, equ, close_equ, gau_img, edge))
cv2.imwrite(r'-------------------------', dst)




##cv2.imshow('equ', equ)
##cv2.imshow('open_equ', open_equ)
##cv2.imshow('gau_img', gau_img)
##cv2.imshow('edge', edge)
###cv2.imshow('median', median)





