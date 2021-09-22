import cv2

big_img = cv2.imread("resources/xyber.jpg")
img = cv2.resize(big_img, (370, 480))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)