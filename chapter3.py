#-------- RESIZING AND CROPPING --------#

import cv2

img = cv2.imread("resources/xyber.jpg")
print(img.shape)

imgResize = cv2.resize(img, (370, 480)) # Width comes first then height in this case
print(imgResize.shape)

imgCropped = imgResize[0:240, 100:370] # Height comes first then width in this case

# cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)