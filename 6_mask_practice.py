##---------------------------------------3. 背景提取/去背景-------------------------------------
##mask 是一种0，1 分布的数组。 应用bitwise_and 时，‘0’的部分被置0，1的部分被保留原数值不便(原色)

import cv2
import numpy as np

img_1 = cv2.imread(r'c:/Users/wangyiguang/Desktop/piclib/car.jpg')  #读取背景图
img_2 = cv2.imread(r'c:/Users/wangyiguang/Desktop/piclib/logo.jpg') #读取前景图-即需要加在背景上的图
roi_fg = img_2[0:300, 0:300] #根据前景图的尺寸估算出前景图需要extact的部分的范围，如果不清楚可以不用截取，直接用整图
roi_bg = img_1[0:300, 0:300 ]#相应的背景图也要选出对应相同尺寸的区域用户放前景图。（可以不从（0,0）开始）

img2_gray = cv2.cvtColor(roi_fg, cv2.COLOR_BGR2GRAY) #转成gray_scale，为threshold做准备
_, mask = cv2.threshold(img2_gray, 200, 255, cv2.THRESH_BINARY ) #treshold，得到mask和inv_mask
inv_mask = cv2.bitwise_not(mask)
#extract背景时，所用mask的背景是1（即白色），其余部分为0 （即黑色）
#extract前景是，所用mask的前景是1（即黑色），其余部分为1 （即白色）

img1_bg= cv2.bitwise_and(roi_bg, roi_bg, mask = mask)
img2_fg = cv2.bitwise_and(roi_fg,roi_fg, mask = inv_mask)
dst = cv2.add(img1_bg, img2_fg)
img_1[0:300, 0:300 ] = dst #将合成的bg+fg赋给原图的对应位置(即：roi_bg)

cv2.imshow('img_1', img_1)

