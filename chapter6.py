#------ Joining Images ------#

import cv2
import numpy as np

img = cv2.imread('resources/xyber.jpg')
img_resize = cv2.resize(img, (370, 480))

#TODO ---> SCALE IMAGE

# The images should have same no of color channels
imgHor = np.hstack((img_resize, img_resize, img_resize))
imgVer = np.vstack((img_resize, img_resize))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)