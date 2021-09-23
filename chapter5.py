#------ Warp Perspective ------#
# Basically flattening a curved image (aka Bird Eye or Top down view)

import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[108, 215], [288, 185], [152, 485], [355, 442]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image Warped", imgOutput)
cv2.waitKey(0)