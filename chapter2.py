#------- BASIC FUNCTIONS -------#

import cv2
import numpy as np

big_img = cv2.imread("resources/xyber.jpg")
img = cv2.resize(big_img, (370, 480))

kernel = np.ones((7, 7), np.uint8) # A matrix of size 7x7 with 1s and values from 0-255(np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (5, 5), 0)
imgCanny = cv2.Canny(img, 200, 200) # Canny Edge Detector
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erotion Image", imgEroded)
cv2.waitKey(0)