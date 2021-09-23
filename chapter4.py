#--------- Shapes and Text ---------#

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[200:300, 100: 300] = 0, 255, 0 <---- Coloring the image

# line(img, starting offset, ending offset, color, thickness)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 1)
cv2.rectangle(img, (0, 0), (200, 300), (255, 0, 0), 2)
# cv2.rectangle(img, (0, 0), (200, 300), (255, 0, 0), cv2.FILLED) # Either put thickness or cv2.FILLED (yk why)
cv2.circle(img, (300, 50), 30, (255, 155, 0), cv2.FILLED)
cv2.putText(img, "Xyber Open Cv", (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 0), 2) # org -> origin

cv2.imshow("Image", img)
cv2.waitKey(0)