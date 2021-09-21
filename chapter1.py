import cv2

print("Package Imported")

# '''--------- Image Reading -----------'''
# img = cv2.imread("resources/xyber.jpg")
# img_small = cv2.resize(img, (370, 480))
#
# cv2.imshow("Output", img_small)
#
# # 0 means infinite and other values mean that many milliseconds
# # waitkey helps to delay the script
# cv2.waitKey(0)

# '''--------- Video Capture -----------'''
# cap = cv2.VideoCapture("resources/gow.mp4")
#
# while True :
#     success, img = cap.read()
#     img_small = cv2.resize(img, (800, 480))
#     cv2.imshow("Video", img_small)
#     if cv2.waitKey(3) & 0xFF == ord('q') :
#         print("Stopping")
#         break

# '''--------- Webcam Capture ----------'''
# Setting the VideoCaptures parameter as 0 sets the webcam as the capture resource
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 360)
cap.set(10, 1)

while True :
    success, img = cap.read()
    img_small = cv2.resize(img, (800, 480))
    cv2.imshow("Web Cam", img_small)
    if cv2.waitKey(3) & 0xFF == ord('q') :
        print("Stopping")
        break